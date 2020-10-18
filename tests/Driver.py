import numpy as np
import MasseyMethod
import DataCollection

class Driver:

    results = {}
    fileName = ""

    def __init__(self, file_name, num_teams):
        self.fileName = file_name
        data = DataCollection.DataCollection(file_name, num_teams)

        massey = MasseyMethod.MasseyMethod(data.getGames(), data.getDifference(), data.getTeams())

        counter = 0
        for team in massey.runMethod():
            counter += 1
            self.results[str(team)] = counter

    def getResults(self):
        return self.results

    def getFileName(self):
        return self.fileName
    


#full_file = Driver('/Users/katiemendel1/Desktop/MarchMadness/misc-files/mcb2019CSV.csv', 648)
#whitepaper = Driver('/Users/katiemendel1/Desktop/MarchMadness/misc-files/whitepaper-example.csv', 5)

#print(whitepaper.getResults())