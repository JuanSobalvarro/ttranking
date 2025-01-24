import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getDoubleMatch, getPlayer } from 'services/api';
import Header from 'components/visitor/Header';
import Footer from 'components/visitor/Footer';
import 'styles/tailwind.css';

function DoubleMatchDetail() {
  const { id } = useParams();
  const [match, setMatch] = useState(null);
  const [team1Player1, setTeam1Player1] = useState(null);
  const [team1Player2, setTeam1Player2] = useState(null);
  const [team2Player1, setTeam2Player1] = useState(null);
  const [team2Player2, setTeam2Player2] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMatchDetails = async () => {
      try {
        setLoading(true);
        const data = await getDoubleMatch(id);
        const team1p1 = await getPlayer(data.team1_player1);
        const team1p2 = await getPlayer(data.team1_player2);
        const team2p1 = await getPlayer(data.team2_player1);
        const team2p2 = await getPlayer(data.team2_player2);

        setTeam1Player1(team1p1);
        setTeam1Player2(team1p2);
        setTeam2Player1(team2p1);
        setTeam2Player2(team2p2);
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
        <h2 className="text-center text-4xl font-bold mb-8">Doubles Match Details</h2>
        <div className="bg-gray-700 rounded-lg shadow-lg p-6 space-y-8">
          {match ? (
            <>
              <div className="flex justify-center items-center space-x-8">
                {/* Team 1 */}
                <div className="flex items-center space-x-6">
                  <div className="flex items-center space-x-4">
                    <img
                      src={team1Player1.photo || '/src/assets/images/defaultPlayer.png'}
                      alt={team1Player1.first_name + ' ' + team1Player1.last_name || 'Player 1'}
                      className="w-24 h-24 rounded-full object-cover"
                    />
                    <div className="text-lg font-semibold">{team1Player1.first_name + ' ' + team1Player1.last_name || 'Unknown Player'}</div>
                  </div>
                  <div className="flex items-center space-x-4">
                    <img
                      src={team1Player2.photo || '/src/assets/images/defaultPlayer.png'}
                      alt={team1Player2.first_name + ' ' + team1Player2.last_name || 'Player 2'}
                      className="w-24 h-24 rounded-full object-cover"
                    />
                    <div className="text-lg font-semibold">{team1Player2.first_name + ' ' + team1Player2.last_name || 'Unknown Player'}</div>
                  </div>
                </div>

                {/* VS separator */}
                <div className="text-4xl text-gray-400 font-bold">VS</div>

                {/* Team 2 */}
                <div className="flex items-center space-x-6">
                  <div className="flex items-center space-x-4">
                    <img
                      src={team2Player1.photo || '/src/assets/images/defaultPlayer.png'}
                      alt={team2Player1.first_name + ' ' + team2Player1.last_name || 'Player 1'}
                      className="w-24 h-24 rounded-full object-cover"
                    />
                    <div className="text-lg font-semibold">{team2Player1.first_name + ' ' + team2Player1.last_name || 'Unknown Player'}</div>
                  </div>
                  <div className="flex items-center space-x-4">
                    <img
                      src={team2Player2.photo || '/src/assets/images/defaultPlayer.png'}
                      alt={team2Player2.first_name + ' ' + team2Player2.last_name || 'Player 2'}
                      className="w-24 h-24 rounded-full object-cover"
                    />
                    <div className="text-lg font-semibold">{team2Player2.first_name + ' ' + team2Player2.last_name || 'Unknown Player'}</div>
                  </div>
                </div>
              </div>
              <div className="mt-4 text-lg space-y-2">
                <p><strong>Date:</strong> {new Date(match.date).toLocaleString()}</p>
                <p><strong>Season:</strong> {match.season || 'N/A'}</p>
                <p><strong>Score:</strong> {match.team1_score} - {match.team2_score}</p>
                <p><strong>Winners:</strong> {match.winners || 'No winner'}</p>
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

export default DoubleMatchDetail;
