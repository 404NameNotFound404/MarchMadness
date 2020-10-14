import numpy as np

class MasseyMethod:

    a = np.matrix()
    y = np.matrix()
    teams = {}

    def MasseyMethod(self, left_side, right_side, t):
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
        for name in teams.values():
            teams[name] = result[i]
            i += 1

        sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
        return sorted_teams

