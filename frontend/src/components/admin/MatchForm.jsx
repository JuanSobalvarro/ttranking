import React, { useState, useEffect } from 'react';
import ColorThief from 'colorthief';
import { getPlayers, getCurrentSeason } from 'services/api.js';
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

const MatchForm = ({ matchType, postMatch, postGame }) => {
  const [players, setPlayers] = useState([]);
  const [selectedPlayers, setSelectedPlayers] = useState({});
  const [matchDateTime, setMatchDateTime] = useState('');
  const [season, setSeason] = useState([]);
  const [games, setGames] = useState([{ team1_score: 0, team2_score: 0 }]);
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
    }

    fetchSeason();
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

      const colors = await Promise.all(
        Object.values(selectedPlayers).map(playerId => getDominantColor(playerId))
      );

      for (let i = 0; i < 4; i++) {
            if (!colors[i]) colors[i] = defaultColor;
          }

      if (matchType === 'singles') {
        setBackgroundGradient(
          `linear-gradient(to right, rgba(${colors[0].join(',')}, 0.8), rgba(${colors[1].join(',')}, 0.8))`
        );
      } else {
        setBackgroundGradient(
          `linear-gradient(135deg, rgba(${colors[0].join(',')}, 1), rgba(${colors[0].join(',')}, 0) 70.71%),
           linear-gradient(45deg, rgba(${colors[1].join(',')}, 1), rgba(${colors[1].join(',')}, 0) 70.71%),
           linear-gradient(225deg, rgba(${colors[2].join(',')}, 1), rgba(${colors[2].join(',')}, 0) 70.71%),
           linear-gradient(315deg, rgba(${colors[3].join(',')}, 1), rgba(${colors[3].join(',')}, 0) 70.71%)`
        );
      }
    };

    updateGradient();
  }, [selectedPlayers, players, matchType]);

  const handleGameScoreChange = (gameIndex, team, change) => {
    setGames((prevGames) =>
      prevGames.map((game, index) =>
        index === gameIndex
          ? {
              ...game,
              [team]: Math.max(0, game[team] + change),
            }
          : game
      )
    );
  };

  const addNewGame = () => setGames([...games, { team1_score: 0, team2_score: 0 }]);
  const removeGame = (gameIndex) => setGames((prevGames) => prevGames.filter((_, index) => index !== gameIndex));

  const handleSave = async () => {
    const playerIds = Object.values(selectedPlayers);
    if (playerIds.some(id => !id)) {
      setAlert({
        isOpen: true,
        message: "Por favor, selecciona todos los jugadores.",
        type: "error",
      });
      return;
    }

    if (new Set(playerIds).size !== playerIds.length) {
      setAlert({
        isOpen: true,
        message: "Un jugador no puede estar en más de un equipo.",
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
        ...(matchType === 'singles' ? {
          player1: selectedPlayers.player1,
          player2: selectedPlayers.player2,
        } : {
          team1: [selectedPlayers.team1Player1, selectedPlayers.team1Player2],
          team2: [selectedPlayers.team2Player1, selectedPlayers.team2Player2],
        }),
        date: matchDateTime,
      };

      const matchResponse = await postMatch(matchData);

      for (let i = 0; i < games.length; i++) {
        const gameData = {
          match: matchResponse.id,
          ...(matchType === 'singles' ? {
            player1_score: games[i].team1_score,
            player2_score: games[i].team2_score,
          } : {
            team1_score: games[i].team1_score,
            team2_score: games[i].team2_score,
          }),
        };
        await postGame(gameData);
      }

      setAlert({
        isOpen: true,
        message: "Partido guardado con éxito.",
        type: "success",
      });
      setSelectedPlayers({});
      setMatchDateTime('');
      setGames([{ team1_score: 0, team2_score: 0 }]);
    } catch (error) {
      console.error('Error saving match:', error);
      setAlert({
        isOpen: true,
        message: "Ocurrió un error al guardar el partido.",
        type: "error",
      });
    } finally {
      setSaving(false);
    }
  };

  return (
    <div>
      <AlertModal
        isOpen={alert.isOpen}
        message={alert.message}
        type={alert.type}
        onClose={() => setAlert({ ...alert, isOpen: false })}
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
          Agregar Partido {matchType === 'singles' ? 'Individual' : 'de Dobles'}
        </h2>
          <div className="flex flex-col items-center">
            {matchType === 'singles' ? (
                <div className="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-8 mb-8">
                    <PlayerSelector
                        players={players}
                        selectedPlayer={selectedPlayers.player1}
                        setSelectedPlayer={(player) => setSelectedPlayers(prev => ({...prev, player1: player}))}
                        label="Seleccionar Jugador 1"
                    />
                    <div className="flex flex-row items-center justify-center">
                        <h3 className="text-2xl md:text-4xl font-bold">VS</h3>
                    </div>
                    <PlayerSelector
                        players={players}
                        selectedPlayer={selectedPlayers.player2}
                        setSelectedPlayer={(player) => setSelectedPlayers(prev => ({...prev, player2: player}))}
                        label="Seleccionar Jugador 2"
                    />
                </div>
            ) : (
                <>
                    <PlayerSelector
                        players={players}
                        selectedPlayer={selectedPlayers.team1Player1}
                        setSelectedPlayer={(player) => setSelectedPlayers(prev => ({ ...prev, team1Player1: player }))}
                        label="Seleccionar Jugador Equipo 1"
                    />
                    <PlayerSelector
                        players={players}
                        selectedPlayer={selectedPlayers.team1Player2}
                        setSelectedPlayer={(player) => setSelectedPlayers(prev => ({ ...prev, team1Player2: player }))}
                        label="Seleccionar Jugador Equipo 1"
                    />
                    <div className="flex flex-row items-center justify-center">
                        <h3 className="text-2xl md:text-4xl font-bold">VS</h3>
                    </div>
                    <PlayerSelector
                        players={players}
                        selectedPlayer={selectedPlayers.team2Player1}
                        setSelectedPlayer={(player) => setSelectedPlayers(prev => ({ ...prev, team2Player1: player }))}
                        label="Seleccionar Jugador Equipo 2"
                    />
                    <PlayerSelector
                        players={players}
                        selectedPlayer={selectedPlayers.team2Player2}
                        setSelectedPlayer={(player) => setSelectedPlayers(prev => ({ ...prev, team2Player2: player }))}
                        label="Seleccionar Jugador Equipo 2"
                    />
                </>
            )}
          </div>
            <div className="">
              <MatchDateTimeInput
                matchDateTime={matchDateTime}
                setMatchDateTime={setMatchDateTime}
              />
            </div>

        <GamesManager
          games={games}
          handleGameScoreChange={handleGameScoreChange}
          addNewGame={addNewGame}
          removeGame={removeGame}
        />

        <div className="flex justify-center mt-8">
          <Button
            disabled={saving}
            onClick={handleSave}
            className="bg-primary text-white hover:bg-primary-dark px-6 py-3 rounded-full"
          >
            {saving ? 'Guardando...' : 'Guardar Partido'}
          </Button>
        </div>
      </div>

      <AdminFooter />
    </div>
  );
};

export default MatchForm;
