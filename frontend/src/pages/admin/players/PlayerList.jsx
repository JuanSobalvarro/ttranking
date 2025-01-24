import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import AdminHeader from 'components/admin/AdminHeader';
import AdminFooter from 'components/admin/AdminFooter';
import { getPlayers } from 'services/api.js';
import 'styles/tailwind.css';

function AdminPlayerList() {
  const [players, setPlayers] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const fetchPlayers = async (page = 1) => {
    try {
      const result = await getPlayers(page);
      setPlayers(result.results); // Assuming the API returns { results: [], count: 0, ... }
      setTotalPages(Math.ceil(result.count / 10)); // Update based on page size
    } catch (error) {
      console.error('Error fetching players:', error);
    }
  };

  useEffect(() => {
    fetchPlayers(currentPage);
  }, [currentPage]);

  const handleNextPage = () => {
    if (currentPage < totalPages) setCurrentPage((prevPage) => prevPage + 1);
  };

  const handlePrevPage = () => {
    if (currentPage > 1) setCurrentPage((prevPage) => prevPage - 1);
  };

  return (
    <div>
      <AdminHeader />
      <main className="container mx-auto px-4 py-8">
        <h2 className="text-3xl font-bold mb-6">Lista de Jugadores</h2>
        <Link to="/admin/players/add" className="bg-green-500 text-white px-6 py-3 rounded hover:bg-green-600 mb-6 inline-block">Agregar Nuevo Jugador</Link>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {players.map(player => (
            <div key={player.id} className="bg-white rounded-lg shadow-lg overflow-hidden">
              <img src={player.photo ? player.photo : '/src/assets/images/defaultPlayer.png'} alt={`${player.first_name} ${player.last_name}`} className="w-full h-48 object-cover" />
              <div className="p-6">
                <h5 className="text-xl font-semibold mb-2">{player.first_name} {player.last_name}</h5>
                <p className="text-gray-600 mb-4">{player.alias}</p>
                <p className="text-gray-800 mb-4">Ranking: {player.ranking}</p>
                <Link to={`/admin/players/edit/${player.id}`} className="bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600">Editar</Link>
                <Link to={`/admin/players/delete/${player.id}`} className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 ml-2">Eliminar</Link>
              </div>
            </div>
          ))}
        </div>
        <div className="mt-8 flex justify-between">
          <button
            onClick={handlePrevPage}
            disabled={currentPage === 1}
            className={`px-4 py-2 rounded ${currentPage === 1 ? 'bg-gray-400' : 'bg-blue-500 hover:bg-blue-600'} text-white`}
          >
            Anterior
          </button>
          <span className="text-lg font-medium">Página {currentPage} de {totalPages}</span>
          <button
            onClick={handleNextPage}
            disabled={currentPage === totalPages}
            className={`px-4 py-2 rounded ${currentPage === totalPages ? 'bg-gray-400' : 'bg-blue-500 hover:bg-blue-600'} text-white`}
          >
            Siguiente
          </button>
        </div>
      </main>
      <AdminFooter />
    </div>
  );
}

export default AdminPlayerList;
