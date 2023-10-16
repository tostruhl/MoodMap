import csv
from datetime import datetime

#hard-coded guesser
def basicGuesser(currentMood: int):
    futureMood: int = 0
    if currentMood == 5:
        futureMood = 3
    else:
        futureMood = currentMood +1
    print(f"basicGuesser says you're predicted mood for tomorrow is: {futureMood}")

#uses data from csv to make a guess
def lessBasicGuesser():
    tomorrowMood: int = 0
    historicalMoods = getData()
    today = int(historicalMoods[-1][1])
    yesterday = int(historicalMoods[-2][1])

    if today == yesterday:
        tomorrowMood = today
    if today > yesterday:
        tomorrowMood = today + 1
    if today < yesterday:
        tomorrowMood = today - 1
    if tomorrowMood > 5:
        tommorowMood = 5
    if tomorrowMood < 1:
        tomorrowMood = 1
    
    print(f"LessBasicGuesser says you're predicted mood for tommorow is: {tomorrowMood}")



#returns nested array of all historical moodData
def getData():
    file = open('../moodData.csv')
    type(file)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    return rows

#takes current mood and adds it to database with time of entry
def storeData(currentMood: int):
    now = datetime.now()
    entry = [now, currentMood]
    with open('../moodData.csv', 'a') as file_obj:
        writer_obj = csv.writer(file_obj)
        writer_obj.writerow(entry)
        file_obj.close()

    