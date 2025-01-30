import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getSeason, getRankings, getSeasonLastMatches } from 'services/api'; // Assumes an API service to fetch season details
import Header from 'components/visitor/Header';
import Footer from 'components/visitor/Footer';
import RankingTable from "components/visitor/RankingTable.jsx";
import 'styles/tailwind.css';

const SeasonDetail = () => {
  const { id } = useParams();
  const [season, setSeason] = useState(null);
  const [ranking, setRanking] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [lastMatches, setLastMatches] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSeason = async () => {
      try {
        const data = await getSeason(id); // Fetch season details
        const ranking = await getRankings(1, 100, data.start_date);
        const lastMatches = await getSeasonLastMatches(data.id);
        setLastMatches(lastMatches.results);
        setSeason(data);
        setRanking(ranking.results);
      } catch (err) {
        setError('Error al obtener la información de la temporada.');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchSeason();
  }, [id]);

  const calculateSeasonStatus = () => {
    if (!season) return null;

    const today = new Date();
    const startDate = new Date(season.start_date);
    const endDate = new Date(season.end_date);

    if (today < startDate) {
      return 'Próxima';
    } else if (today > endDate) {
      return 'Concluida';
    } else {
      return 'En curso';
    }
  };

  return (
    <div className="bg-gradient-to-r from-gray-800 via-gray-900 to-black min-h-screen text-white flex flex-col">
      <Header />
      <main className="container mx-auto px-4 py-8 flex-grow">
        <h2 className="text-center text-4xl font-bold mb-8">Detalles de la Temporada</h2>
        {isLoading ? (
          <div className="flex justify-center items-center h-64">
            <div className="spinner-border animate-spin inline-block w-12 h-12 border-4 rounded-full text-emerald-500"></div>
          </div>
        ) : error ? (
          <div className="text-center text-red-500">{error}</div>
        ) : (
          <div>
            {/* Season Info */}
            <div className="bg-gray-800 p-6 rounded-lg shadow-lg mb-6">
              <h3 className="text-3xl font-bold mb-4">{season.name}</h3>
              <p className="mb-2">
                <strong>Descripción:</strong> {season.description}
              </p>
              <p className="mb-2">
                <strong>Fecha de Inicio:</strong>{' '}
                {new Date(season.start_date).toLocaleDateString()}
              </p>
              <p className="mb-2">
                <strong>Fecha de Fin:</strong>{' '}
                {new Date(season.end_date).toLocaleDateString()}
              </p>
              <p className="mb-4">
                <strong>Estado:</strong> {calculateSeasonStatus()}
              </p>
              {calculateSeasonStatus() === 'En curso' && (
                <p className="text-emerald-400 font-semibold">
                  Esta temporada está actualmente activa.
                </p>
              )}
            </div>
            {console.log(ranking)}
            {/* Player Rankings */}
            <RankingTable ranking={ranking} title="Ranking de temporada" />

            {/* Recent Matches */}
            <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
              <h4 className="text-2xl font-bold mb-4">Últimos Partidos</h4>
              <ul className="space-y-4">
                {lastMatches.map((match) => (
                  <li
                    key={match.id}
                    className="border-b border-gray-700 pb-4 last:border-b-0"
                  >
                    <p>
                      <strong>Partido:</strong> {match.player1} vs {match.player2}
                    </p>
                    <p>
                      <strong>Resultado:</strong> {match.result}
                    </p>
                    <p>
                      <strong>Fecha:</strong>{' '}
                      {new Date(match.date).toLocaleDateString()}
                    </p>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </main>
      <Footer />
    </div>
  );
};

export default SeasonDetail;
