CREATE TABLE teams(
	team_id SERIAL,
	team_name CHAR(25) NOT NULL,
    PRIMARY KEY(team_id)
);

CREATE TABLE players(
	player_id SERIAL,
	player_name CHAR(50) NOT NULL,
	player_position CHAR(15),
	team_id INT NOT NULL, 
    PRIMARY KEY (player_id),
	FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

CREATE TABLE stats(
	player_id INT NOT NULL,
	matches_played INT,
	goals INT,
	assists INT,
	yellow_cards INT,
	red_cards INT,
    PRIMARY KEY(player_id),
	FOREIGN KEY(player_id) REFERENCES players(player_id)
);