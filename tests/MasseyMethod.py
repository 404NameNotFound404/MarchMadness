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
    methodLeftSide(a):
        Calculates and returns the left side matrix based on the Massey Method.

    methodRightSide(a, y):
        Calculates and returns the right side matrix based on the Massey Method.

    solve(at_a, at_y):
        Calculates and returns the least squares solution to the system of equations.

    setRankings(self, teams, result):
        Rank the results from solve.
    """
    __slots__ = ['a', 'y', 'teams']
    

    def __init__(self, left_side, right_side, t):
        '''
        Constructor for MasseyMethod class

            Parameters:
                    left_side (np.array): An array that contains a row for each game played with 1 in winning team column and -1 in losing team column
                    right_side (np.array): An array that contains a row for each game played with the absolute value of the score differential
                    t (dict): A dictionary containing the team names as keys and the index as value
        '''
        self.a = left_side
        self.y = right_side
        self.teams = t

        """
        results = self.solve(self.methodLeftSide(self.a), self.methodRightSide(self.a, self.y))
        self.setRankings(self.teams, results)
        """

    def methodLeftSide(self, a):
        '''
        Calculates and returns the left side matrix based on the Massey Method.

            Parameters:
                    a (np.array): An array that contains a row for each game played with 1 in winning team column and -1 in losing team column

            Returns:
                    at_a (np.array): An array calculated based on steps in Massey Method
        '''
        at = np.transpose(a)
        at_a = at.dot(a)
        at_a[len(at_a)-1:,] = 1
        return at_a

    def methodRightSide(self, a, y):
        '''
        Calculates and returns the right side matrix based on the Massey Method.

            Parameters:
                    a (np.array): An array that contains a row for each game played with 1 in winning team column and -1 in losing team column
                    y (np.array): An array that contains a row for each game played with the absolute value of the score differential

            Returns:
                    at_y (np.array): An array calculated based on steps in Massey Method
        '''
        at = np.transpose(a)
        at_y = np.squeeze(np.asarray(at)).dot(np.squeeze(np.asarray(y)))
        at_y[len(at_y)-1] = 0
        return at_y
    
    def solve(self, at_a, at_y):
        '''
        Calculates and returns the least squares solution to the system of equations.

            Parameters:
                    at_a (np.array): A square array calculated based on steps in Massey Method
                    at_y (np.array): An single dimensional array calculated based on steps in Massey Method

            Returns:
                    results (np.array): Least squares solution, r, to the equation at_a * r = at_y
        '''
        results = np.linalg.solve(at_a, at_y)
        return results
    
    def setRankings(self, teams, result):
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
        for name in teams.keys():
            sorted_teams[name] = result[i]
            i += 1

        sorted_teams = {k: v for k, v in sorted(sorted_teams.items(), key=lambda item: item[1], reverse=True)}
        return sorted_teams

    def runMethod(self):
        return self.setRankings(self.teams, self.solve(self.methodLeftSide(self.a), self.methodRightSide(self.a, self.y)))

    
