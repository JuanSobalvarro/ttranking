import React from 'react';
import { Link } from 'react-router-dom';
import { getPlayerImage } from "src/services/helpers.js";
import 'styles/tailwind.css';

const SubSpotlight = ({ topByWinrate }) => {
  return (
    <div className="mx-auto my-12 text-center bg-green-700 text-white p-12 rounded-lg max-w-screen-lg">
      <h2 className="text-4xl font-bold mb-6">Jugadores Play2Win</h2>
      <p className="text-xl mb-8">Estos jugadores se destacan por su winrate, ganándose el título de "Play2Win", jugar para ganar</p>
      <div className="flex flex-wrap justify-center">
        {topByWinrate.map((player, index) => {
          let winrateGradient;
          let nameGradient;

          // Apply gradient based on winrate ranking (for top 5 players)
          switch(index) {
            case 0:
              winrateGradient = "bg-gradient-to-r from-yellow-400 to-yellow-500"; // Gold
              nameGradient = "bg-gradient-to-r from-yellow-400 to-yellow-500"; // Gold
              break;
            case 1:
              winrateGradient = "bg-gradient-to-r from-gray-300 to-gray-500"; // Silver
              nameGradient = "bg-gradient-to-r from-gray-300 to-gray-500"; // Silver
              break;
            case 2:
              winrateGradient = "bg-gradient-to-r from-orange-400 to-orange-600"; // Bronze
              nameGradient = "bg-gradient-to-r from-orange-400 to-orange-600"; // Bronze
              break;
            case 3:
              winrateGradient = "bg-gradient-to-r from-pink-400 to-pink-600"; // Copper
              nameGradient = "bg-gradient-to-r from-pink-400 to-pink-600"; // Copper
              break;
            case 4:
              winrateGradient = "bg-gradient-to-r from-blue-400 to-blue-600"; // Steel
              nameGradient = "bg-gradient-to-r from-blue-400 to-blue-600"; // Steel
              break;
            default:
              winrateGradient = "bg-gradient-to-r from-gray-600 to-gray-800"; // Default gray for others
              nameGradient = "bg-gradient-to-r from-gray-600 to-gray-800"; // Default gray for others
          }

          return (
            <div key={player.id} className="w-full md:w-1/4 p-4">
              <Link to={`/players/${player.id}`} className="block bg-gray-900 text-white p-6 rounded-lg shadow-lg">
                <img
                  src={getPlayerImage(player.photo)}
                  className="w-full h-auto object-cover rounded-lg"
                  alt={`${player.first_name} ${player.last_name}`}
                />
                <div className="mt-4">
                  {/* Player Name with Gradient */}
                  <h3 className={`text-2xl font-bold text-transparent bg-clip-text ${nameGradient}`}>
                    {player.first_name} {player.last_name}
                  </h3>
                  {player.alias && <p className="text-lg italic">{player.alias}</p>}
                  <p className="mt-2"><strong>Partidos Jugados:</strong> {player.matchesPlayed}</p>
                  {/* Winrate with Gradient */}
                  <p className={`text-4xl mt-4 text-transparent bg-clip-text ${winrateGradient}`}>
                    {player.winrate}%
                  </p>
                </div>
              </Link>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default SubSpotlight;
