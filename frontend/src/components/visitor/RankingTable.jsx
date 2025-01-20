import React from 'react';
import { Link } from 'react-router-dom';
import 'styles/tailwind.css';
import { Table } from 'flowbite-react';
import { getPlayerImage } from "services/helpers.js";

const RankingTable = ({ ranking }) => {
  return (
    <div className="container mx-auto my-12 px-4">
      <h2 className="text-center text-3xl font-bold mb-6">Top 20 Jugadores</h2>
      <div className="overflow-x-auto">
        <Table striped hoverable>
          <thead className="bg-gray-800 text-white">
            <tr>
              <th className="py-3 px-6">Posición</th>
              <th className="py-3 px-6">Jugador</th>
              <th className="py-3 px-6">Nacionalidad</th>
              <th className="py-3 px-6">Puntos</th>
              <th className="py-3 px-6">Partidos</th>
              <th className="py-3 px-6">Victorias</th>
              <th className="py-3 px-6">%Victorias</th>
            </tr>
          </thead>
          <tbody>
            {ranking.map((player, index) => (
              <tr key={player.id} className="border-b">
                <td className="py-3 px-6 text-center">{index + 1}</td>
                <td className="py-3 px-6 flex items-center">
                  <Link to={`/players/${player.id}`} className="flex items-center no-underline text-black">
                    <img
                      src={getPlayerImage(player.photo)}
                      alt={`${player.firstName} ${player.lastName}`}
                      className="w-12 h-12 rounded-full mr-4 object-cover"
                    />
                    <div>
                      <strong className="block">{player.firstName} {player.lastName}</strong>
                      {player.alias && <span className="text-sm text-gray-600">{player.alias}</span>}
                    </div>
                  </Link>
                </td>
                <td className="py-3 px-6 text-center">
                  {player.nationality && (
                    <img
                      src={`https://flagsapi.com/${player.nationality}/flat/32.png`}
                      alt={`Bandera de ${player.nationality}`}
                      className="inline-block"
                    />
                  )}
                  {player.nationality || 'N/D'}
                </td>
                <td className="py-3 px-6 text-center">{player.ranking}</td>
                <td className="py-3 px-6 text-center">{player.matchesPlayed}</td>
                <td className="py-3 px-6 text-center">{player.victories}</td>
                <td className="py-3 px-6 text-center">{player.winrate}%</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
    </div>
  );
};

export default RankingTable;
