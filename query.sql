SELECT player_name, (goals + assists) AS goals_and_assists FROM stats
JOIN players ON stats.player_id = players.player_id
ORDER BY goals_and_assists DESC;

SELECT player_position, COUNT(player_position) AS num_positions FROM players
GROUP BY player_position
ORDER BY num_positions DESC;

SELECT t1.team_name, SUM(t1.goals_and_assists) FROM (
SELECT teams.team_id, team_name, (goals + assists) AS goals_and_assists FROM teams
JOIN players ON teams.team_id = players.team_id
JOIN stats ON players.player_id = stats.player_id) AS t1
GROUP BY t1.team_name
ORDER BY SUM(goals_and_assists) DESC;