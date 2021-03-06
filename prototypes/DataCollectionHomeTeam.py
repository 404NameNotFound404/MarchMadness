import csv
import numpy as np
from csv import reader
import re
# open file in read mode

class DataCollectionHomeTeam:

    """
    A class to load a file to be used by the MassyMethod class.

    ...

    Attributes
    ----------
    a : np.array
        An array that contains a row for each game played with 1 in winning team column and -1 in losing team column
    
    games : np.array
        An array with the teams and has information on what team won a game

    teams : np.array
        An array with the names of every team

    difference : np.array
        An array that has the difference in scores of every game

    num_teams : int
        The number of teams in the file



    Methods
    -------
    __init__(numTeams):
        Sets instance variables.

    read_file(file_path):
        Reads file of games and sets games, teams and difference variables.

    getters()
        There are getters for the instance variables.
    """
    
    #count = 0
    rows = 0
    games = []
    teams = {}
    difference = []
    num_teams = 0
    file = ''

    def __init__(self, file_name_p, num_teams_p):
        '''
        Constructor for DataCollection class

            Parameters:
                    numTeams (int): Number of unique teams from file
        '''
        self.games = []
        self.teams = {}
        self.difference = []
        self.num_teams = num_teams_p
        self.file = file_name_p

        self.read_file(file_name_p, num_teams_p)


    def read_file(self, file_path_p, num_teams_p):
        '''
        Read information from specified csv file and put information into corresponding instance variables.

            Parameters:
                    file_path (String): Location of csv file containing information on games played between teams to be ranked. Each game is stored
                        in a separate row contining date, team names and points for each team
        '''
        with open(file_path_p, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            count = 0
            # Iterate over each row in the csv using reader object
            countT = 0

            for row in csv_reader:
                assert(len(row) == 5)
                # row variable is a list that represents a row in csv
                g = [0] * num_teams_p
                differential = 0
                team_name = ''
                for x in [1, 3]:
                    differential = int(row[2])-int(row[4])
                    #populate dictionary of team names
                    team_name = re.sub('@', '', row[x])
                    if team_name not in self.teams.keys():
                        self.teams[team_name] = count
                        count += 1
                
                # modify for home team advantage

                if differential > 0 and '@' in row[3]:
                    #print("LOSS 1 - home team: " + team_name)
                    g[self.teams.get(team_name)] = -1
                    g[self.teams.get(re.sub('@', '', row[1]))] = 1
                    differential *= 1.2
                    
                    
                elif differential > 0 and '@' not in row[3]:
                    #print("WIN 1 - home team:" + team_name)
                    g[self.teams.get(team_name)] = -1
                    g[self.teams.get(re.sub('@', '', row[1]))] = 1
                
                elif differential < 0 and '@' in row[3]:
                    g[self.teams.get(team_name)] = 1
                    g[self.teams.get(re.sub('@', '', row[1]))] = -1

                elif differential < 0 and '@' not in row[3]:
                    g[self.teams.get(team_name)] = 1
                    g[self.teams.get(re.sub('@', '', row[1]))] = -1
                    differential *= 1.2

                else:
                    raise Exception("Invalid file format")
                    


                self.games.append(g)
                self.difference.append(abs(differential))

                """
                #MODIFY HERE FOR TEMPORALIZED
                

                for row in self.games:
                    if(np.array(g).nonzero()[0].all() != np.array(row).nonzero()[0].all()):
                        continue
                    else:
                        print(row)
                        row = g
                        #self.games = self.games[0:len(self.games),]
                """
            
            self.games = np.array(self.games)
            self.difference = np.array(self.difference)


    def get_teams(self):
        '''
        Accessor method to get teams represented in the specified file along with index information in games array.

            Returns:
                    teams (dict): Dictionary containing each unique team name as key and index in games array as value.
        '''
        return self.teams

    def get_difference(self):
        '''
        Accessor method to get score differentials for each game.

            Returns:
                    difference (np.array): Array containing the score differential in each game.
        '''
        return self.difference

    def get_games(self):
        '''
        Accessor method to get game array representation for the input file.

            Returns:
                    games (np.array): Array containing win information for each game. Each row represents a game with 1 in the winning team column,
                        -1 in the losing team column and 0 in all other columns. 
        '''
        return self.games

    def get_num_teams(self):
        '''
        Accessor method to get number of teams.

            Returns:
                    num_teams (int): Number of unique teams in the input file.
        '''
        return self.num_teams