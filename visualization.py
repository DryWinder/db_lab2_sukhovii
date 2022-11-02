import psycopg2
import matplotlib.pyplot as plt

username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

query_1 = '''
SELECT player_name, (goals + assists) AS goals_and_assists FROM stats
JOIN players ON stats.player_id = players.player_id
ORDER BY goals_and_assists DESC; 

'''

query_2 = '''
SELECT player_position, COUNT(player_position) AS num_positions FROM players
GROUP BY player_position
ORDER BY num_positions DESC;

'''

query_3 = '''
SELECT t1.team_name, SUM(t1.goals_and_assists) FROM (
SELECT teams.team_id, team_name, (goals + assists) AS goals_and_assists FROM teams
JOIN players ON teams.team_id = players.team_id
JOIN stats ON players.player_id = stats.player_id) AS t1
GROUP BY t1.team_name
ORDER BY SUM(goals_and_assists) DESC;

'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur1 = conn.cursor()
    cur1.execute(query_1)
    player_names = []
    goals_and_assists = []

    for row in cur1:
        player_names.append(row[0])
        goals_and_assists.append(row[1])


    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(11, 8))

    x_range = range(len( player_names))
    bar = bar_ax.bar(x_range, goals_and_assists, label='goals_and_assists', width=0.5)
    plt.title('Кількість зроблених гольових дій(голів + асистів) грацями')
    
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels( player_names, fontdict={'rotation': 75})
    bar_ax.set(xlabel='Гравці', ylabel='Голи та асисти')
    bar_ax.bar_label(bar)

    cur2 = conn.cursor()
    cur2.execute(query_2)
    player_positions = []
    player_positions_amount = []

    for row in cur2:
        player_positions.append(row[0])
        player_positions_amount.append(row[1])

    pie_ax.pie(player_positions_amount, labels=player_positions, autopct='%1.1f%%')
    pie_ax.set_title('Частка кількості позицій гравців на футбольному полі в даній БД')

    cur3 = conn.cursor()
    cur3.execute(query_3)
    team_names = []
    goals_and_assists_amount = []

    for row in cur3:
        team_names.append(row[0])
        goals_and_assists_amount.append(row[1])

    x_range = range(len(team_names))
    graph_ax.plot(x_range, goals_and_assists_amount, marker='o')
    graph_ax.set_xticks(x_range)
    graph_ax.set_xticklabels(team_names)
    graph_ax.set_title('Загальний обсяг гольових дій гравців кожної команди з даної БД')
    graph_ax.set(xlabel='Назва команди', ylabel='Голи та асисти')

    for x, y in zip(x_range, goals_and_assists_amount):
        label = "{:.2f}".format(y)
        graph_ax.annotate(label, (x, y), textcoords="offset points", xytext=(0, 4.5), ha='center')


figure.tight_layout()
plt.show()