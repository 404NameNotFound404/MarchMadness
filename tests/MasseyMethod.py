import numpy as np
import collections

class MasseyMethod:

    a = 0
    y = 0
    teams = {}

    def __init__(self, left_side, right_side, t):
        self.a = left_side
        self.y = right_side
        self.teams = t

    def methodLeftSide(self, a):
        at = np.transpose(a)
        at_a = at.dot(a)
        at_a[len(at_a)-1:,] = 1
        return at_a

    def methodRightSide(self, a, y):
        at = np.transpose(a)
        at_y = np.squeeze(np.asarray(at)).dot(np.squeeze(np.asarray(y)))
        at_y[len(at_y)-1] = 0
        return at_y
    
    def solve(self, at_a, at_y):
        results = np.linalg.solve(at_a, at_y)
        return results
    
    def setRankings(self, teams, result):
        i = 0
        sorted_teams = {}
        for name in teams.keys():
            sorted_teams[name] = result[i]
            i += 1

        #print(sorted_teams)
        #sorted_dict = collections.OrderedDict(sorted_teams)
        #sorted_teams = sorted(sorted_teams.items(), key=lambda x: x[1], reverse=True)
        sorted_teams = {k: v for k, v in sorted(sorted_teams.items(), key=lambda item: item[1], reverse=True)}
        #print(sorted_teams)
        return sorted_teams

"""a = np.matrix([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
[-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
[1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
[0, -1, 1, 0, 0]])

at_a = np.matrix([[4, -1, -1, -1, -1], \
    [-1, 4, -1, -1, -1], [-1, -1, 4, -1, -1], \
    [-1, -1, -1, 4, -1], [1, 1, 1, 1, 1]])"""
        

"""at_y = np.matrix([-40, 32, 15, 103, 0])

y = np.matrix([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

results = np.matrix([-8, 6.4, 3, 20.6, -22])
    
rankings = ["J", "F", "G", "D", "M"]

teams = {"J": 1, "F": 2, "G": 3, "D": 4, "M": 5}

mas = MasseyMethod(a, y, teams)

print(mas.methodLeftSide(a))"""