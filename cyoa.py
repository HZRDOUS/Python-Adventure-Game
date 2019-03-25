import time
from random import randint
import msvcrt as m
import datetime
import random

global namePlayer
namePlayer = ""
global inventory
inventory = [ ]
global plantCount
plantCount = 0

def wait():
    m.getch()

def printOutInventory():
    global inventory
    print("You have the following things in your inventory:")
    for item in inventory:
        print(f'- {item}')
    print("-" * 30 + "\n")

# inventory.append("Porscuitto")

def gameComplete():
    print("Congrats! You completed the game! Would you like to quit, or try again?")
    while True:
        print("""
        1. Replay
        2. Quit""")
        tryAgain = input("Try again?? >> ")
        if tryAgain == "1":
            intro()
        elif tryAgain == "2":
            print("Thank you for playing!")
            exit()
        else:
            print("Bad input!")
            wait()
            continue

def outOfLives():
    print("You ran out of lives.")
    while True:
        print("""
        1. Replay
        2. Quit""")
        tryAgain = input("Try again?? >> ")
        if tryAgain == "1":
            intro()
        elif tryAgain == "2":
            exit()
        else:
            print("Bad input!")
            wait()
            continue

def deathAftermath():
    while True:
        print("""
        1. Replay
        2. Quit""")
        tryAgain = input("Try again?? >> ")
        if tryAgain == "1":
            intro()
        elif tryAgain == "2":
            exit()
        else:
            print("Bad input!")
            wait()
            continue

def pokeCreature():
    global inventory
    print("You poke the creature in the eyes as it lunges towards you...")
    wait()
    inventory.remove("Key")
    print("The monster stops. You blinded it, and it's now wandering around. ")
    print("Congrats! You can go home now. What do you want to do?")
    while True:
        print("""
        1. Go through the portal
        2. Go back to the foyer... it's too easy.""")
        option = input("What do you want to do?? >> ")
        if option == "1":
            print("You hop through the portal...")
            wait()
            print("You successfully arrive back at the train station you came from.")
            wait()
            gameComplete()
        elif option == "2":
            print("...")
            wait()
            print("Are you serious??? ")
            wait()
            print("You want to go back??")
            wait()
            print("""
            1. Yes
            2. No""")
            goBack = input("Really?? >> ")
            if goBack == "1":
                wait()
                print("Wow... well, alright, then.")
                wait()
                print("You go back to where you started... for some reason...")
                wait()
                global triedUnlocking
                triedUnlocking = True
                wait()
                castleOptions()
            else:
                print("Invalid input. Try again.")
                wait()
                continue
        else:
            print("Invalid input. Try again.")
            wait()
            continue

def roomDeath():
    print("You should probably know from your instincts these guys don't take well to reasoning.")
    wait()
    print("Aaand you're dead!")
    wait()
    deathAftermath()

def unlockedRoom():
    print("You enter the unlocked room... but you're greeted to a big surprise!")
    global flag
    flag = True
    wait()
    print("A portal that says... back to your home town! Just your luck!")
    wait()
    print("Oh yeah, did I mention that there's a bloodthirsty monster guarding that portal!")
    wait()
    print("What are you going to do?")
    while True:
        print("""
        1. Try talking some sense into it, Dr. Phil style.
        2. Poke it in the eye with the key""")
        option = input("What do you want to do?? >> ")
        if option == "1":
            roomDeath()
        elif option == "2":
            pokeCreature()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option.")
            wait()
            continue
        
def rightAfterCafeteria():
    global flag
    print("You continue going left, and you approach a door.")
    print("You try opening it- but it's locked. What do you wanna do?")
    while True:
        if "Key" in inventory:
            while True:
                print("""
                1. Go back the way you came.
                2. Use your key to unlock the door""")
                option = input("What do you want to do? >> ")
                if option == "1":
                    print("You give up and walk back to square one.")
                    flag = True
                    castleOptions()
                elif option == "2":
                    print("You use your key to try and unlock it...")
                    wait()
                    print("Voila! It works!")
                    unlockedRoom()
                elif option == "44":
                    printOutInventory()
                    wait()
                    continue
                else: 
                    print("Invalid option. Try again")
                    wait()
                    continue
        else:
            while True:
                print("""
                1. Go back to the way you came.
                2. Use your key to unlock the door.""")
                option = input("What do you want to do?? >> ")
                if option == "1":
                    print("You give up and walk back to square one.")
                    flag = True
                    wait()
                    castleOptions()
                elif option == "2":
                    print("You don't have a key to unlock it.")
                    wait()
                    continue
                elif option == "44":
                    printOutInventory()
                    wait()
                    continue
                else:
                    print("Invalid input. Try again.")
                    wait()
                    continue



def sneakyBeakyLike():
    global inventory
    print("You sneak around the corners of the cafeteria.")
    print("The creatures are far too distracted to notice you.")
    wait()
    print("You snoop around and go to the shiny object... aha! You got it.")
    wait()
    print("It's a key!")
    inventory.append("Key")
    wait()
    print("The key has been added to your inventory.")
    print("(Handy tip: You can look at your inventory by entering \"44\" at any decision moment.)")
    wait()
    print("You slowly make your way back to the entrance. You're now back where you started.")
    wait()
    rightAfterCafeteria()

def nonchalantCafe():
    print("You enter the cafe like you won't die...")
    wait()
    print("But you do.")
    print("These creatures don't take kindly to intruders!")
    wait()
    deathAftermath()

def cafeteriaOptions():
    while True:
        print("""
        Do you want to either:
        1. Go in nonchalantly?
        2. Go in sneaky-beaky like""")
        option = input("What do you want to do? >> ")
        if option == "1":
            nonchalantCafe()
        elif option == "2":
            sneakyBeakyLike()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Wrong input. Try again.")
            wait()
            continue

def rightEdge():
    print("You decide to sneak on the right.")
    wait()
    print("You come across a door. You look inside.")
    print("The creatures are having lunch in the cafeteria... it's basically a riot in there!")
    print("However, in the midst of the riot, you see a shimmer of a certain object...")
    print("You aren't sure if it's worth it to go in there.")
    wait()
    print("Do you want to try and enter?")
    wait()
    rightEdgeOptions()

def rightEdgeOptions():
    while True:
        print("""
        1. Go in
        2. Continue on""")
        option = input("What do you want to do?? >> ")
        if option == "1":
            cafeteriaOptions()
        elif option == "2":
            rightAfterCafeteria()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Wrong input, try again")
            continue

def coffee():
    print("You try some coffee on the desk...")
    wait()
    print("You don't like it, so you spit it out.")
    wait()
    print("""
    1. Clean it up
    2. Just leave it""")
    cleanUp = input("Clean up your mess? >> ")
    while True:
        if cleanUp == "1":
            print("You clean up the mess. ")
            wait()
            print("A janitor creature approaches you.")
            wait()
            print("Janitor: Thanks for cleaning up that mess. I hate when people leave messes like that and don't clean it up!")
            wait()
            breakRoom()
        elif cleanUp == "2":
            print("You leave it there like a slob.")
            wait()
            print("A janitor creature approaches you. ")
            wait()
            print("Janitor: HEY! YOU DIDN'T CLEAN UP YOUR MESS! COME HERE!")
            wait()
            print("You try to outrun him, but you can't run faster than him.")
            wait()
            print("He eats you, and you die!")
            wait()
            deathAftermath()
        elif cleanUp == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option. Try again.")

def searchDesk():
    global inventory
    print("You look through the desk...")
    wait()
    print("You find a pack of porscuittoo.")
    wait()
    print("\"Porscuitto\" has been added to your inventory.")
    inventory.append("Porscuitto")
    wait()
    secondFloorDoor1Options()

def inspectBookshelf():
    print("There's a book about cooking with porscuitto in here...")
    wait()
    print("21: Dem little s&#ts love that stuff... I dunno why...")
    wait()
    print("Language!")
    wait()
    secondFloorDoor1Options()

def secondFloorDoor1():
    print("It's a library like room...")
    wait()
    secondFloorDoor1Options()

def secondFloorDoor1Options():
    while True:
        print("""
        1. Inspect bookshelf
        2. Search desk
        3. Leave""")
        option = input("What would you like to do? >> ")
        if option == "1":
            inspectBookshelf()
        elif option == "2":
            searchDesk()
        elif option == "3":
            print("You decide to leave the room.")
            wait()
            secondFloorOptions()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid input. Try again.")
            wait()
            continue

def admirePaintings():
    print("It's a painting of of a cow, crudely drawn too.")
    wait()
    print("21: Yeah, these dudes have no idea what true art is.")
    wait()
    print(f"{namePlayer}: Yeah, I can see. The black and white spots are mixed up. ")
    wait()
    print("21: They tried bringing a chocolate cow over here to get chocolate milk once. ")
    wait()
    print(f"{namePlayer}: That must have been disappointing for them.")
    wait()
    print("21: You could imagine how I feel, I wanted some chocolate milk myself.")
    wait()
    print(f"{namePlayer}: ...")
    wait()
    secondFloorDoor2Options()

def admireStatue():
    print("It's a poorly-made statue of David, but with a creature head on it.")
    wait()
    print("You think to yourself, you did not need to look closer at that today...")
    wait()
    secondFloorDoor2Options()

def secondFloorDoor2():
    print("A second room... very artsy.")
    wait()
    secondFloorDoor2Options()

def secondFloorDoor2Options():
    while True:
        print("""
        1. Admire paintings
        2. Admire statue
        3. Leave""")
        option = input("What would you like to do? >> ")
        if option == "1":
            admirePaintings()
        elif option == "2":
            admireStatue()
        elif option == "3":
            secondFloorOptions()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid input. Try again.")
            wait()
            continue

def secondFloor():
    print("You arrived at the second floor, and are greeted with three doors.")
    wait()
    print("21: The hospital should be somewhere in deez three doors. Let's go explorin'.")
    wait()
    secondFloorOptions()

def hopsital():
    print("You enter the hospital... it's a waiting room and you see a bunch of sick creatures ")
    wait()
    print("21: Stupid thangs ain't cook they meat properly.")
    wait()
    print(f"{namePlayer}: Can't say I'm too surprised...")
    wait()
    print("21: Bull#$*^ aside, the room the rocket launcher is hidden in is somewhere in room 199. Let's head there.")
    wait()
    hospitalOptions()

def inspectPlant():
    global plantCount
    plantCount += 1
    if plantCount < 2:
        print("You touch the plant. Neat plant- it's fake though.")
        wait()
        hospitalOptions()
    else:
        print("You touch the pla-")
        time.sleep(0.5)
        print("Security Guard: Hey! You! You'll regret touching that plant with your filthy hands!")
        wait()
        print("Before you can think, he hits you over the head with a baton...")
        wait()
        print("You're dead. They don't play about their plants.")
        wait()
        deathAftermath()

def securityGuard():
    global inventory
    print("You talk to the security guard.")
    wait()
    print("Secuirty Guard: Ach! Humans! We have enough sickness here, get out!")
    wait()
    print("21: Why the hell are you talkin to this guy? He gonna kill us!")
    wait()
    print("Security Guard: Nah. We don't like police brutality here. We leave the killing up to the random monsters, like the janitors.")
    wait()
    print(f"{namePlayer}: Odd. More civilized than actual human beings.")
    if "Porscuitto" in inventory:
        wait()
        securityGuardOptions()
    else:
        wait()
        hospitalOptions()

def bribe():
    print("You give the security guard the porscuitto.")
    wait()
    print(f"{namePlayer}: How about you do us a favor for this?")
    wait()
    print("His ears perk up.")
    wait()
    print("Security Guard: Oh. For that? ")
    wait()
    print("Security Guard: I don't know... I can't take that stuff from h-")
    wait()
    print("Security Guard: You know what? Sure. Why not. Gimmegimmegimme.")
    wait()
    print("21: No, not yet. You gonna get us outta here.")
    wait()
    print("Security Guard: But- bu-")
    wait()
    print("21: No buts, monsta. You don't get dis meat if you don't help us.")
    wait()
    print("...")
    wait()
    print("Security Guard: Fine... follow me.")
    wait()
    print("The security guard brings you to the hospital's supply closet.")
    wait()
    print("Security Guard: Alright... here it is. Can I have it now?")
    wait()
    print(f"{namePlayer}: Hold on, how do we get home with this?")
    wait()
    print("Security Guard: Look in the mop bucket.")
    wait()
    print("You look inside the mop bucket- it's a portal.")
    wait()
    print("21: What? Why you guys have dis?")
    wait()
    print("Security Guard: I dunno, in case someone bribes us?")
    wait()
    print("How handy...")
    wait()
    print("You hand the security guard his porscuitto. ")
    wait()
    print("Security Guard: Good. Now never come back again, you two could have ended up in biiig trouble!")
    wait()
    print("21: Aight, we get it, we gonna leave now...")
    wait()
    print("You both hop into the bucket one at at a time. After a short ride through a bunch of green nothing...")
    wait()
    print("You're both back home!")
    wait()
    gameComplete()

def securityGuardOptions():
    print("21, whispering: (Psst! You can bribe dis guy!)")
    wait()
    while True:
        print("""
        1. Bribe guard with porscuitto
        2. Don't. Too easy""")
        wait()
        option = input("What do you want to do? >> ")
        if option == "1":
            bribe()
        elif option == "2":
            print("Alright, your choice!")
            wait()
            hospitalOptions()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option. Try again.")
            wait()
            continue

def room199():
    global inventory
    wait()
    print("You are on your way to room 199. When you get there, there's a sick creature in the bed.")
    wait()
    print("Creature: I should have never cooked that chicken medium rare...")
    wait()
    print(f"{namePlayer}: Wow, they are just that stupid, aren't they?")
    wait()
    print("21 was busy getting the rocket launcher out of under the bed.")
    wait()
    print("Creature: Screw you, human! That was my secret weapon!")
    wait()
    print("21: For what?")
    wait()
    inventory.append("Rocket Launcher")
    inventory.append("Rocket x3")
    print("Creature: Uhh... I dunno!")
    wait()
    print("21: Exactly. Let's get da hell out.")
    wait()
    print("The rocket launcher has been added to your inventory.")
    wait()
    hospitalOptions()

def shootIt():
    print("21 shoots the rocket-")
    wait()
    print("He misses.")
    wait()
    print("You both get mauled by the monster and die...")
    wait()
    lifeCheck()

def runBackDown():
    print("21: What? Dis plan better be good, why are we doin-")
    wait()
    print("Going back down was a bad move, you both got mauled.")
    wait()
    lifeCheck()

def stupidMom():
    print(f"{namePlayer}: Hey monster!")
    wait()
    print("The monster looks at you.")
    wait()
    print("Crea-tur: Oh? You have something to say to MY monster?")
    wait()
    print(f"{namePlayer}: Yeah! Your mother's stupid!")
    wait()
    print("...")
    wait()
    print("The monster eats you.")
    wait()
    print("Crea-tur: That's what you get for being immature! Ta-ta!")
    wait()
    print("You're dead!")
    wait()
    lifeCheck()

def matador():
    print("You rip off a piece of curtain and taunt it.")
    wait()
    print(f"{namePlayer}: Hey you! Come get this!")
    wait()
    print("The monster rushes towards you.")
    wait()
    print("You don't pull back in time and he hits you, killing you.")
    wait()
    print("You're dead!")
    wait()
    lifeCheck()

def finalRoom():
    global inventory
    inventory.remove("Rocket Launcher")
    inventory.remove("Rocket")
    print("With another fire of the rocket launcher, the door with the portal bursts open!")
    wait()
    print(f"{namePlayer}: Oh, hell yeah! Does this mean we can finally leave?")
    wait()
    print("21: @)$! dawg, what the hell you think?")
    wait()
    print("You both step inside the pitch-black room with the glowing green portal.")
    wait()
    print("21: Well, it's been nice workin with ya, kid. We finally get to leave dis place.")
    wait()
    print(f"{namePlayer}: Yeah... not many people can say they worked with someone famous to escape a... castle full of weird creatures.")
    wait()
    print("21: Exactly. Where dat with pride. Tell all your friends, also buy my new album, in stores now.")
    wait()
    print("21: Anyway, cya! I gotta go back to my mansion. Hopefully they ain't auction it off for tax purposes.")
    wait()
    print(f"{namePlayer}: Alright, cya later...")
    wait()
    print("21 made it through the portal... and after that, you step in too...")
    wait()
    print("And wouldn't you know it, you're back at the train station you came from!")
    wait()
    gameComplete()

def funnyFace():
    print("21: Make a funny face? Dat might work...")
    wait()
    print("You make a funny face at the monster...")
    wait()
    print("...")
    wait()
    print("The monster actually starts to laugh!")
    wait()
    print("21: Hey! Dat worked! Let me shoot it!")
    wait()
    print("21 shoots the rocket launcher...")
    wait()
    print("It hits the creature, and it works!")
    wait()
    monsterDefeat()

def monsterDefeat():
    global inventory
    inventory.remove("Rocket x2")
    inventory.append("Rocket")
    print("21: Hell yeah! We done made it!")
    wait()
    print(f"{namePlayer}: Wooooo hooo!")
    wait()
    print("Crea-tur: No! You killed my strongest one! Now I need to go back to using Jeff!")
    wait()
    print("21: Have fun wit dat. Jeff's in da hospital, he cooked his chicken medium rare.")
    wait()
    print("Crea-tur: No! No! No! You'll pay! I hope you have FUN back at home, idiots!")
    wait()
    print("She stormed out of the room, presumably to the hospital.")
    wait()
    print("21: Aight, now we got dat outta da way, lemme blow open dis door!")
    wait()
    finalRoom()

def splitDistract():
    print("21: Dat's a good idea. Let's both split up, and go on the two different staircases.")
    wait()
    print("You go to the right staircase, and he goes to the left.")
    wait()
    print("Crea-tur: Aw, come on! Let me kill ya!")
    wait()
    print("What's next?")
    while True:
        print("""
        1. Call its Mother stupid
        2. Tear off a piece of red curtain and taunt it like a matador
        3. Make a funny face at the creature""")
        option = input("What do you want to do? >> ")
        if option == "1":
            stupidMom()
        elif option == "2":
            matador()
        elif option == "3":
            funnyFace()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid input. Try again.")
            wait()
            continue

def splitAttack():
    randomChoice = random.choice(['weak', 'carry'])
    if randomChoice == "weak":
        print("21: Lemme hand you the rocket launcher!")
        wait()
        print("You try to catch it- and you do- but...")
        wait()
        print("You're far too weak to hold it. You fall down, and can't get up, and...")
        wait()
        print("Get eaten by the monster!")
        wait()
        print("You're dead!")
        wait()
        lifeCheck()
    elif randomChoice == "carry":
        print("21: Lemme hand you the rocket launcher!")
        wait()
        print("You try to catch it- and you do- but...")
        wait()
        print("You are able to carry it!")
        wait()
        print("You decide the best course of action is to shoot the monster...")
        wait()
        print("And voila! A successful hit!")
        wait()
        monsterDefeat()

def jumpOff():
    print("You jump off the landing and onto the carpet below.")
    wait()
    print("The monster tries to chase you- but one of his claws snags on the carpet below him, and he trips and falls, knocking him out!")
    wait()
    print("21: Oh, dat's hilarious.")
    wait()
    monsterDefeat()

def runUp():
    print("You are now at the landing.")
    wait()
    print("21: @($*, what do we do now?")
    wait()
    while True:
        print("""
        1. Split up and distract
        2. Split up and attack
        3. Jump off the landing and fight it head-on!""")
        option = input("What do you want to do? >> ")
        if option == "1":
            splitDistract()
        elif option == "2":
            splitAttack()
        elif option == "3":
            jumpOff()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option. Try again.")
            wait()
            continue

def runForSafety():
    print("Good call!")
    wait()
    print("You both ran to the bottom of the staircase.")
    wait()
    print("21: Quick! What do we do now?")
    wait()
    while True:
        print("""
        1. Run back down, you can get better aim there.
        2. Run up the staircase to avoid the monster.""")
        option = input("What do you want to do ? >> ")
        if option == "1":
            runBackDown()
        elif option == "2":
            runUp()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid input. Try again.")
            wait()
            continue
        

global liveCount
liveCount = 3

def lifeCheck():
    global liveCount
    liveCount -= 1
    if liveCount == 0:
        outOfLives()
    else:
        bossFight()

def bossFight():
    global liveCount
    print("Lives left : ", liveCount)
    time.sleep(1)
    while True:
        print("""
        1. Shoot it right now!
        2. Run for safety!""")
        option = input("What do you want to do? >> ")
        if option == "1":
            shootIt()
        elif option == "2":
            runForSafety()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid input. Try again.")
            wait()
            continue
    

def finalBossRoom():
    print("You arrive at the room. It's a red room with very sophisticated furnishings, red carpet, red drapes, and brown-red staircases on both sides, both leading to a landing.")
    wait()
    print("21: Aight, here we is... the final room. It shouldn't be too hard. Dis room's locked up in case of emergency.")
    wait()
    print(f"{namePlayer}: Emergency?")
    wait()
    print("21: Dere's a room at da top of that landing. We need to blow dat open too. It can either bring us back to dat train station you came from, or it's just a \"panic room\" for tha monstas when they scared.")
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
    print("21: She the general of these creatures! Her name's Crea-tur!")
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
    bossFight()

def finalBossWarning():
    print("""
    WARNING: Final boss time! 
    You will have THREE (3) chances to try and defeat the boss.
    Lives will be printed every retry.
    Some options might be random and in the hands of fate... so be careful of that!
    If you run out of lives... you need to redo the whole program!
    """)
    time.sleep(1)
    print("Press any key to continue.")
    wait()
    finalBossRoom()

def hallway12():
    global inventory
    print("21: Alright, we here. Stand back.")
    wait()
    print(f"{namePlayer}: What? Why?")
    wait()
    print("21: I gotta blow tha door open")
    wait()
    print("You stand back, and with a quick fire of the rocket, the door in front of you blows open, revealing a stairway")
    wait()
    print("BOOM!")
    wait()
    print("That was less exciting, especially just in text form.")
    wait()
    print("You both go up the staircase and you're met with a surprise...")
    inventory.remove("Rocket x3")
    inventory.append("Rocket x2")
    wait()
    finalBossWarning()

def examineCreatures():
    randNum = randint(1,2)
    if randNum == 1:
        print("There are some sick creatures in this waiting room.")
        wait()
        print("Creature 1: I didn't know you couldn't eat steak raw!")
        wait()
        print("Creature 2: That wasn't steak, that was pig.")
        wait()
        print("Creature 3: I think you mean pork?")
        wait()
        print("Creature 2: Shut up, I know what I'm talking about.")
        wait()
        hospitalOptions()
    elif randNum == 2:
        print("There are some sick creatures in this waiting room.")
        wait()
        print("Creature 1: What's up with you?")
        wait()
        print("Creature 2: I ate raw chicken...")
        wait()
        print("Creature 1: You're dumb, you're not supposed to eat raw chicken, dude.")
        wait()
        print("Creature 2: Oh really? Then why are you here?")
        wait()
        print("Creature 1: I have an ear infection.")
        wait()
        print("Creature 2: Oh.")
        wait()
        hospitalOptions()

def hospital():
    print("You arrive at the hospital. There are a lot of sick creatures...")
    wait()
    print("21: Aight, do you know why we here?")
    wait()
    print(f"{namePlayer}: No, not really. Why?")
    wait()
    print("21: There's a rocket launcher somewhere in here. We can use that to get out. First to get to the next floor, and second if we need to defend ourselfs.")
    wait()
    print("21: It should be in dat room 199. I know a guy who's sick right now and always keeps one, we can take it from him.")
    wait()
    print(f"{namePlayer}: Alright... sounds good I guess.")
    wait()
    print("Find the rocket launcher.")
    wait()
    hospitalOptions()

def hospitalOptions():
    global inventory
    if "Rocket Launcher" not in inventory:
        while True:
            print("""
            1. Inspect plant
            2. Talk to security guard
            3. Examine creatures
            4. Go to room 199""")
            option = input("What do you want to do? >> ")
            if option == "1":
                inspectPlant()
            elif option == "2":
                securityGuard()
            elif option == "3":
                examineCreatures()
            elif option == "4":
                room199()
            elif option == "44":
                printOutInventory()
                wait()
                continue
            else:
                print("Invalid input. Try again.")
                wait()
                continue
    else:
        while True:
            print("""
            1. Inspect plant
            2. Talk to security guard
            3. Examine creatures
            4. Leave""")
            option = input("What do you want to do? >> ")
            if option == "1":
                inspectPlant()
            elif option == "2":
                securityGuard()
            elif option == "3":
                examineCreatures()
            elif option == "4":
                hallway12()
            elif option == "44":
                printOutInventory()
                wait()
                continue
            else:
                print("Invalid input. Try again.")
                wait()
                continue


def secondFloorOptions():
    while True:
        print("""
    1. First Door
    2. Second Door
    3. Third Door""")
        door = input("Which door do you want to go through? >> ")
        if door == "1":
            secondFloorDoor1()
        elif door == "2":
            secondFloorDoor2()
        elif door == "3":
            hospital()
        elif door == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option.")
            wait()
            continue

def proceedToFirst():
    print("You touch the doorknob to the next floor. However, you're interrupted.")
    wait()
    print("21: Hey, kid...")
    wait()
    print("You: Uhm... yes??")
    wait()
    print("21: Let me come with you. I be damned if another person die in this place.")
    wait()
    print("You: But didn't you say you liked it here?")
    wait()
    print("21: I do, but as time goes by I'm gonna get lazier. If I ever do need to go back, I won't be on my grind as much. You feel?")
    wait()
    print("21: And besides, sometimes these creatures is annoying. I don't know how long imma take that.")
    wait()
    print("You: Well, if you really want to come, I guess you can.")
    wait()
    print("21: Good, I woulda finna went anyway, but I'm glad you fine with it.")
    wait()
    print("21: We gonna make a great team together, kid.")
    print("But first, tell me somethin, what's your name? Type Yes to confirm or anything else to re-enter.")
    while True:
        global namePlayer
        namePlayer = str(input("Enter your name. >> "))
        confirm = str(input(f"Is {namePlayer} your name?"))
        if confirm in ("Yes"):
            print(f"{namePlayer}: My name is {namePlayer}. Pleasure to meet you.")
            wait()
            print("21: Hell yeah, you bet it is. You already know me.")
            wait()
            print("21: So is we on our way now we got everything settled?")
            wait()
            print(f"{namePlayer}: Yep... let's get out of here.")
            wait()
            print("With your newfound team member, you open the door to the next floor with confidence in getting out of this place.")
            wait()
            secondFloor()
        else:
            continue

def creatureBrkRoom():
    wait()
    print("Creature: Hello, human! What brings you here? ")
    wait()
    print("You: I'm trying to get out of here.")
    wait()
    print("Creature: I don't supposed you came off that train? After sleeping? You won't believe how many people tell us that before we kill them!")
    wait()
    print("...")
    wait()
    print("Creature: Ooops. I mean others. They do the killing. I don't like humans. ")
    wait()
    print("You: Well, that's comforting, I guess...")
    wait()
    print("That conversation was odd.")
    wait()
    breakRoom()

def breakAfterConversation():
    while True:
        print("""You're in the break room.
        1. Proceed onward.""")
        option = input("What do you want to do? >> ")
        if option == "1":
            proceedToFirst()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option, try again.")
            wait()
            continue

def savage21():
    print("You approach the shadowy figure with his back turned against the desk.")
    wait()
    print("You: Uhhh, hello? Who is this? ")
    wait()
    print("A familiar famous figure turns his chair around.")
    wait()
    print("It's no one other than 21 Savage in the flesh!")
    wait()
    print("You: Wh- you!?")
    wait()
    print("21: Hey there, $&%^@. What's a lil kid doin in this castle? This a dangerous place.")
    wait()
    print("You: Can we not swear? This is a school assignment.")
    wait()
    print("21: My apologies, kid. But how the hell did you get in here? Dey gonna kill ya!")
    wait()
    print("You: I accidentally took a one-way train here. I need to find my way home!")
    wait()
    print("21: Aw, man, this the fifth time this week! And four of em didn't make it!")
    wait()
    print("You: Aaaah!")
    wait()
    print("21: Don't be scared, lil kid, I can see it in your eyes. You gonna make it out alive!")
    wait()
    print("You: Really? You think so?")
    wait()
    print("21: I dunno. I'm tryna be motivational here.")
    wait()
    print("You: Well, that's flattering...")
    wait()
    print("You: How did you end up in here? It's really odd seeing you out of all people in this room.")
    wait()
    print("""21: Well, they was gonna send me back to the UK, but I ain't want that, so I ended up fleeing on the same train you took.
    Luckily, the monstas recognized me, and now I live here. It's a real bad place, these monstas will find anyone and eat em alive! Tougher
    than Zone 6! And all they feed me is porscuitto. That s**t stretchy as hell, I'm sick of it.""")
    wait()
    print("You: Oh, so that's where you went. It doesn't seem good here, and besides, a lot of people miss you, dude.")
    wait()
    print("21: I realize dat, but a life without fame is a lot more quiet, so here I am.")
    wait()
    print("You: That makes sense... so, do you know how to get out of this place?")
    wait()
    print("21: Hell yeah I do. But it ain't gonna be easy. You gotta get to the top floor of dis castle.")
    print("21: There are two floors to go afta this one. Once you at the top there should be a portal back to the train station.")
    print("21: On your way, you gonna meet some nasty creatures, tho. I advise you watch yo back!")
    wait()
    print("You: Oh no, what kind of creatures?")
    wait()
    print("21: I cannot say, it's too violent. Mr. Shaft will take marks off.")
    wait()
    print("Ugh, fine. I'll find out when the time comes but I'm sure it won't be pretty.")
    wait()
    print("You: 21: The door behind me is the way to the second floor. It's a hospital, fulla sick creatures.")
    wait()
    print("You: ...That's kind of sad. What type of diseases?")
    wait()
    print("21: Mostly scurvy. They don't eat no fruit. I been tryna get them to take supplements but they don't know what dat is.")
    print("21: Regardless, you gon have to find a special weapon to break down the barrier to floor three. It's in dat hospital.")
    wait()
    print("You: Alright, thank you. ")
    wait()
    print("21: Good luck on your travels, child, and I hope you make it back in one piece.")
    wait()
    print("You: Didn't think I'd have someone say that to me, but thanks...")
    wait()
    breakAfterConversation()

def breakRoom():
    print("You're in the break room.")
    wait()
    while True:
        print("""
        1. Talk to the shadowy figure
        2. Talk to the friendly creature
        3. Drink coffee""")
        option = input("What do you want to do? >> ")
        if option == "1":
            savage21()
        elif option == "2":
            creatureBrkRoom()
        elif option == "3":
            coffee()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option. Try again.")
            wait()
            continue

def leftEdge():
    print("You decide to sneak left.")
    wait()
    print("You come across a door. You look through, and it's a few creatures having a business meeting.")
    wait()
    print("Best not disturb them...")
    wait()
    print("You continue creeping to the left... and you come across a break room.")
    wait()
    print("The door is unlocked, so you decide to open it. There's a friendly creature sitting there, and a shadowy figure in the chair at a desk.")
    wait()
    breakRoom()

def tryLeaving():
    print("You try to open the castle door behind you quietly.")
    wait()
    print("It doesn't budge. You're stuck.")
    wait()
    castleOptions()

def walkMiddle():
    print("You step into the middle of the castle foyer...")
    wait()
    print("You die! The guarding monsters don't like intruders.")
    wait()
    deathAftermath()

def tryUnlock():
    print("You try unlocking the door...")
    wait()
    print("There's no keyhole! No way out!")
    global triedUnlocking
    triedUnlocking = True
    wait()
    castleOptions()

def enterCastle():
    print("You enter the castle ever-so-carefully. You're in the foyer now, and there are multiple creatures guarding a big staircase.")
    wait()
    print("You think to yourself that you should probably be very quiet and sneaky if you're going to get out successfully.")
    wait()
    castleOptions()

global triedUnlocking
triedUnlocking = False

def castleOptions():
    global triedUnlocking
    global inventory
    global flag
    if "Key" not in inventory and triedUnlocking is False:
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the right edge of the room.
            4. Creep around the left edge of the room.""")
            option = input("What do you want to do? >> ")
            if option == "1":
                tryLeaving()
            elif option == "2":
                walkMiddle()
            elif option == "3":
                rightEdge()
            elif option == "4":
                leftEdge()
            elif option == "44":
                printOutInventory()
                wait()
                continue
            else:
                print("Invalid input.")
                wait()
                continue
    elif "Key" in inventory and triedUnlocking is False:
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the left edge of the room.
            4. Try unlocking the front door with the key.""")
            option = input("What do you want to do? >> ")
            if option == "1":
                tryLeaving()
            elif option == "2":
                walkMiddle()
            elif option == "3":
                leftEdge()
            elif option == "4":
                tryUnlock()
            elif option == "44":
                printOutInventory()
                wait()
                continue
            else:
                print("Invalid input.")
                wait()
                continue
    elif "Key" in inventory and triedUnlocking is True:
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the left edge of the room.""")
            option = input("What do you want to do? >> ")
            if option == "1":
                tryLeaving()
            elif option == "2":
                walkMiddle()
            elif option == "3":
                leftEdge()
            elif option == "44":
                printOutInventory()
                wait()
                continue
            else:
                print("Invalid input.")
                wait()
                continue
    elif "Key" not in inventory and flag is True:
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the left edge of the room.""")
            option = input("What do you want to do? >> ")
            if option == "1":
                tryLeaving()
            elif option == "2":
                walkMiddle()
            elif option == "3":
                leftEdge()
            elif option == "44":
                printOutInventory()
                wait()
                continue
            else:
                print("Invalid input.")
                wait()
                continue

def talk1():
    print("Creature: Hey, kiddo! What are you doing here?")
    wait()
    print("You: I fell asleep on a train and got off here. Any way I can get out?")
    wait()
    print("Creature: Sorry, kiddo. That's a one-way stop. They only let people get off that train, not on.")
    wait()
    print("You: Okay, you're kidding with me, right?")
    wait()
    print("Creature: Nope. I wish I was.. this place is less than ideal to be around.")
    wait()
    print("You: Huh? What do you mean?")
    wait()
    print("Creature: Aw, crap, I've said too much. You go on with your day now, I'll let you find out...")
    wait()
    print("You: Uhh... okayyy?")
    print("You return back to where you started.")
    wait()
    introOptions()

def railway():
    print("You go back to the railway and wait a little...")
    wait()
    print("No trains! You give up and head back to the front of the castle.")
    wait()
    introOptions()

def introOptions():
    while True:
        print("""
        1. Go back to the railway to find a way home.
        2. Talk to a bystanding creature
        3. Go up to the castle steps and enter.""")
        option = input("What do you want to do? >>")
        if option == "1":
            railway()
        elif option == "2":
            talk1()
        elif option == "3":
            enterCastle()
        elif option == "44":
            printOutInventory()
            wait()
            continue
        else:
            print("Invalid option. Try again.")
            wait()
            continue

def intro():
    print("""
    Game Instructions:
    - During dialogue, press any key to continue through it.
    - If you type 44 during a decision making moment, your inventory will print out.
    - Have fun!
    Press any key to continue.""")
    wait()
    print("Oh no! After falling asleep on the train back home from school, you accidentally got off a stop at some sort of castle.")
    wait()
    print("You: What the hell is this place?")
    wait()
    print("You hear nothing but gusts of wind in the background.")
    wait()
    print("You: Might as well try getting out of here...")
    wait()
    introOptions()
            
intro()