# Table Tennis Ranking Management System (TTRanking)

This project is part of the greater Sports Game Database (SGD) system. It is designed to manage table tennis rankings, match tracking, player management, and data integrity for tournaments and competitions.

## Features

- **Player Management**: Create, update, and manage player profiles with details such as name, alias, gender, nationality, and more.
- **Match Management**: Track singles and doubles matches, including player scores, match results, and ranking updates.
- **Ranking System**: Automatically updates player rankings based on match results.
- **Winrate Tracking**: Calculates and displays player winrates based on their match history.
- **Spotlight Section**: Displays the top 5 most efficient players on the homepage.
- **Data Integrity Checks**: Ensure consistency of player rankings and match counts through custom Django management commands.
- **Automated Database Backups**: Regularly backs up the database and verifies the integrity of the backups.

## Models

### Player

- **Fields**:
  - `first_name`: First name of the player.
  - `last_name`: Last name of the player.
  - `alias`: Player's alias (optional).
  - `gender`: Gender of the player (Male/Female).
  - `date_of_birth`: Date of birth of the player (optional).
  - `nationality`: Nationality of the player.
  - `ranking`: Player's current ranking points.
  - `matches_played`: Number of matches the player has played.
  - `photo`: Player's profile picture (auto-resized to 600x600 pixels).
  - `created_at`: Timestamp of when the player profile was created.
  - `updated_at`: Timestamp of when the player profile was last updated.

- **Properties**:
  - `age`: Calculates the player's age based on their date of birth.
  - `victories`: Calculates the number of victories based on the player's ranking.
  - `winrate`: Calculates the player's winrate as a percentage.

- **Methods**:
  - `add_points(points)`: Adds ranking points to the player.
  - `remove_points(points)`: Removes ranking points from the player.

### SinglesMatch

- **Fields**:
  - `date`: Date and time of the match.
  - `player1`: The first player in the match.
  - `player2`: The second player in the match.
  - `player1_score`: Score of the first player.
  - `player2_score`: Score of the second player.
  - `winner`: The player who won the match (auto-calculated).

- **Properties**:
  - `players`: Returns a list of players in the match.
  - `score`: Returns the match score as a string (e.g., "11 - 9").
  - `winner_display`: Returns a string indicating the winner of the match.

- **Methods**:
  - `update_winner()`: Determines and updates the winner of the match.
  - `update_player_points()`: Updates ranking points for the winner and loser.
  - `update_matches_played()`: Increments the match count for both players.

### DoublesMatch

- **Fields**:
  - `date`: Date and time of the match.
  - `team1_player1`: The first player of the first team.
  - `team1_player2`: The second player of the first team.
  - `team2_player1`: The first player of the second team.
  - `team2_player2`: The second player of the second team.
  - `team1_score`: Score of the first team.
  - `team2_score`: Score of the second team.
  - `winner_team`: The winning team (auto-calculated).

- **Properties**:
  - `players`: Returns a list of all players in the match.
  - `score`: Returns the match score as a string (e.g., "11 - 9").
  - `winner_display`: Returns a string indicating the winning team.

- **Methods**:
  - `update_winner()`: Determines and updates the winning team.
  - `update_team_points()`: Updates ranking points for the winning and losing teams.
  - `update_matches_played()`: Increments the match count for all players.

## Management Commands

### `checkintegrity`

- **Purpose**: Checks and ensures the integrity of player data.
- **Usage**:
  - `python manage.py checkintegrity --ranking`: Checks and updates player rankings.
  - `python manage.py checkintegrity --matchcount`: Updates match counts for each player.

### `backupdb.py`

- **Purpose**: Creates a backup of the MySQL database.
- **Configuration**:
  - `DB_HOST`: Database host.
  - `DB_USER`: Database username.
  - `DB_PASSWORD`: Database password.
  - `DB_NAME`: Database name.
  - `BACKUP_DIR`: Directory where backups will be stored.

- **Usage**:
  - Run the script to create a backup: `python backupdb.py`

### `checkbackup.py`

- **Purpose**: Checks the latest backup file for integrity.
- **Configuration**:
  - `BACKUP_DIR`: Directory where backups are stored.
  - `DB_NAME`: Database name.

- **Usage**:
  - Run the script to check the latest backup: `python checkbackup.py`

## Deployment

The system is deployed on an Oracle Linux VM. Ensure all necessary dependencies are installed and that the MySQL database is properly configured.

## Future Enhancements

- Adding more detailed player statistics.
- Expanding the spotlight section to include different categories.
- Enhancing the data integrity checks with additional verification steps.
