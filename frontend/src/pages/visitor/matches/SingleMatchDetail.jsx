import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getSingleMatch, getPlayer } from 'services/api'; // Assume this API function fetches match details
import Header from 'components/visitor/Header';
import Footer from 'components/visitor/Footer';
import 'styles/tailwind.css';

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
      <main className="container mx-auto px-4 py-8 flex-grow">
        <h2 className="text-center text-4xl font-bold mb-8">Match Details</h2>
        <div className="bg-gray-700 rounded-lg shadow-lg p-6 space-y-8">
          {match ? (
            <>
              <div className="flex justify-center items-center space-x-8">
                {/* Player 1 */}
                <div className="flex items-center space-x-4">
                  <img
                    src={player1.photo || '/src/assets/images/defaultPlayer.png'}
                    alt={player1.first_name + ' ' + player1.last_name || 'Player 1'}
                    className="w-24 h-24 rounded-full object-cover"
                  />
                  <div className="text-lg font-semibold">{player1.first_name + ' ' + player1.last_name || 'Unknown Player'}</div>
                </div>

                {/* VS */}
                <div className="text-4xl font-bold text-white">VS</div>

                {/* Player 2 */}
                <div className="flex items-center space-x-4">
                  <img
                    src={player2.photo || '/src/assets/images/defaultPlayer.png'}
                    alt={player2.first_name + ' ' + player2.last_name || 'Player 2'}
                    className="w-24 h-24 rounded-full object-cover"
                  />
                  <div className="text-lg font-semibold">{player2.first_name + ' ' + player2.last_name || 'Unknown Player'}</div>
                </div>
              </div>
              <div className="mt-4 text-lg space-y-2">
                <p><strong>Date:</strong> {new Date(match.date).toLocaleString()}</p>
                <p><strong>Season:</strong> {match.season || 'N/A'}</p>
                <p><strong>Score:</strong> {match.player1_score} - {match.player2_score}</p>
                <p><strong>Winner:</strong> {winner.first_name + ' ' + winner.last_name || 'No winner'}</p>
              </div>
            </>
          ) : (
            <p className="text-center">Match details are unavailable.</p>
          )}
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default SingleMatchDetail;
