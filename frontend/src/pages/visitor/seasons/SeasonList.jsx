import React, { useEffect, useState } from 'react';
import { getSeasons } from 'services/api'; // Assumes getSeasons fetches the list of seasons from the backend
import Header from 'components/visitor/Header';
import Footer from 'components/visitor/Footer';
import 'styles/tailwind.css';

function SeasonList() {
  const [seasons, setSeasons] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchSeasons = async () => {
      try {
        const data = await getSeasons(); // Fetch the seasons
        setSeasons(data.results);
      } catch (error) {
        console.error('Error fetching seasons:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchSeasons();
  }, []);

  const renderSeasons = () => (
    <div className="mb-8">
      <h3 className="text-2xl font-bold mb-4">Temporadas de Ranking</h3>
      {seasons.length > 0 ? (
        <table className="table-auto w-full border-collapse border border-gray-700 text-center text-sm">
          <thead>
            <tr className="bg-gray-700 text-white">
              <th className="border border-gray-600 px-4 py-2">ID</th>
              <th className="border border-gray-600 px-4 py-2">Nombre</th>
              <th className="border border-gray-600 px-4 py-2">Fecha de Inicio</th>
              <th className="border border-gray-600 px-4 py-2">Fecha de Fin</th>
              <th className="border border-gray-600 px-4 py-2">Detalles</th>
            </tr>
          </thead>
          <tbody>
            {seasons.map((season) => (
              <tr key={season.id} className="hover:bg-gray-700">
                <td className="border border-gray-600 px-4 py-2">{season.id}</td>
                <td className="border border-gray-600 px-4 py-2">{season.name}</td>
                <td className="border border-gray-600 px-4 py-2">
                  {new Date(season.start_date).toLocaleDateString()}
                </td>
                <td className="border border-gray-600 px-4 py-2">
                  {new Date(season.end_date).toLocaleDateString()}
                </td>
                <td className="border border-gray-600 px-4 py-2">
                  <a
                    href={`/seasons/${season.id}`}
                    className="text-emerald-500 hover:underline"
                  >
                    Ver Detalles
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-center text-gray-400 py-4">No hay temporadas disponibles.</p>
      )}
    </div>
  );

  return (
    <div className="bg-gradient-to-r from-gray-800 via-gray-900 to-black min-h-screen text-white flex flex-col">
      <Header />
      <main className="container mx-auto px-4 py-8 flex-grow">
        <h2 className="text-center text-4xl font-bold mb-8">Lista de Temporadas</h2>
        {isLoading ? (
          <div className="flex justify-center items-center h-64">
            <div className="spinner-border animate-spin inline-block w-12 h-12 border-4 rounded-full text-emerald-500"></div>
          </div>
        ) : (
          renderSeasons()
        )}
      </main>
      <Footer />
    </div>
  );
}

export default SeasonList;
