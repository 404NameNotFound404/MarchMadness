import numpy as np
import src.MasseyMethod
import src.DataCollection
import src.DataCollectionHomeTeam


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
    get_results():
        Calculates and returns rankings for data in specified file.
    """
    results = {}

    def __init__(self, file_name_p, num_teams_p, home_team_p):
        '''
        Constructor for Driver class

            Parameters:
                    file_name (String): file path to csv containing game information

                    num_teams (int): the number of unique team names contained in file at location file_name

                    home_team_p (boolean): True if data should take into account home team advantage
        '''
        self.fileName = file_name_p

        # collect data from file
        data = src.DataCollection.DataCollection(file_name_p, num_teams_p, home_team_p)

        massey = src.MasseyMethod.MasseyMethod(data.get_games(), data.get_difference(), data.get_teams())

        counter = 0
        final_rankings = massey.run_method()

        for team in final_rankings:
            counter += 1
            self.results[str(team)] = counter

    def get_results(self):
        '''
        Returns results of Massey method rankings

            Returns:
                    results (dict) : Calculates and returns rankings for data in specified file.
        '''
        return self.results
    


#full_file = Driver('/Users/katiemendel1/Desktop/MarchMadness/tests/data/mcb2019CSV.csv', 648, True)
#whitepaper = Driver('/Users/katiemendel1/Desktop/MarchMadness/tests/data/whitepaper-example.csv', 5)

#print(full_file.get_results())