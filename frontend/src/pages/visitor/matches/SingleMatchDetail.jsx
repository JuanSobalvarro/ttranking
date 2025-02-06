import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getSingleMatch, getPlayer } from 'services/api'; // Assume this API function fetches match details
import Header from 'components/visitor/Header';
import Footer from 'components/visitor/Footer';
import 'styles/tailwind.css';
import MatchDetailCard from "components/visitor/MatchDetailCard.jsx";

function SingleMatchDetail() {
  const { id } = useParams();
  const [match, setMatch] = useState(null);
  const [player1, setPlayer1] = useState(null);
  const [player2, setPlayer2] = useState(null);
  const [winner, setWinner] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMatchDetails = async () => {
      try {
        setLoading(true);
        const data = await getSingleMatch(id); // Fetch match details using the match ID
        const p1 = await getPlayer(data.player1); // Fetch player details for player 1
        const p2 = await getPlayer(data.player2); // Fetch player details for player 2
        const w = await getPlayer(data.winner); // Fetch player details for the winner

        setPlayer1(p1);
        setPlayer2(p2);
        setWinner(w);
        setMatch(data);
      } catch (err) {
        console.error('Error fetching match details:', err);
        setError('Failed to fetch match details. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    if (id) fetchMatchDetails();
  }, [id]);

  if (loading) {
    return <div className="text-center text-white mt-20">Loading match details...</div>;
  }

  if (error) {
    return <div className="text-center text-red-500 mt-20">{error}</div>;
  }

  return (
    <div className="bg-gradient-to-r from-gray-800 via-gray-900 to-black min-h-screen text-white flex flex-col">
      <Header />
      <MatchDetailCard matchType={'singles'} />
      <Footer />
    </div>
  );
}

export default SingleMatchDetail;
