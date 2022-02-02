With respect to the first part of this project, our goals are:
1.	Create our own Database Schema from a reference figure given by the assignment using SQL Server Management Studio.
2.	Write a python program that splits tennis.csv file into 4 chunks of different csv files with their proper names: “match”, “player”, “tournament”, “date” and retrieving the feature "sex" from male_players.csv and female_players.csv. These two tasks had to be accomplished without using pandas library.
3.	Write a Python program that populates our database with the various tables from the .csv files, establishing schema relations as necessary.

With respect to the second part of this project, we explain how SSIS was used to solve some problems on the database previously created. Our goals are:
1. Show, for every country, the players ordered by number of matches won
2. For each year, list the player that participated in the most age mismatches. 
A match is said to be an “age mismatch” if the difference in years between the winner and the loser is more than 6.0.
3. Calculate for each player the total number of spectators that he performed in front of 

With respect to the third part of this project, we generated a datacube and MDX queries will be used to interrogate it.
1. Show the percentage increase in winner rank points with respect to the previous year for each winner
2. For each tournament show the total winner rank points in percentage with respect to the total winner rank points of the corresponding year of the tournament.
3. Show the winners having a total winner rank points greater than the average winner rank points in each continent by continent and year.
At the end of the part we created some dashboards using Microsoft Powerbi showing news about our data.
