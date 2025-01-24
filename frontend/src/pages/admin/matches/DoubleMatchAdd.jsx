import React, { useState, useEffect } from 'react';
import ColorThief from 'colorthief';
import { getPlayers, postDoubleMatch, postDoubleGame } from 'services/api.js';
import PlayerSelector from 'components/admin/PlayerSelector.jsx';
import MatchDateTimeInput from 'components/admin/MatchDateTimeInput.jsx';
import GamesManager from 'components/admin/GamesManager.jsx';
import 'styles/tailwind.css';
import AdminFooter from 'components/admin/AdminFooter.jsx';
import AdminHeader from 'components/admin/AdminHeader.jsx';
import { Button } from 'flowbite-react';

function DoubleMatchAdd() {
  const [players, setPlayers] = useState([]);
  const [team1Player1, setTeam1Player1] = useState(null);
  const [team1Player2, setTeam1Player2] = useState(null);
  const [team2Player1, setTeam2Player1] = useState(null);
  const [team2Player2, setTeam2Player2] = useState(null);
  const [matchDateTime, setMatchDateTime] = useState('');
  const [games, setGames] = useState([{ team1Score: 0, team2Score: 0 }]);
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
      const defaultColor = [255, 255, 255];
      const getDominantColor = async (playerId) => {
        if (!playerId) return defaultColor;
        const player = players.find((p) => p.id === Number(playerId));
        if (!player?.photo) return defaultColor;

        const img = new Image();
        img.crossOrigin = 'anonymous';
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

      const colors = await Promise.all([
        getDominantColor(team1Player1),
        getDominantColor(team1Player2),
        getDominantColor(team2Player1),
        getDominantColor(team2Player2),
      ]);

      setBackgroundGradient(
          `
            linear-gradient(135deg, rgba(${colors[0].join(',')}, 1), rgba(${colors[0].join(',')}, 0) 70.71%),
            linear-gradient(45deg, rgba(${colors[1].join(',')}, 1), rgba(${colors[1].join(',')}, 0) 70.71%),
            linear-gradient(225deg, rgba(${colors[2].join(',')}, 1), rgba(${colors[2].join(',')}, 0) 70.71%),
            linear-gradient(315deg, rgba(${colors[3].join(',')}, 1), rgba(${colors[3].join(',')}, 0) 70.71%)
          `
        );

    };

    updateGradient();
  }, [team1Player1, team1Player2, team2Player1, team2Player2, players]);

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

  const addNewGame = () => setGames([...games, { team1Score: 0, team2Score: 0 }]);
  const removeGame = (gameIndex) => setGames((prevGames) => prevGames.filter((_, index) => index !== gameIndex));

  const handleSave = async () => {
    if (!team1Player1 || !team1Player2 || !team2Player1 || !team2Player2) {
      alert('Selecciona todos los jugadores antes de guardar el partido.');
      return;
    }

    if (new Set([team1Player1, team1Player2, team2Player1, team2Player2]).size !== 4) {
      alert('Un jugador no puede estar en más de un equipo.');
      return;
    }

    if (!matchDateTime) {
      alert('Selecciona una fecha y hora para el partido.');
      return;
    }

    if (games.length === 0) {
      alert('Debes agregar al menos un juego antes de guardar el partido.');
      return;
    }

    setSaving(true);

    try {
      const matchData = {
        team1: [team1Player1, team1Player2],
        team2: [team2Player1, team2Player2],
        date: matchDateTime,
      };

      const matchResponse = await postDoubleMatch(matchData);

      for (let i = 0; i < games.length; i++) {
        const gameData = {
          match: matchResponse.id,
          team1_score: games[i].team1Score,
          team2_score: games[i].team2Score,
        };
        await postDoubleGame(gameData);
      }

      alert('Partido guardado con éxito.');
      setTeam1Player1(null);
      setTeam1Player2(null);
      setTeam2Player1(null);
      setTeam2Player2(null);
      setMatchDateTime('');
      setGames([{ team1Score: 0, team2Score: 0 }]);
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
                  Agregar Partido de Dobles
              </h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-8 mb-8 items-center">
                  <div className="flex flex-col items-center">
                      <PlayerSelector
                          players={players}
                          selectedPlayer={team1Player1}
                          setSelectedPlayer={setTeam1Player1}
                          label="Jugador 1 del Equipo 1"
                      />
                      <PlayerSelector
                          players={players}
                          selectedPlayer={team1Player2}
                          setSelectedPlayer={setTeam1Player2}
                          label="Jugador 2 del Equipo 1"
                      />
                  </div>
                  <div className="flex items-center justify-center col-span-1">
                      <h3 className="text-2xl md:text-4xl font-bold">VS</h3>
                  </div>
                  <div className="flex flex-col items-center">
                      <PlayerSelector
                          players={players}
                          selectedPlayer={team2Player1}
                          setSelectedPlayer={setTeam2Player1}
                          label="Jugador 1 del Equipo 2"
                      />
                      <PlayerSelector
                          players={players}
                          selectedPlayer={team2Player2}
                          setSelectedPlayer={setTeam2Player2}
                          label="Jugador 2 del Equipo 2"
                      />
                  </div>
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

export default DoubleMatchAdd;
