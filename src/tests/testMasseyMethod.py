import unittest
import numpy as np

import src.MasseyMethod

class testMasseyMethod(unittest.TestCase):


    def setUp(self):
        self.a = np.array([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
        [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
        [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
        [0, -1, 1, 0, 0]])

        self.at_a = np.array([[4, -1, -1, -1, -1], \
        [-1, 4, -1, -1, -1], [-1, -1, 4, -1, -1], \
        [-1, -1, -1, 4, -1], [1, 1, 1, 1, 1]])


        self.at_y = np.array([-40, 32, 15, 103, 0])

        self.y = np.array([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

        self.results = np.array([-8, 6.4, 3, 20.6, -22])

        self.rankings = {"J": 1,"F": 2, "G": 3, "D": 4, "M": 5}

        self.teams = {"D": 1, "F": 2, "G": 3, "J": 4, "M": 5}

        self.massey = src.MasseyMethod.MasseyMethod(self.a, self.y, self.teams)
    
    def testMethodLeftSide(self):

        actual_left_side = self.massey.method_left_side(self.a)
        self.assertEqual(actual_left_side.all(), self.at_a.all())

    def testMethodRightSide(self):

        actual_right_side = self.massey.method_right_side(self.a, self.y)
        self.assertEqual(actual_right_side.all(), self.at_y.all())

    def testSetRankings(self):

        actual_rankings = self.massey.set_rankings(self.teams, (self.massey.solve(self.massey.method_left_side(self.a), self.massey.method_right_side(self.a, self.y))))

        index1 = 0
        index2 = 0
        for team1 in actual_rankings.keys():
            index1 += 1
            for team2 in self.rankings.keys():
                index2 +=1 
                if(index1 == index2):
                    self.assertEqual(team1, team2)

    def testSolve(self):
        actual_result = self.massey.solve(self.massey.method_left_side(self.a), self.massey.method_right_side(self.a, self.y))
        self.assertEqual(actual_result.all(), self.results.all())

    def testRunMethod(self):
        final_rankings = self.massey.run_method()
        self.assertEqual(final_rankings, self.rankings)

    
