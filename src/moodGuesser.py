import csv
from datetime import datetime
def basicGuesser(currentMood: int):
    futureMood: int = 0
    if currentMood == 5:
        futureMood = 3
    else:
        futureMood = currentMood +1
    print(futureMood)
def storeData(currentMood: int):
    now = datetime.now()
    entry = [now, currentMood]
    with open('../moodData.csv', 'a') as file_obj:
        writer_obj = csv.writer(file_obj)
        writer_obj.writerow(entry)
        file_obj.close()

    