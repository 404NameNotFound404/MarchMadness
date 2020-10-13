import csv
import pandas as pd
import numpy as np
from csv import reader
import re
# open file in read mode
teams = {}
count = 0
rows = 0

games = []
y = [] * 648

with open('/Users/katiemendel1/Desktop/MarchMadness/mcb2019CSV.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        assert(len(row) == 5)
        # row variable is a list that represents a row in csv
        g = [0] * 648
        differential = 0
        team_name = ''
        for x in [1, 3]:
            rows += 1
            differential = int(row[2])-int(row[4])
            #populate dictionary of team names
            team_name = re.sub('@', '', row[x])
            if team_name not in teams.keys():
                teams[team_name] = count
                count += 1
        if differential > 0:
            g[teams.get(team_name)] = -1
            g[teams.get(re.sub('@', '', row[1]))] = 1
            
        else:
            g[teams.get(team_name)] = 1
            g[teams.get(re.sub('@', '', row[1]))] = -1
            print(team_name)
            print(re.sub('@', '', row[1]))
        games.append(g)
        y.append(abs(differential))

#print(rows)
#print(len(teams.values()))
#print(y)
#print(games)

#print(games)

## MASSEY ###########################

a = np.matrix(games)
y = np.matrix(y)
at = np.transpose(a)
at_a = at.dot(a)
at_a[len(at_a)-1:,] = 1
at_y = np.squeeze(np.asarray(at)).dot(np.squeeze(np.asarray(y)))
at_y[len(at_y)-1] = 0
results = np.linalg.solve(at_a, at_y)

print(results)