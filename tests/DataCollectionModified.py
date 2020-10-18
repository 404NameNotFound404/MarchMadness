import csv
import numpy as np
from csv import reader
import re
# open file in read mode

class DataCollectionModified:

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

    numTeams : int
        The number of teams in the file



    Methods
    -------
    __init__(numTeams):
        Sets instance variables.

    readFile(file_path):
        Reads file of games and sets games, teams and difference variables.

    getters()
        There are getters for the instance variables.
    """
    
    #count = 0
    rows = 0
    games = []
    teams = {}
    difference = []
    numTeams = 0
    file = ''

    def __init__(self, file_name, num_teams):
        '''
        Constructor for DataCollection class

            Parameters:
                    numTeams (int): Number of unique teams from file
        '''
        self.games = []
        self.teams = {}
        self.difference = []
        self.numTeams = num_teams
        self.file = file_name

        self.readFile(file_name, num_teams)


    def readFile(self, file_path, numTeams):
        '''
        Read information from specified csv file and put information into corresponding instance variables.

            Parameters:
                    file_path (String): Location of csv file containing information on games played between teams to be ranked. Each game is stored
                        in a separate row contining date, team names and points for each team
        '''
        with open(file_path, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            count = 0
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                assert(len(row) == 5)
                # row variable is a list that represents a row in csv
                g = [0] * numTeams
                differential = 0
                team_name = ''
                for x in [1, 3]:
                    differential = int(row[2])-int(row[4])
                    #populate dictionary of team names
                    team_name = re.sub('@', '', row[x])
                    if team_name not in self.teams.keys():
                        self.teams[team_name] = count
                        count += 1
                
                #MODIFY HERE FOR HOME TEAM ADVANTAGE

                if differential > 0:
                    g[self.teams.get(team_name)] = -1
                    g[self.teams.get(re.sub('@', '', row[1]))] = 1
                    
                else:
                    g[self.teams.get(team_name)] = 1
                    g[self.teams.get(re.sub('@', '', row[1]))] = -1
                    #print(re.sub('@', '', row[1]))
                self.games.append(g)
                self.difference.append(abs(differential))
            
            self.games = np.array(self.games)
            self.difference = np.array(self.difference)


    def getTeams(self):
        '''
        Accessor method to get teams represented in the specified file along with index information in games array.

            Returns:
                    teams (dict): Dictionary containing each unique team name as key and index in games array as value.
        '''
        return self.teams

    def getDifference(self):
        '''
        Accessor method to get score differentials for each game.

            Returns:
                    difference (np.array): Array containing the score differential in each game.
        '''
        return self.difference

    def getGames(self):
        '''
        Accessor method to get game array representation for the input file.

            Returns:
                    games (np.array): Array containing win information for each game. Each row represents a game with 1 in the winning team column,
                        -1 in the losing team column and 0 in all other columns. 
        '''
        return self.games

    def getNumTeams(self):
        '''
        Accessor method to get number of teams.

            Returns:
                    numTeams (int): Number of unique teams in the input file.
        '''
        return self.numTeams



