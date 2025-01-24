import React, { useEffect, useState } from 'react';
import { getSingleMatches, getDoubleMatches, getPlayer } from 'services/api.js';
import Header from 'components/visitor/Header';
import Footer from 'components/visitor/Footer';
import 'styles/tailwind.css';
import { Spinner } from 'flowbite-react';
import ConfirmationModal from "components/admin/ConfirmationModal.jsx";

function MatchList() {
  const [singleMatches, setSingleMatches] = useState([]);
  const [doubleMatches, setDoubleMatches] = useState([]);
  const [players, setPlayers] = useState({});
  const [currentSinglesPage, setCurrentSinglesPage] = useState(1);
  const [currentDoublesPage, setCurrentDoublesPage] = useState(1);
  const [totalSinglesPages, setTotalSinglesPages] = useState(1);
  const [totalDoublesPages, setTotalDoublesPages] = useState(1);
  const [loading, setLoading] = useState(true);

  const matchesPerPage = 10;

  const fetchPlayers = async (playerIds) => {
    try {
      for (const id of playerIds) {
        if (!players[id]) {
          const player = await getPlayer(id);
          setPlayers((prev) => ({ ...prev, [id]: `${player.first_name} ${player.last_name}` }));
        }
      }
    } catch (error) {
      console.error('Error fetching players:', error);
    }
  };

  const fetchMatches = async () => {
    try {
      const singleResult = await getSingleMatches(currentSinglesPage, matchesPerPage);
      const singlePlayerIds = singleResult.results.flatMap((match) => [match.player1, match.player2]);
      await fetchPlayers(singlePlayerIds);
      setSingleMatches(singleResult.results);
      setTotalSinglesPages(Math.ceil(singleResult.count / matchesPerPage));

      const doubleResult = await getDoubleMatches(currentDoublesPage, matchesPerPage);
      const doublePlayerIds = doubleResult.results.flatMap((match) => [
        match.team1_player1,
        match.team1_player2,
        match.team2_player1,
        match.team2_player2,
      ]);
      await fetchPlayers(doublePlayerIds);
      setDoubleMatches(doubleResult.results);
      setTotalDoublesPages(Math.ceil(doubleResult.count / matchesPerPage));
    } catch (error) {
      console.error('Error fetching matches:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    fetchMatches();
  }, [currentSinglesPage, currentDoublesPage]);

  const getPlayerName = (id) => players[id] || 'N/A';

  const renderMatches = (matches, type) => (
      <div>
      <h3 className="text-2xl font-bold mb-4">{type === 'single' ? 'Partidos Individuales' : 'Partidos Dobles'}</h3>
      <table className="table-auto w-full border-collapse border border-gray-300 text-center text-sm">
        <thead>
          <tr className="bg-gray-800">
            <th className="border border-gray-300 px-4 py-2">Fecha</th>
            <th className="border border-gray-300 px-4 py-2">{type === 'single' ? 'Jugador 1' : 'Equipo 1'}</th>
            <th className="border border-gray-300 px-4 py-2">{type === 'single' ? 'Jugador 2' : 'Equipo 2'}</th>
            <th className="border border-gray-300 px-4 py-2">Juegos ganados</th>
            <th className="border border-gray-300 px-4 py-2">Ganador</th>
            <th className="border border-gray-300 px-4 py-2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {matches.length > 0 ? (
            matches.map((match) => (
              <tr key={match.id} className="hover:bg-gray-600">
                <td className="border border-gray-300 px-4 py-2">{new Date(match.date).toLocaleString()}</td>
                <td className="border border-gray-300 px-4 py-2">
                  {type === 'single'
                    ? getPlayerName(match.player1)
                    : `${getPlayerName(match.team1_player1)} / ${getPlayerName(match.team1_player2)}`}
                </td>
                <td className="border border-gray-300 px-4 py-2">
                  {type === 'single'
                    ? getPlayerName(match.player2)
                    : `${getPlayerName(match.team2_player1)} / ${getPlayerName(match.team2_player2)}`}
                </td>
                <td className="border border-gray-300 px-4 py-2">
                  {type === 'single'
                    ? `${match.player1_games}-${match.player2_games}`
                    : `${match.team1_games}-${match.team2_games}`}
                </td>
                <td className="border border-gray-300 px-4 py-2">{type === 'single' ? getPlayerName(match.winner) : match.winners}</td>
                <td className="border border-gray-300 px-4 py-2">
                  <div className="flex justify-center space-x-2">
                    <a
                      href={`/matches/${type === 'single' ? 'singles' : 'doubles'}/${match.id}/edit`}
                      className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
                    >
                      Editar
                    </a>
                    <button
                        onClick={() => handleDeleteClick(match)}
                        className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                    >
                      Eliminar
                    </button>
                  </div>
                </td>
              </tr>
            ))
          ) : (
              <tr>
                <td colSpan="6" className="text-center text-gray-500 py-4">
                No hay partidos registrados.
              </td>
            </tr>
          )}
        </tbody>
      </table>
      <div className="flex justify-between mt-4">
        <button
          onClick={() => (type === 'single' ? setCurrentSinglesPage : setCurrentDoublesPage)((prev) => Math.max(prev - 1, 1))}
          disabled={type === 'single' ? currentSinglesPage === 1 : currentDoublesPage === 1}
          className="bg-gray-200 text-gray-800 px-4 py-2 rounded hover:bg-gray-300"
        >
          Anterior
        </button>
        <span className="text-gray-600">
          {`Página ${
            type === 'single' ? currentSinglesPage : currentDoublesPage
          } de ${type === 'single' ? totalSinglesPages : totalDoublesPages}`}
        </span>
        <button
          onClick={() => (type === 'single' ? setCurrentSinglesPage : setCurrentDoublesPage)((prev) => prev + 1)}
          disabled={type === 'single' ? currentSinglesPage === totalSinglesPages : currentDoublesPage === totalDoublesPages}
          className="bg-gray-200 text-gray-800 px-4 py-2 rounded hover:bg-gray-300"
        >
          Siguiente
        </button>
      </div>
    </div>
  );

  return (
    <div className="bg-gradient-to-r from-gray-800 via-gray-900 to-black min-h-screen text-white flex flex-col">
      <Header />
      <main className="container mx-auto px-4 py-8 flex-grow">
        <h2 className="text-center text-4xl font-bold mb-8">Lista de Partidos</h2>
        {loading ? (
          <div className="flex justify-center items-center">
            <Spinner size="xl" />
          </div>
        ) : (
          <>
            {renderMatches(singleMatches, 'single')}
            {renderMatches(doubleMatches, 'double')}
          </>
        )}
      </main>
      <Footer />
    </div>
  );
}

export default MatchList;
