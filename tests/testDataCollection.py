import unittest
import tests.DataCollection
import numpy as np

class testDataCollection(unittest.TestCase):
	def setUp(self):
		self.short_csv = tests.DataCollection.DataCollection('data/mcb2019CSV-Less.csv', 200)
		self.whitepaper_data = tests.DataCollection.DataCollection('data/whitepaper-example.csv', 5)

		self.teams_dict = {'South Florida': 0, 'Alabama A&M': 1, 'Iowa St': 2, 'Alabama St': 3, 'Tulsa': 4, 'Alcorn St': 5, 
		'Appalachian St': 6, 'Mars Hill': 7, 'Austin Peay': 8, 'Oakland City': 9, 'Ball St': 10, 'Indiana St': 11, 
		'Cornell': 12, 'Binghamton': 13, 'Boston College': 14, 'WI Milwaukee': 15, 'Boston Univ': 16, 'Northeastern': 17, 
		'Bowling Green': 18, 'Tiffin': 19, 'Buffalo': 20, 'St Francis PA': 21, 'Campbell': 22, 'UNC Wilmington': 23, 
		'Missouri': 24, 'Cent Arkansas': 25, 'Central Conn': 26, 'Hartford': 27, 'Davidson': 28, 'Cleveland St': 29, 
		'NJIT': 30, 'Colgate': 31, 'W Michigan': 32, 'Detroit': 33, 'Texas': 34, 'E Illinois': 35, 'James Madison': 36, 
		'E Mennonite': 37, 'Syracuse': 38, 'E Washington': 39, 'Illinois St': 40, 'FL Gulf Coast': 41, 'VA Commonwealth': 42, 
		'Gardner Webb': 43, 'Penn': 44, 'George Mason': 45, 'Gonzaga': 46, 'Idaho St': 47, 'S Dakota St': 48, 
		'Grand Canyon': 49, 'Stony Brook': 50, 'G Washington': 51, 'Harvard': 52, 'MIT': 53, 'UC Irvine': 54, 'Idaho': 55, 
		'Notre Dame': 56, 'IL Chicago': 57, 'Texas Tech': 58, 'Incarnate Word': 59, 'MTSU': 60, 'Lees-McRae': 61, 'Lehigh': 62, 
		'Monmouth NJ': 63, 'Tennessee': 64, 'Lenoir Rhyne': 65, 'Massachusetts': 66, 'MA Lowell': 67, 'UAB': 68, 'Mercer': 69, 
		'Michigan': 70, 'Norfolk St': 71, 'NC State': 72, "Mt St Mary's": 73, 'New Mexico St': 74, 'N Dakota St': 75, 
		'New Hampshire': 76, 'Rivier': 77, 'Samford': 78, 'North Alabama': 79, 'North Carolina': 80, 'Wofford': 81, 
		'Oregon St': 82, 'UC Riverside': 83, 'UTEP': 84, 'Permian Basin': 85, 'Pittsburgh': 86, 'Youngstown St': 87, 'USC': 88, 
		'Robert Morris': 89, 'Seton Hall': 90, 'Wagner': 91, 'Virginia': 92, 'Towson': 93, 'UTRGV': 94, 'TX A&M Commerce': 95, 
		'Washington': 96, 'WKU': 97, 'WI Green Bay': 98, 'WI Lutheran': 99, 'Arizona St': 100, 'CS Fullerton': 101, 
		'San Diego St': 102, 'Ark Pine Bluff': 103, 'Rhode Island': 104, 'Bryant': 105, 'Wisconsin': 106, 'Coppin St': 107, 
		'Denver': 108, 'Maine': 109, 'Xavier': 110, 'IUPUI': 111, 'Utah St': 112, 'Montana St': 113, 'Villanova': 114, 
		'Morgan St': 115, 'San Francisco': 116, 'UC Davis': 117, 'South Carolina': 118, 'SC Upstate': 119, 'UCLA': 120, 
		'PFW': 121, 'Auburn': 122, 'South Alabama': 123, 'TX Southern': 124, 'Baylor': 125, 'Purdue': 126, 'Fairfield': 127, 
		'Georgetown': 128, 'MD E Shore': 129, 'Kansas': 130, 'Michigan St': 131, 'Louisiana Tech': 132, 'Wichita St': 133, 
		"St John's": 134, 'Loyola MD': 135, 'Marquette': 136, 'UMBC': 137, 'Memphis': 138, 'Tennessee Tech': 139, 'Minnesota': 140, 
		'NE Omaha': 141, 'New Orleans': 142, 'Spring Hill': 143, 'Pacific': 144, 'SIUE': 145, 'Providence': 146, 'Siena': 147, 
		'Rice': 148, 'St Leo': 149, 'UC Santa Barbara': 150, 'Wyoming': 151, 'Fresno St': 152, 'AK Anchorage': 153, 'Alabama': 154, 
		'Southern Univ': 155, 'Chattanooga': 156, 'Charlotte': 157, 'Col Charleston': 158, 'Presbyterian': 159, 
		'East Carolina': 160, 'Delaware St': 161, 'Duke': 162, 'Kentucky': 163, 'Sam Houston St': 164, 'E Texas Bap': 165, 
		'Temple': 166, 'La Salle': 167, 'Loyola-Chicago': 168, 'Missouri KC': 169, 'Old Dominion': 170, 'Navy': 171, 
		'UNC Greensboro': 172, 'NC A&T': 173, 'Stanford': 174, 'Seattle': 175, 'St Louis': 176, 'SE Missouri St': 177, 
		'VMI': 178, 'Washington MD': 179, 'New Mexico': 180, 'CS Northridge': 181, 'Georgia St': 182, 'ETSU': 183, 
		'Lipscomb': 184, 'Sewanee': 185, 'Akron': 186, 'Cedarville': 187, 'Longwood': 188, 'Randolph Col': 189, 
		'Oregon': 190, 'Portland St': 191, 'San Diego': 192, 'Weber St': 193, 'UT Arlington': 194, 'UT Tyler': 195, 
		'Army': 196, 'Marist': 197, 'Northwestern LA': 198, 'Centenary': 199}

		self.score_difference = np.array([17, 26, 17, 63, 61, 17, 11, 20, 3, 39, 15, 4, 13, 7, 20, 3, 13, 12, 28, 32, 8, 12, 1, 41, 5, 3, 
		12, 18, 17, 50, 22, 24, 45, 8, 8, 19, 50, 17, 54, 17, 11, 13, 27, 16, 21, 40, 31, 7, 18, 56, 8, 16, 34, 22, 13, 13, 
		30, 23, 34, 13, 25, 43, 3, 33, 15, 5, 13, 21, 25, 15, 28, 29, 9, 10, 16, 10, 28, 20, 11, 12, 25, 34, 21, 8, 31, 23, 
		8, 22, 10, 33, 3, 6, 44, 20, 28, 27, 17, 24, 4, 40])

		self.maxDiff = None

		self.wp_teams = {"D": 1, "F": 2, "G": 3, "J": 4, "M": 5}

		self.wp_games = np.array([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
        [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
        [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
        [0, -1, 1, 0, 0]])

		self.wp_y = np.array([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

	def test_team_content(self):		
		for team in self.teams_dict.keys():
			self.assertTrue(team in self.short_csv.get_teams().keys())

		for team in self.wp_teams.keys():
			self.assertTrue(team in self.whitepaper_data.get_teams().keys())

	def test_teams_length(self):
		self.assertEqual(len(self.teams_dict), self.short_csv.get_num_teams())
		self.assertEqual(len(self.wp_teams), self.whitepaper_data.get_num_teams())

	def test_difference_length(self):
		self.assertEqual(len(self.score_difference), len(self.short_csv.get_difference()))

	def test_difference_content(self):
		self.assertEqual(self.score_difference.all(), self.short_csv.get_difference().all())

		self.assertEqual(self.wp_y.all(), self.whitepaper_data.get_difference().all())

	def test_game_length(self):
		self.assertEqual(len(self.wp_games), len(self.whitepaper_data.get_games()))

	def test_game_content(self):
		self.assertEqual(self.wp_games.all(), self.whitepaper_data.get_games().all())
		iowa_vs_alabama = [0] * 200
		iowa_vs_alabama[self.teams_dict['Iowa St']] = 1
		iowa_vs_alabama[self.teams_dict['Alabama St']] = -1
		self.assertEqual(self.short_csv.get_games()[1].all(), np.array(iowa_vs_alabama).all())

		for game in self.short_csv.get_games():
			count_win = 0
			count_loss = 0
			for entry in game:
				if(entry == 1):
					count_win += 1
				elif(entry == -1):
					count_loss += 1
				else:
					self.assertEqual(entry, 0)

			self.assertTrue(count_win == 1)
			self.assertTrue(count_loss == 1)

		
