import numpy as np
import MasseyMethod
import DataCollection

data = DataCollection(648)

data.readFile('../misc-files/mcb2019CSV.csv')

massey = MasseyMethod(data.getGames(), data.getDifference(), data.getTeams())

