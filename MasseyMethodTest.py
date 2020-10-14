import unittest
import numpy as np

import MasseyMethod

class MasseyMethodTest(unittest.TestCase):
    a = np.matrix([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
    [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
    [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
    [0, -1, 1, 0, 0]])

    at_a = np.matrix([[4, -1, -1, -1, -1], \
        [-1, 4, -1, -1, -1], [-1, -1, 4, -1, -1], \
        [-1, -1, -1, 4, -1], [1, 1, 1, 1, 1]])
        

    at_y = np.matrix([-40, 32, 15, 103, 0])

    y = np.matrix([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

    results = np.matrix([-8, 6.4, 3, 20.6, -22])
    
    rankings = ["J", "F", "G", "D", "M"]

    def test_methodLeftSide(self):
        actual_left_side = methodLeftSide(a)
        self.assertEquals(actual_left_side, at_a)

    def test_methodRightSide(self):
        actual_right_side = methodRightSide(a, y)
        self.assertEquals(actual_right_side, at_y)

    def test_solve(self):
        actual_result = solve(a, y)
        self.assertEquals(actual_result, results)

    def test_setRankings(self):
        actual_rankings = setRankings(solve(a, y))
        self.assertEqual(actual_rankings.keys(), rankings)