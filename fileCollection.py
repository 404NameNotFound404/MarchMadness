import numpy
import requests
import re
from bs4 import BeautifulSoup


page = requests.get("https://www.masseyratings.com/scores.php?s=mlb2020")

soup = BeautifulSoup(page.content, 'lxml')
#print(soup.prettify())

table = soup.find("pre").text
print(table)

mid_array = table.split("\n")
final_array = []
for i in range(len(mid_array)):
    toAdd = []
    mid_array[i] = mid_array[i].split()
    for k in range(1, 5):
        try:
            toAdd.append(mid_array[i][k])
            #final_array.append(mid_array[i][k])
        except:
            #do nothing
            print()
    final_array.append(toAdd)

print(final_array)