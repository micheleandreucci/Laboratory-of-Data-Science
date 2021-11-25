import pypyodbc as odbc
import pandas as pd
from django.db import IntegrityError
from django.shortcuts import render

server = 'tcp:lds.di.unipi.it'
driver = '{ODBC Driver 17 for SQL Server}'
database = 'Group_29_DB'
username = 'Group_29'
password = '4CCEZ8YA'


# it converts a list to a string
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


#
def connection_string(driver, server_name, database_name, username, password):
    connectionString = 'DRIVER=' + driver + \
                       ';SERVER=' + server + ';DATABASE=' + database + \
                       ';UID=' + username + ';PWD=' + password
    return connectionString


# it uses connect constructor to create a connection with the database
conn = odbc.connect(connection_string(driver, server, database, username, password))


# we populate  a table of the database
# we pass to the function a dataframe, a table to populate, a list of the dataframe header and its number of columns
def upload_db(df, table, columns, column_number):
    number = []
    for i in range(0, column_number):
        number.append('?,')
    number = listToString(number)
    number = number[:-1]
    # we iterate on the dataframe rows
    for i, row in df.iterrows():
        sql = "INSERT INTO " + table + "(" + columns + ")VALUES(" + number + ")"
        try:
            # we create a cursor via the connection
            cursor = conn.cursor()
            # it submits the SQL query
            cursor.execute(sql, tuple(row))
            conn.commit()  # it closes the connection
        except IntegrityError as e:
            return render(None, "template.html", {"message": e.message})


match = pd.read_csv('match.csv', sep=',')
del match['Unnamed: 0']
tournament = pd.read_csv('tournament.csv', sep=',')
del tournament['Unnamed: 0']
date = pd.read_csv('date.csv', sep=',')
del date['Unnamed: 0']
player = pd.read_csv("player.csv", sep=',')
del player['Unnamed: 0']
geo = pd.read_csv('geography.csv', sep=',')
del geo['Unnamed: 0']

match_column = []
player_column = []
date_column = []
tournament_column = []
geo_column = []
for col in tournament.columns:
    tournament_column.append("[" + col + "],")
for col in match.columns:
    match_column.append("[" + col + "],")
for col in player.columns:
    player_column.append("[" + col + "],")
for col in date.columns:
    date_column.append("[" + col + "],")
for col in geo.columns:
    geo_column.append("[" + col + "],")


# Applying the listToString function we convert the header name list into a string
# With the rstrip(date_column[-1]) we delete the last character corresponding to the comma placed at the end of the list
date_column = listToString(date_column)
date_column = date_column.rstrip(date_column[-1])
player_column = listToString(player_column)
player_column = player_column.rstrip(player_column[-1])
match_column = listToString(match_column)
match_column = match_column.rstrip(match_column[-1])
tournament_column = listToString(tournament_column)
tournament_column = tournament_column.rstrip(tournament_column[-1])
geo_column = listToString(geo_column)
geo_column = geo_column.rstrip(geo_column[-1])

# we get the number of columns of each dataframe
match_number = match.shape[1]
player_number = player.shape[1]
tournament_number = tournament.shape[1]
geo_number = geo.shape[1]
date_number = date.shape[1]

# The function upload_db is invoked to populate the tables in the database
upload_db(date, "[Group29HWMart].[Date]", date_column, date_number)
upload_db(tournament, "[Group29HWMart].[Tournament]", tournament_column, tournament_number)
upload_db(geo, "[Group29HWMart].[Geography]", geo_column, geo_number)
upload_db(player, "[Group29HWMart].[Player]", player_column, player_number)
upload_db(match, "[Group29HWMart].[Match]", match_column, match_number)
