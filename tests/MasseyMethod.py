import numpy as np
import collections

class MasseyMethod:
    """
    A class to solve a system of equations using the Massey Method.

    ...

    Attributes
    ----------
    a : np.array
        An array that contains a row for each game played with 1 in winning team column and -1 in losing team column
    y : np.array
        An array that contains a row for each game played with the absolute value of the score differential
    t : dict
        A dictionary containing the team names as keys and the index as value

    Methods
    -------
    method_left_side(a):
        Calculates and returns the left side matrix based on the Massey Method.

    method_right_side(a, y):
        Calculates and returns the right side matrix based on the Massey Method.

    solve(at_a, at_y):
        Calculates and returns the least squares solution to the system of equations.

    set_rankings(self, teams, result):
        Rank the results from solve.

    run_method():
        Calculates and returns rankings for preloaded data.
    """
    __slots__ = ['a', 'y', 'teams']
    

    def __init__(self, left_side_p, right_side_p, teams_p):
        '''
        Constructor for MasseyMethod class

            Parameters:
                    left_side (np.array): An array that contains a row for each game played with 1 in winning team column and -1 in losing team column
                    right_side (np.array): An array that contains a row for each game played with the absolute value of the score differential
                    t (dict): A dictionary containing the team names as keys and the index as value
        '''
        self.a = left_side_p
        self.y = right_side_p
        self.teams = teams_p

        """
        results = self.solve(self.methodLeftSide(self.a), self.methodRightSide(self.a, self.y))
        self.setRankings(self.teams, results)
        """

    def method_left_side(self, a_p):
        '''
        Calculates and returns the left side matrix based on the Massey Method.

            Parameters:
                    a (np.array): An array that contains a row for each game played with 1 in winning team column and -1 in losing team column

            Returns:
                    at_a (np.array): An array calculated based on steps in Massey Method
        '''
        at = np.transpose(a_p)
        at_a = at.dot(a_p)
        at_a[len(at_a)-1:,] = 1
        return at_a

    def method_right_side(self, a_p, y_p):
        '''
        Calculates and returns the right side matrix based on the Massey Method.

            Parameters:
                    a (np.array): An array that contains a row for each game played with 1 in winning team column and -1 in losing team column
                    y (np.array): An array that contains a row for each game played with the absolute value of the score differential

            Returns:
                    at_y (np.array): An array calculated based on steps in Massey Method
        '''
        at = np.transpose(a_p)
        at_y = np.squeeze(np.asarray(at)).dot(np.squeeze(np.asarray(y_p)))
        at_y[len(at_y)-1] = 0
        return at_y
    
    def solve(self, at_a_p, at_y_p):
        '''
        Calculates and returns the least squares solution to the system of equations.

            Parameters:
                    at_a (np.array): A square array calculated based on steps in Massey Method
                    at_y (np.array): An single dimensional array calculated based on steps in Massey Method

            Returns:
                    results (np.array): Least squares solution, r, to the equation at_a * r = at_y
        '''
        results = np.linalg.solve(at_a_p, at_y_p)
        return results
    
    def set_rankings(self, teams_p, result_p):
        '''
        Rank the results from solve.

            Parameters:
                    teams (dict): A dictionary containing the team names as keys and the index as value
                    result (np.array): An single dimensional array calculated as solution to the system of equations

            Returns:
                    sorted_teams (dict): A dictionary sorted by highest rank to lowest rank
        '''
        i = 0
        sorted_teams = {}
        for name in teams_p.keys():
            sorted_teams[name] = result_p[i]
            i += 1

        sorted_teams = {k: v for k, v in sorted(sorted_teams.items(), key=lambda item: item[1], reverse=True)}
        return sorted_teams

    def run_method(self):
        '''
        Run Massey Method end-to-end using the instance fields and return sorted dictionary

            Returns:
                    final_rankings (dict): A dictionary sorted by highest rank to lowest rank
        '''
        final_rankings = self.set_rankings(self.teams, self.solve(self.method_left_side(self.a), self.method_right_side(self.a, self.y)))

        count = 1
        for team in final_rankings.keys():
            final_rankings[team] = count
            count += 1
        
        return final_rankings

    
