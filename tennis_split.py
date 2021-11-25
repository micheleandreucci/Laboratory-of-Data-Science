import csv

match = open('match.csv', 'w', newline='')
tournament = open('tournament.csv', 'w', newline='')
date = open('date.csv', 'w', newline='')
player = open('player.csv', 'w', newline='')

files = [match, tournament, date, player]
cols = [
    ['tourney_id', 'tourney_date', 'match_num', 'winner_id', 'loser_id', 'score', 'best_of', 'round', 'minutes',
     'w_ace', 'w_df', 'w_svpt', 'w_1stIn', 'w_1stWon', 'w_2ndWon', 'w_SvGms', 'w_bpSaved', 'w_bpFaced', 'l_ace',
     'l_df', 'l_svpt', 'l_1stIn', 'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved', 'l_bpFaced', 'winner_rank',
     'winner_rank_points', 'loser_rank', 'loser_rank_points'],
    ['tourney_id', 'tourney_date', 'match_num', 'tourney_name', 'surface', 'draw_size', 'tourney_level',
     'tourney_spectators', 'tourney_revenue'],
    ['tourney_id', 'tourney_date', 'match_num'],
    ['winner_id', 'loser_id', 'winner_age', 'loser_age', 'tourney_date', 'winner_ioc', 'loser_ioc', 'winner_name',
     'loser_name', 'winner_hand', 'loser_hand', 'winner_ht', 'loser_ht']
]

for i in range(4):
    csv.writer(files[i]).writerow(col for col in cols[i])

# it splits the tennis csv file into 4 different files with the headers listed above
with open("tennis.csv", 'r') as tennis:
    reader = csv.DictReader(tennis, delimiter=',')
    for row in reader:
        for i in range(4):
            csv.writer(files[i]).writerow(row[col] for col in cols[i])

for j in range(4):
    files[j].close()
