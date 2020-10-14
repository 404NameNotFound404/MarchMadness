import csv
import pandas as pd
import numpy as np
from csv import reader
import re
# open file in read mode

class DataCollection:

    

    def __init__(self, file_path):
        count = 0
        rows = 0
        self.games = []
        self.teams = {}
        self.difference = [] * 648

        
        
        with open(file_path, 'r') as read_obj:
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
                    if team_name not in self.teams.keys():
                        self.teams[team_name] = count
                        count += 1
                if differential > 0:
                    g[self.teams.get(team_name)] = -1
                    g[self.teams.get(re.sub('@', '', row[1]))] = 1
                    
                else:
                    g[self.teams.get(team_name)] = 1
                    g[self.teams.get(re.sub('@', '', row[1]))] = -1
                    print(team_name)
                    print(re.sub('@', '', row[1]))
                self.games.append(g)
                self.difference.append(abs(differential))
