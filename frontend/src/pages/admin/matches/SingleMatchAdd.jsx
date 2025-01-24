import React, { useState, useEffect } from 'react';
import ColorThief from 'colorthief';
import { getPlayers, postSingleMatch, postSingleGame } from 'services/api.js';
import PlayerSelector from 'components/admin/PlayerSelector.jsx';
import MatchDateTimeInput from 'components/admin/MatchDateTimeInput.jsx';
import GamesManager from 'components/admin/GamesManager.jsx';
import 'styles/tailwind.css';
import AdminFooter from 'components/admin/AdminFooter.jsx';
import AdminHeader from 'components/admin/AdminHeader.jsx';
import { Button } from 'flowbite-react';

function SingleMatchAdd() {
  const [players, setPlayers] = useState([]);
  const [selectedPlayer1, setSelectedPlayer1] = useState(null);
  const [selectedPlayer2, setSelectedPlayer2] = useState(null);
  const [matchDateTime, setMatchDateTime] = useState('');
  const [games, setGames] = useState([{ player1Score: 0, player2Score: 0 }]);
  const [saving, setSaving] = useState(false);
  const [backgroundGradient, setBackgroundGradient] = useState('white');

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const result = await getPlayers(1, 100);
        setPlayers(result.results);
      } catch (error) {
        console.error('Error fetching players:', error);
      }
    };

    fetchPlayers();
  }, []);

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

  const handleGameScoreChange = (gameIndex, player, change) => {
    setGames((prevGames) =>
      prevGames.map((game, index) =>
        index === gameIndex
          ? {
              ...game,
              [player]: Math.max(0, game[player] + change),
            }
          : game
      )
    );
  };

  const addNewGame = () => setGames([...games, { player1Score: 0, player2Score: 0 }]);
  const removeGame = (gameIndex) => setGames((prevGames) => prevGames.filter((_, index) => index !== gameIndex));

  const handleSave = async () => {
    if (!selectedPlayer1 || !selectedPlayer2) {
      alert('Selecciona ambos jugadores antes de guardar el partido.');
      return;
    }

    if (selectedPlayer1 === selectedPlayer2) {
      alert('Un jugador no puede enfrentarse a sí mismo.');
      return;
    }

    if (!matchDateTime) {
      alert('Selecciona una fecha y hora para el partido.');
      return;
    }

    if (!isMatchInSeason()) {
      setSeasonError('La fecha del partido no está dentro de una temporada activa.');
      return;
    } else {
      setSeasonError('');
    }

    if (games.length === 0) {
      alert('Debes agregar al menos un juego antes de guardar el partido.');
      return;
    }

    setSaving(true);

    try {
      const matchData = {
        player1: selectedPlayer1,
        player2: selectedPlayer2,
        date: matchDateTime,
      };

      const matchResponse = await postSingleMatch(matchData);

      for (let i = 0; i < games.length; i++) {
        const gameData = {
          match: matchResponse.id,
          player1_score: games[i].player1Score,
          player2_score: games[i].player2Score,
        };
        await postSingleGame(gameData);
      }

      alert('Partido guardado con éxito.');
      setSelectedPlayer1(null);
      setSelectedPlayer2(null);
      setMatchDateTime('');
      setGames([{ player1Score: 0, player2Score: 0 }]);
    } catch (error) {
      console.error('Error saving match:', error);
      alert('Ocurrió un error al guardar el partido.');
    } finally {
      setSaving(false);
    }
  };

  return (
      <div>
        <AdminHeader/>
        <div
            className="min-h-screen flex flex-col items-center justify-center px-4 sm:px-6 lg:px-8"
            style={{background: backgroundGradient}}
        >
          <h2 className="text-2xl md:text-4xl font-bold mb-4 md:mb-8 text-center">
            Agregar Partido Individual
          </h2>
          <div
              className="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-8 mb-8">
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
          <MatchDateTimeInput matchDateTime={matchDateTime} setMatchDateTime={setMatchDateTime}/>
          <GamesManager
              games={games}
              handleGameScoreChange={handleGameScoreChange}
              addNewGame={addNewGame}
              removeGame={removeGame}
          />
          <div className="mt-4 md:mt-8">
            <Button className="w-full md:w-auto" onClick={handleSave} disabled={saving}>
              {saving ? 'Guardando...' : 'Guardar Partido'}
            </Button>
          </div>
        </div>
        <AdminFooter/>
      </div>

  );
}

export default SingleMatchAdd;
