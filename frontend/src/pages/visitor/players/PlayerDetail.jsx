import React, { useEffect, useState, useRef } from 'react';
import { useParams } from 'react-router-dom';
import { getPlayer, getRankingForPlayer, getSeasonForDate } from 'services/api.js';
import ColorThief from 'colorthief';
import Header from 'components/visitor/Header';
import Footer from 'components/visitor/Footer';
import 'styles/tailwind.css';

function PlayerDetail() {
  const { id } = useParams();
  const [player, setPlayer] = useState(null);
  const [loading, setLoading] = useState(true);
  const [radialGradient, setRadialGradient] = useState('');
  const [palette, setPalette] = useState([]);
  const [ranking, setRanking] = useState([]);
  const imgRef = useRef(null);

  useEffect(() => {
    const fetchPlayer = async () => {
      try {
        const result = await getPlayer(id);
        const season = await getSeasonForDate(new Date());
        console.log(season);
        const rankingResult = await getRankingForPlayer(id, season.id);
        console.log(rankingResult.results[0]);
        setRanking(rankingResult.results[0]);
        setPlayer(result);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching player details:', error);
        setLoading(false);
      }
    };

    fetchPlayer();
  }, [id]);

  useEffect(() => {
    if (imgRef.current) {
      const colorThief = new ColorThief();
      const img = imgRef.current;
      img.crossOrigin = 'anonymous';

      const generateRadialGradient = (palette) => {
        return `radial-gradient(circle at 50% 50%, rgba(${palette[0][0]}, ${palette[0][1]}, ${palette[0][2]}, 0.8), rgba(${palette[1][0]}, ${palette[1][1]}, ${palette[1][2]}, 0.6) 50%, rgba(${palette[2][0]}, ${palette[2][1]}, ${palette[2][2]}, 0.4) 80%)`;
      };

      const processImage = () => {
        const palette = colorThief.getPalette(img, 5);
        setPalette(palette);
        setRadialGradient(generateRadialGradient(palette));
      };

      if (img.complete) {
        processImage();
      } else {
        img.addEventListener('load', processImage);
      }
    }
  }, [player]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen bg-gradient-to-r from-teal-600 via-blue-600 to-indigo-600 text-white text-3xl">
        Cargando...
      </div>
    );
  }

  if (!player) {
    return (
      <div className="flex items-center justify-center h-screen bg-gradient-to-r from-teal-600 via-blue-600 to-indigo-600 text-white text-3xl">
        Jugador no encontrado
      </div>
    );
  }

  return (
    <div className="min-h-screen text-white flex flex-col backdrop-blur-3xl relative overflow-hidden">
      <Header />
      <main
        className="w-full flex-grow relative flex justify-center items-center overflow-hidden"
        style={{
          background: radialGradient || 'rgba(0, 0, 0, 0.7)',
        }}
      >
        {/* Decorative Color Drops */}
        {palette.map((color, i) => (
          <div
            key={i}
            className="absolute rounded-full"
            style={{
              width: `${Math.random() * 200 + 50}px`,
              height: `${Math.random() * 200 + 50}px`,
              backgroundColor: `rgba(${color[0]}, ${color[1]}, ${color[2]}, 0.4)`,
              top: `${Math.random() * 100}%`,
              left: `${Math.random() * 100}%`,
              filter: 'blur(40px)',
            }}
          />
        ))}

        <div className="flex flex-col my-20 md:flex-row items-center bg-gray-800 bg-opacity-90 rounded-lg shadow-2xl p-8 md:p-16 max-w-3xl max-h-80 z-10">
          {/* Player Photo */}
          <div className="w-20 h-20 md:w-72 md:h-72 bg-gray-700 rounded-full overflow-hidden shadow-lg mb-6 md:mb-0">
            <img
              ref={imgRef}
              src={player.photo ? player.photo : '/src/assets/images/defaultPlayer.png'}
              alt={`${player.first_name} ${player.last_name}`}
              className="w-full h-full object-cover shadow-xl"
            />
          </div>

          {/* Player Info */}
          <div className="mt-6 md:mt-0 md:ml-8 text-center md:text-left">
            <h2 className="text-4xl font-extrabold text-green-400 mb-4">
              {player.first_name} {player.last_name}
            </h2>
            <p className="text-xl italic text-gray-300 mb-3">
              {player.alias || ' '}
            </p>
            <p className="text-lg text-gray-200 mb-2">
              Sexo: <span className="font-semibold text-neutral-100">{player.gender}</span>
            </p>
            <p className="text-lg text-gray-200 mb-2">
              Fecha de nacimiento:{' '}
              <span className="font-semibold text-neutral-100">
                {player.date_of_birth || 'N/A'}
              </span>
            </p>
            <p className="text-lg text-gray-200 mb-2">
              Nacionalidad:{' '}
              <span className="font-semibold text-neutral-100">
                {player.nationality}
                <img src={`https://flagsapi.com/${player.nationality}/flat/32.png`}></img>
              </span>
            </p>
            <p className="text-lg text-gray-200 mb-2">
              Ranking: <span className="font-semibold text-neutral-100">{ranking.ranking}</span>
            </p>
            <p className="text-lg text-gray-200 mb-2">
              Partidos jugados:{' '}
              <span className="font-semibold text-neutral-100">{ranking.matches_played}</span>
            </p>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default PlayerDetail;
