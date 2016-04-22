positiveWords = ['good','great','fun','happy','awesome','amazing',':)','(:',':D']
falsePositiveWords = ['the shit']
negativeWords = ['shit','fuck','terrible','bad','crap','bitch','garbage','bad','sucks','stinks','trouble',"can't connect","cannot connect",'dicks','dick',':(','):','D:']
falseNegativeWords = ['the shit']

def positiveStory(line):
    count = 0
    for word in positiveWords:
        if word in line:
            count+= 1
            break

    for word in falsePositiveWords:
        if word in line:
            count-= 1
            break
    
    return count

def negativeStory(line):
    count = 0
    for word in negativeWords:
        if word in line:
            count+= 1
            break

    for word in falseNegativeWords:
        if word in line:
            count-= 1
            break

    return count

csvArray = ["Activision1.csv", "Activision2.csv", "CallofDuty1.csv", "CallofDuty2.csv", "SkylandersGame1.csv", "SkylandersGame2.csv", "Blizzard_Ent1.csv", "Blizzard_Ent2.csv", "Warcraft1.csv", "Warcraft2.csv", "StarCraft1.csv", "StarCraft2.csv", "King_Games1.csv", "King_Games2.csv", "CandyCrushSaga1.csv", "CandyCrushSaga2.csv", "CandyCrushSoda1.csv", "CandyCrushSoda2.csv"]
Activision1 = open("Activision1.csv")
Activision2 = open("Activision2.csv")

for i in range(0, len(csvArray)):
    tweets = 0
    pos = 0
    neg = 0
    file = open(str(csvArray[i]))
    for line in file:
        tweets += 1
        pos += positiveStory(line)
        neg += negativeStory(line)
            
    print(str(csvArray[i]))
    print(tweets, ' tweets')
    print('     Positive Count: ' + str(pos))
    print('     Positive Percent: ' + str((pos/tweets) * 100))
    print('     Negative Count: ' + str(neg))
    print('     Negative Percent: ' + str((neg/tweets) * 100))
    print()

