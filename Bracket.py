import random
from Team import *

def createMatchups():
    # generate objects from csv
    list = Team.generateArray()
    # clone the array and shuffle
    matchup = list.copy()
    random.shuffle(matchup)
    #Check for even/odd
    oddnumber = False
    if len(list) % 2 != 0:
        oddnumber = True
        extraTeam = matchup[-1]
        #print(extraTeam.name)
        matchup.pop(-1)
        list.remove(extraTeam)
        extraTeam.setTarget(Team("None/Bye", "N/A"))
    #Create Matchups
    for i in range(len(list)):
        for j in range(len(matchup)):
            if list[i].name != matchup[j].name:
                list[i].setTarget(matchup[j])
                matchup.pop(j)
                break
    #copy results to output list and add outlier team if necessary
    output = list.copy()
    if oddnumber:
        output.append(extraTeam)
    return output