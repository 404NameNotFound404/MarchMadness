import unittest
import numpy as np

import MasseyMethod

class MasseyMethodTest(unittest.TestCase):

    def testMethodLeftSide(self):
        a = np.array([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
        [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
        [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
        [0, -1, 1, 0, 0]])

        at_a = np.array([[4, -1, -1, -1, -1], \
        [-1, 4, -1, -1, -1], [-1, -1, 4, -1, -1], \
        [-1, -1, -1, 4, -1], [1, 1, 1, 1, 1]])
        

        at_y = np.array([-40, 32, 15, 103, 0])

        y = np.array([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

        results = np.array([-8, 6.4, 3, 20.6, -22])
    
        rankings = ["J", "F", "G", "D", "M"]

        teams = {"J": 1, "F": 2, "G": 3, "D": 4, "M": 5}

        mas = MasseyMethod.MasseyMethod(a, y, teams)

        actual_left_side = mas.methodLeftSide(a)
        self.assertEqual(actual_left_side.all(), at_a.all())

    def testMethodRightSide(self):
        a = np.array([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
        [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
        [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
        [0, -1, 1, 0, 0]])

        at_a = np.array([[4, -1, -1, -1, -1], \
        [-1, 4, -1, -1, -1], [-1, -1, 4, -1, -1], \
        [-1, -1, -1, 4, -1], [1, 1, 1, 1, 1]])
        

        at_y = np.array([-40, 32, 15, 103, 0])

        y = np.array([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

        results = np.array([-8, 6.4, 3, 20.6, -22])
    
        rankings = ["J", "F", "G", "D", "M"]

        teams = {"J": 1, "F": 2, "G": 3, "D": 4, "M": 5}
        mas = MasseyMethod.MasseyMethod(a, y, teams)
        actual_right_side = mas.methodRightSide(a, y)
        self.assertEqual(actual_right_side.all(), at_y.all())

    def testSetRankings(self):
        a = np.array([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
        [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
        [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
        [0, -1, 1, 0, 0]])

        y = np.array([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])
        
        rankings = ["J", "F", "G", "D", "M"]
        teams = {"J": 1,"F": 2, "G": 3, "D": 4, "M": 5}
        #teams = {1: "J", 2: "F", 3: "G", 4 : "D", 5: "M"}
        mas = MasseyMethod.MasseyMethod(a, y, teams)
        actual_rankings = mas.setRankings(teams, (mas.solve(mas.methodLeftSide(a), mas.methodRightSide(a, y))))
        print(actual_rankings)
        for i in range(len(actual_rankings)):
            self.assertEqual(actual_rankings[i][0], rankings[i])

    def testSolve(self):
        a = np.array([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
        [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
        [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
        [0, -1, 1, 0, 0]])

        at_a = np.array([[4, -1, -1, -1, -1], \
        [-1, 4, -1, -1, -1], [-1, -1, 4, -1, -1], \
        [-1, -1, -1, 4, -1], [1, 1, 1, 1, 1]])
        

        at_y = np.array([-40, 32, 15, 103, 0])

        y = np.array([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

        results = np.array([-8, 6.4, 3, 20.6, -22])

        teams = {"J": 1, "F": 2, "G": 3, "D": 4, "M": 5}
        mas = MasseyMethod.MasseyMethod(a, y, teams)
        actual_result = mas.solve(mas.methodLeftSide(a), mas.methodRightSide(a, y))
        self.assertEqual(actual_result.all(), results.all())
    
    