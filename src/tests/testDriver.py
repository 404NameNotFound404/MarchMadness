import unittest
import numpy as np

import src.Driver

class testDriver(unittest.TestCase):


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

        self.whitepaper = src.Driver.Driver('tests/data/whitepaper-example.csv', 5)
    
    def test_getResultsLength(self):
        self.assertEqual(len(self.whitepaper.get_results().keys()), 5)

    def test_getResultsContent(self):
        self.assertEqual(self.whitepaper.get_results(), self.rankings)

    
