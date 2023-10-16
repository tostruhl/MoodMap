import moodGuesser

def helloWorld():
    mood = int(input("Enter mood from 1-5:"))
    moodGuesser.basicGuesser(mood)
    moodGuesser.storeData(mood)
    moodGuesser.lessBasicGuesser()
if __name__ == "__main__":
    helloWorld()
