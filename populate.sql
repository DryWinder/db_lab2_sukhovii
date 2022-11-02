INSERT INTO teams(team_name)
VALUES('Real Madrid'), ('Bayern Munchen'), 
('Liverpool'), ('Ajax'), 
('PSG'), ('Manchester United'), 
('RB Leipzig'), ('Barcelona'),
('Dynamo Kyiv'), ('Shakhtar Donetsk');

INSERT INTO players(player_name, player_position, team_id)
VALUES ('Karim Benzema', 'Forward', 1), ('Robert Lewandowski', 'Forward', 2),
('Sebastian Haller', 'Forward', 4), ('Christofer Nkunku', 'Midfielder', 7),
('Leroy Sane', 'Midfielder', 2), ('Mohamed Salah', 'Forward', 3),
('Cristiano Ronaldo', 'Forward', 6), ('Lionel Messi', 'Forward', 5),
('Kylian Mbappe', 'Forward', 5), ('Vinisius Jr.', 'Forward', 1);

INSERT INTO stats(player_id, matches_played, goals, assists, yellow_cards, red_cards)
VALUES (1, 12, 15, 1, 1, 0), (2, 10, 13, 1, 1, 0),
(3, 8, 11, 1, 1, 0), (4, 6, 7, 0, 0, 0),
(5, 10, 6, 6, 0, 0), (6, 13, 8, 2, 0, 0),
(7, 7, 6, 0, 1, 0), (8, 7, 5, 0, 1, 0),
(9, 8, 6, 4, 1, 0), (10, 13, 4, 6, 1, 0);
