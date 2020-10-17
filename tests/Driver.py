import numpy as np
import MasseyMethod
import DataCollection

data = DataCollection.DataCollection('/Users/katiemendel1/Desktop/MarchMadness/misc-files/mcb2019CSV.csv', 648)

massey = MasseyMethod.MasseyMethod(data.getGames(), data.getDifference(), data.getTeams())

counter = 0
for team in massey.runMethod():
    counter += 1
    print(str(counter) + ": " + str(team))
    
