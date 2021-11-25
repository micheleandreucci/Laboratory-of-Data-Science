import csv
from csv import reader

male_players = []
female_players = []

with open('male_players.csv', mode='r') as read_obj:
    csv_reader = reader(read_obj)
    male_players = list(csv_reader)
with open('female_players.csv', mode='r') as read_obj1:
    csv_reader1 = reader(read_obj1)
    female_players = list(csv_reader1)

female_players = ["{} {}".format(i[0], i[1]) for i in female_players]
male_players = ["{} {}".format(i[0], i[1]) for i in male_players]

inf = open('Giocatori.csv', 'r', newline='')
out = open('player.csv', 'w', newline='')
reader = csv.DictReader(inf)
fieldnames = ['Sex'] + reader.fieldnames  # Add column name to beginning.
writer = csv.DictWriter(out, fieldnames)
writer.writeheader()

# it creates a new file and adds a columns with the information about the player sex
for row in reader:
    if row['name'] in female_players:
        writer.writerow(dict(row, Sex='Femmina'))
    elif row['name'] in male_players:
        writer.writerow(dict(row, Sex='Maschio'))
    else:
        writer.writerow(dict(row, Sex='Sconosciuto'))
