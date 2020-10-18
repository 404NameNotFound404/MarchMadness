import numpy as np
import MasseyMethod
import DataCollection

class Driver:
    """
    A class to solve a system of equations using the Massey Method reading information from a file using DataCollection.

    ...

    Attributes
    ----------
    results : dict
        Ranked results with team name as key and ranking as value.

    Methods
    -------
    getResults():
        Calculates and returns rankings for data in specified file.
    """
    results = {}

    def __init__(self, file_name, num_teams):
        '''
        Constructor for Driver class

            Parameters:
                    file_name (String): file path to csv containing game information
                    num_teams (int): the number of unique team names contained in file at location file_name
        '''
        self.fileName = file_name
        data = DataCollection.DataCollection(file_name, num_teams)

        massey = MasseyMethod.MasseyMethod(data.getGames(), data.getDifference(), data.getTeams())

        counter = 0
        for team in massey.runMethod():
            counter += 1
            self.results[str(team)] = counter

    def getResults(self):
        '''
        Returns results of Massey method rankings

            Returns:
                    results (dict) : Calculates and returns rankings for data in specified file.
        '''
        return self.results
    


#full_file = Driver('/Users/katiemendel1/Desktop/MarchMadness/misc-files/mcb2019CSV.csv', 648)
#whitepaper = Driver('/Users/katiemendel1/Desktop/MarchMadness/misc-files/whitepaper-example.csv', 5)

#print(whitepaper.getResults())