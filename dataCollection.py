import csv
import pandas as pd
import numpy as np
from csv import reader
import re
# open file in read mode
teams = {}
count = 0
rows = 0
#games = [row, team1, team2, scoredifference]
games: {}
with open('/Users/katiemendel1/Desktop/MarchMadness/mcb2019CSV.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        assert(len(row) == 5)
        # row variable is a list that represents a row in csv
        for x in [1, 3]:
            rows += 1
            #populate dictionary of team names
            team_name = re.sub('@', '', row[x])
            if team_name not in teams.keys():
                teams[team_name] = count
                count += 1
        

print(rows)
print(len(teams.values()))

#print(games)