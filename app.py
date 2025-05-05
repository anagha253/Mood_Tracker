from datetime import date
import json

Mood_Map = {1: "Happy", 2:"Sad", 3:"Emotional",4:"Stressed"}


def getDate():
    return date.today().strftime("%Y-%m-%d")

def setMood(today,mood):

    data = {}
    data[today] = {"mood":Mood_Map[int(mood)]}
    addToLog(data)

    
def addToLog(data):
    with open("mood_log.json","w") as file:
        json.dump(data,file,indent=4)


def viewMoods():
    with open("mood_log.json","r") as file:
        data = json.load(file)
    if not data:
                print("No mood records found.")
                return

    print("\nYour Mood Log:")
    for date, entry in data.items():
        print(f"{date} - Mood: {entry['mood']}")



if __name__ == "__main__":
    #login (opt)

    #date should be mentioned prompt enter your mood => give choices
    today = getDate()
    print(today)
    mood = input("Enter your mood:\n 1)Happy\n 2)Sad\n 3)Emotional\n 4)Stressed\n")
    setMood(today,mood)

    #the mood on the day is added to the calender 
    viewMoods()

