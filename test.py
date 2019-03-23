import time
from random import randint
import msvcrt as m
import datetime
def wait():
    m.getch()

global liveCount
liveCount = 3

def getElapsedTimeMinutes():
    global startTime
    
    currentTime = datetime.datetime.now()
    elapsedTime = datetime.datetime(1, 1, 1) + abs(startTime - currentTime)
    return elapsedTime.minute

def bossFight():
    global liveCount
    print(getElapsedTimeMinutes())
    print(liveCount)
    time.sleep(1)
    while True:
        print("""
        1. Shoot it right now!
        2. Run for safety!""")
        option = input("What do you want to do? >>")
        if option == "1":
            shootIt()
        elif option == "2":
            runForSafety()
        else:
            print("Invalid input. Try again.")
            continue

namePlayer = "Matt"    

def finalBossRoom():
    print("You arrive at the room. It's a red room with very sophisticated furnishings, red carpet, red drapes, and brown-red staircases on both sides, both leading to a landing.")
    wait()
    print("21: Aight, here we is... the final room. It shouldn't be too hard. Dis room's locked up in case of emergency.")
    wait()
    print(f"{namePlayer}: Emergency?")
    wait()
    print("21: Dere's a room at da top of that landing. We need to blow dat open too. Dere's a switch we gotta pull, it can either bring us back to dat train station you came from, or it can lead to a \"panic room\".")
    wait()
    print(f"{namePlayer}: Well, let's get going then, what are we waiting for?")
    wait()
    print("21: Well, da thing is...")
    wait()
    print("21: Dis s$*%'s too quiet, dawg.")
    wait()
    print(f"{namePlayer}: What? What do you mean, quiet? Is something going to happen?")
    wait()
    print("21: Maybe... ")
    wait()
    print("...")
    wait()
    print("Out of nowhere, the right wall starts cracking.")
    wait()
    print(f"{namePlayer}: W-what's that???")
    wait()
    print("A huge creature breaks out of the wall, and someone's riding on top of it!")
    wait()
    print("21: Oh no, it's her! I shoulda known that broad was gonna pop up!")
    wait()
    print(f"{namePlayer}: What? Who?")
    wait()
    print("21: She the general of these creatures! Her namePlayer's Crea-tur!")
    wait()
    print(f"{namePlayer}: Oh no, this can't be good at all.")
    wait()
    print("Crea-tur: Hey you, humans! What the hell are you still doing here!? Don'tcha know it's DANGEROUS to be intruders in a place like this?")
    wait()
    print("The creature takes a swipe at you both, and you run to the side.")
    wait()
    print("21: We finished stayin here, you $*@&(! We finna go back home to the human world!")
    wait()
    print("Crea-tur: Awww, but what are the other creatures gonna eat?")
    wait()
    print("The creature takes another swipe at you both, but you dodge it!")
    wait()
    print("21: I dunno! But this one you on gonna be eatin rockets! And not the candy!")
    wait()
    print("Crea-tur: Good! Because I'm pretty sure we can't have sugar! ")
    wait()
    print("21: (Hey, kid, we need to kill dis monsta! Do you got a plan?")
    wait()
    print(f"{namePlayer}: Yeah, uhhh...")
    wait()
    print("TIMER STARTS...")
    time.sleep(3)
    print("NOW!!")
    global startTime
    startTime = datetime.datetime.now()
    bossFight()

finalBossRoom()