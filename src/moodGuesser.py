def basicGuesser(currentMood: int):
    futureMood: int = 0
    if currentMood == 5:
        futureMood = 3
    else:
        futureMood = currentMood +1
    print(futureMood)
