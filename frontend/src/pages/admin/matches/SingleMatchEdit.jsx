import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ColorThief from 'colorthief';
import { getPlayers, getSingleMatch, getCurrentSeason, putSingleMatch, putSingleGame, getMatchGames } from 'services/api.js';
import { isDateInBetween } from "services/helpers.js";
import PlayerSelector from 'components/admin/PlayerSelector.jsx';
import MatchDateTimeInput from 'components/admin/MatchDateTimeInput.jsx';
import GamesManager from 'components/admin/GamesManager.jsx';
import 'styles/tailwind.css';
import AdminFooter from 'components/admin/AdminFooter.jsx';
import AdminHeader from 'components/admin/AdminHeader.jsx';
import { Button } from 'flowbite-react';
import AlertModal from "components/admin/AlertModal.jsx";
import ConfirmationModal from "components/admin/ConfirmationModal.jsx";

function SingleMatchEdit() {
    const { id } = useParams();
  const [players, setPlayers] = useState([]);
  const [selectedPlayer1, setSelectedPlayer1] = useState(null);
  const [selectedPlayer2, setSelectedPlayer2] = useState(null);
  const [matchDateTime, setMatchDateTime] = useState('');
  const [season, setSeason] = useState([]);
  const [games, setGames] = useState([{ player1Score: 0, player2Score: 0 }]);
  const [saving, setSaving] = useState(false);
  const [backgroundGradient, setBackgroundGradient] = useState('white');
  const [alert, setAlert] = useState({ isOpen: false, message: '', type: 'success' });
  const [isConfirmationModalOpen, setIsConfirmationModalOpen] = useState(false);

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const result = await getPlayers(1, 100);
        setPlayers(result.results);
      } catch (error) {
        console.error('Error fetching players:', error);
      }
    };

    const fetchSeason = async () => {
      try {
        const season = await getCurrentSeason();
        setSeason(season);
      } catch (error) {
        console.error('Error fetching current season:', error);
      }
    };

    const fetchMatch = async () => {
      try {
        const matchData = await getSingleMatch(id);
        setSelectedPlayer1(matchData.player1.id);
        setSelectedPlayer2(matchData.player2.id);
        setMatchDateTime(matchData.date);
      } catch (error) {
        console.error('Error fetching match data:', error);
      }
    };

    const fetchGames = async () => {
        try {
            const gamesData = await getMatchGames(id, 'singles');
            setGames(gamesData.results);
        } catch (error) {
            console.error('Error fetching games data:', error);
        }
    };

    fetchPlayers();
    fetchSeason();
    fetchMatch();
    fetchGames();
  }, [id]);

  useEffect(() => {
    const updateGradient = async () => {
      const colorThief = new ColorThief();
      const defaultColor = [255, 255, 255]; // Default white background
      const getDominantColor = async (playerId) => {
        if (!playerId) return defaultColor;
        const player = players.find((p) => p.id === Number(playerId));
        if (!player?.photo) return defaultColor;

        const img = new Image();
        img.crossOrigin = 'anonymous'; // Ensure cross-origin access
        img.src = player.photo;

        return new Promise((resolve) => {
          img.onload = () => {
            try {
              const dominantColor = colorThief.getColor(img);
              resolve(dominantColor);
            } catch {
              resolve(defaultColor);
            }
          };
          img.onerror = () => resolve(defaultColor);
        });
      };

      const color1 = await getDominantColor(selectedPlayer1);
      const color2 = await getDominantColor(selectedPlayer2);

      setBackgroundGradient(
        `linear-gradient(to right, rgba(${color1.join(',')}, 0.8), rgba(${color2.join(',')}, 0.8))`
      );
    };

    updateGradient();
  }, [selectedPlayer1, selectedPlayer2, players]);

  const handleGameScoreChange = (gameIndex, player, scoreChange) => {
  setGames((previousGames) => {
    // Create a new array by mapping over the previous games
    return previousGames.map((currentGame, index) => {
      // If we are at the game that needs to be updated
      if (index === gameIndex) {
        // Determine the current player's score key (player1Score or player2Score)
        const scoreKey = player === 'player1' ? 'player1Score' : 'player2Score';

        // Calculate the new score, ensuring it doesn't go below 0
        const newScore = Math.max(0, currentGame[scoreKey] + scoreChange);

        // Return the updated game with the new score
        return {
          ...currentGame,
          [scoreKey]: newScore,
        };
      }

      // If it's not the game we want to update, return it unchanged
      return currentGame;
    });
  });
};


  const addNewGame = () => setGames([...games, { player1Score: 0, player2Score: 0 }]);
  const removeGame = (gameIndex) => setGames((prevGames) => prevGames.filter((_, index) => index !== gameIndex));

  const handleSave = async () => {
    if (!selectedPlayer1 || !selectedPlayer2) {
      setAlert({
        isOpen: true,
        message: "Por favor, selecciona dos jugadores.",
        type: "error",
      });
      return;
    }

    if (selectedPlayer1 === selectedPlayer2) {
      setAlert({
        isOpen: true,
        message: "Los jugadores no pueden ser el mismo.",
        type: "error",
      });
      return;
    }

    if (!matchDateTime) {
      setAlert({
        isOpen: true,
        message: "Por favor, selecciona una fecha y hora para el partido.",
        type: "error",
      });
      return;
    }

    if (!isDateInBetween(matchDateTime, season.start_date, season.end_date)) {
      setAlert({
        isOpen: true,
        message: "La fecha está fuera del rango de la temporada.",
        type: "advice",
      });
      return;
    }

    if (games.length === 0) {
      setAlert({
        isOpen: true,
        message: "Por favor, agrega al menos un juego.",
        type: "error",
      });
      return;
    }

    setSaving(true);

    try {
      const matchData = {
        player1: selectedPlayer1,
        player2: selectedPlayer2,
        date: matchDateTime,
      };

      const matchResponse = await putSingleMatch(id, matchData);

      for (let i = 0; i < games.length; i++) {
        const gameData = {
          match: matchResponse.id,
          player1_score: games[i].player1Score,
          player2_score: games[i].player2Score,
        };
        await putSingleGame(gameData);
      }

      setAlert({
        isOpen: true,
        message: "Partido actualizado con éxito.",
        type: "success",
      });
    } catch (error) {
      console.error('Error updating match:', error);
      setAlert({
        isOpen: true,
        message: "Ocurrió un error al actualizar el partido.",
        type: "error",
      });
    } finally {
      setSaving(false);
    }
  };

  const handleCloseAlertModal = () => setAlert({ ...alert, isOpen: false });

  return (
    <div>
      {/* Modals */}
      <AlertModal
        isOpen={alert.isOpen}
        message={alert.message}
        type={alert.type}
        onClose={handleCloseAlertModal}
      />

      <ConfirmationModal
        isOpen={isConfirmationModalOpen}
        onClose={() => setIsConfirmationModalOpen(false)}
      />

      <AdminHeader />
      <div
        className="min-h-screen flex flex-col items-center justify-center px-4 sm:px-6 lg:px-8"
        style={{ background: backgroundGradient }}
      >
        <h2 className="text-2xl md:text-4xl font-bold mb-4 md:mb-8 text-center">
          Editar Partido Individual
        </h2>
        <div
          className="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-8 mb-8"
        >
          <PlayerSelector
            players={players}
            selectedPlayer={selectedPlayer1}
            setSelectedPlayer={setSelectedPlayer1}
            label="Seleccionar Jugador 1"
          />
          <h3 className="text-2xl md:text-4xl font-bold">VS</h3>
          <PlayerSelector
            players={players}
            selectedPlayer={selectedPlayer2}
            setSelectedPlayer={setSelectedPlayer2}
            label="Seleccionar Jugador 2"
          />
        </div>
        <MatchDateTimeInput matchDateTime={matchDateTime} setMatchDateTime={setMatchDateTime} />
        <GamesManager
          games={games}
          handleGameScoreChange={handleGameScoreChange}
          addNewGame={addNewGame}
          removeGame={removeGame}
        />
        <div className="mt-4 md:mt-8">
          <Button className="w-full md:w-auto" onClick={handleSave} disabled={saving}>
            {saving ? 'Guardando...' : 'Actualizar Partido'}
          </Button>
        </div>
      </div>
      <AdminFooter />
    </div>
  );
}

export default SingleMatchEdit;
