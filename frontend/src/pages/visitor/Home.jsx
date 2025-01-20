import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getHomeData } from 'services/api.js';
import Header from 'components/visitor/Header.jsx';
import Footer from 'components/visitor/Footer.jsx';
import 'styles/tailwind.css';
import 'styles/pingpong.css'
import Spotlight from "components/visitor/Spotlight.jsx";
import SubSpotlight from "components/visitor/SubSpotlight.jsx";
import RankingTable from "components/visitor/RankingTable.jsx";

function Home() {
  const [matchesPlayed, setMatchesPlayed] = useState(0);
  const [topPlayers, setTopPlayers] = useState([]);
  const [topByWinrate, setTopByWinrate] = useState([]);
  const [ranking, setRanking] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getHomeData();
        console.log(data);
        setMatchesPlayed(data.matchesPlayed);
        setTopPlayers(data.topPlayers);
        setTopByWinrate(data.topByWinrate);
        setRanking(data.ranking);
      } catch (error) {
        console.error('Error fetching home data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className='bg-gray-900'>
      <Header />


      {/* Hero Section with dynamic table tennis-inspired background */}
      <section className="hero-section bg-gradient-to-r from-green-600 via-black to-green-900 text-white text-center relative overflow-hidden">
        {/* Animated Lights mimicking the fast movement of a ping-pong ball */}
        <div className="absolute inset-0 bg-opacity-50 bg-black z-0"></div>
        <div className="absolute inset-0 bg-gradient-to-r from-green-900 via-teal-900 to-green-600 opacity-10 animate-pulse z-0"></div>


        <div className="text-center py-16 z-10 relative">
          <h1 className="text-4xl font-bold text-white">Bienvenido al Sistema de Clasificación de Tenis de Mesa</h1>
          <p className="text-xl text-white mt-6">Sigue el rendimiento de los jugadores y consulta las últimas clasificaciones.</p>
          <div className="mt-8">
            <Link className="bg-green-500 hover:bg-green-700 text-white font-bold py-3 px-6 rounded-full mr-4 transition-all" to="/players">Ver Jugadores</Link>
            <Link className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-full transition-all" to="/matches">Ver Partidos</Link>
          </div>
        </div>
      </section>

      <div className="bg-green-500 text-white py-3">
        <div className="text-center">
          <div className="text-lg font-semibold">Total Partidos Jugados: {matchesPlayed}</div>
        </div>
      </div>

      <Spotlight topPlayers={topPlayers} />

      <SubSpotlight topByWinrate={topByWinrate} />

      <RankingTable ranking={ranking} />


      {/* Description Section */}
      <div className="container mx-auto my-12 text-center">
        <h2 className="text-3xl font-bold mb-6">Sobre el sistema de Clasificación</h2>
        <p className="text-xl mb-6">
          Nuestro sistema de clasificación de tenis de mesa está diseñado para ofrecer una representación precisa
          y dinámica del rendimiento de los jugadores a lo largo del tiempo. Cada jugador acumula puntos en
          función de los resultados de sus victorias.
        </p>
        <p className="text-xl mb-6">
          Ya sean principiantes, avanzados o profesionales todos pueden participar de nuestro grupo y ser
          registrado/a en nuestra clasificación.
        </p>
        <h3 className="text-2xl font-bold mb-6">Temporada actual</h3>
        <p className="text-xl">
          La temporada actual empezó lunes 5 de agosto, se otorgan 2 puntos por cada victoria y las derrotas no
          restan puntos a los participantes.
        </p>
      </div>

      <Footer />
    </div>
  );
}

export default Home;
