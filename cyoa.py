import time
from random import randint
import msvcrt as m

global name
name = ""
inventory = []
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
            exit()
        else:
            print("Bad input!")
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
            break
        else:
            print("Bad input!")
            continue

def pokeCreature():
    print("You poke the creature in the eyes as it lunges towards you...")
    wait()
    inventory.remove("Key")
    print("The monster stops. You blinded it, and it's now wandering around. ")
    print("Congrats! You can go home now. What do you want to do?")
    while True:
        print("""
        1. Go through the portal
        2. Go back to the foyer... it's too easy.""")
        option = input("What do you want to do?? >>")
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
                castleOptions()

def roomDeath():
    print("You should probably know from your instincts these guys don't take well to reasoning.")
    wait()
    print("Aaand you're dead!")
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
        else:
            print("Invalid option.")
            continue
        
def rightAfterCafeteria():
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
                    castleOptions()
                elif option == "2":
                    print("You use your key to try and u1nlock it...")
                    wait()
                    print("Voila! It works!")
                    unlockedRoom()
                elif option == "44":
                    printOutInventory()
                    continue
                else: 
                    print("Invalid option. Try again")
                    continue
        else:
            while True:
                print("""
                1. Go back to the way you came.
                2. Use your key to unlock the door.""")
                option = input("What do you want to do?? >> ")
                if option == "1":
                    print("You give up and walk back to square one.")
                    wait()
                    castleOptions()
                elif option == "2":
                    print("You don't have a key to unlock it.")
                    wait()
                    continue
                else:
                    print("Invalid input. Try again.")
                    wait()
                    continue



def sneakyBeakyLike():
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
    rightAfterCafeteria()

def nonchalantCafe():
    print("You enter the cafe like you won't die...")
    wait()
    print("But you do.")
    print("These creatures don't take kindly to intruders!")
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
        else:
            print("Wrong input. Try again.")
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
            continueOn()
        else:
            print("Wrong input, try again")
            continue

def coffee():
    wait()
    print("You try some coffee on the desk...")
    wait()
    print("You don't like it, so you spit it out.")
    wait()
    print("""
    1. Clean it up
    2. Just leave it""")
    cleanUp = input("Clean up your mess? >> ")
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

def searchDesk():
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
    secondFloorDoor1Options()

def secondFloorDoor1():
    print("It's a library like room...")
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
        else:
            print("Invalid input. Try again.")
            wait()
            continue

def admirePaintings():
    print("It's a painting of of a cow, crudely drawn too.")
    wait()
    print("21: Yeah, these dudes have no idea what true art is.")
    wait()
    print(f"{name}: Yeah, I can see. The black and white spots are mixed up. ")
    wait()
    print("21: They tried bringing a chocolate cow over here to get chocolate milk once. ")
    wait()
    print(f"{name}: That must have been disappointing for them.")
    wait()
    print("21: You could imagine how I feel, I wanted some chocolate milk myself.")
    wait()
    print(f"{name}: ...")
    secondFloorDoor2Options()

def admireStatue():
    print("It's a poorly-made statue of David, but with a creature head on it.")
    wait()
    print("You think to yourself, you did not need to look closer at that today...")
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
        else:
            print("Invalid input. Try again.")
            wait()
            continue

def secondFloor():
    print("You arrived at the second floor, and are greeted with three doors.")
    wait()
    print("21: The hospital should be somewhere in deez three doors. Let's go explorin'.")
    secondFloorOptions()

def hopsital():
    print("You enter the hospital... it's a waiting room and you see a bunch of sick creatures ")
    wait()
    print("21: Stupid thangs ain't cook they meat properly.")
    wait()
    print(f"{name}: Can't say I'm too surprised...")
    wait()
    print("21: Bull#$*^ aside, the room the rocket launcher is hidden in is somewhere in room 199. Let's head there.")
    wait()
    hospitalOptions()

def inspectPlant():
    wait()
    global plantCount
    plantCount += 1
    if plantCount < 2:
        print("You touch the plant. Neat plant- it's fake though.")
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
    print("You talk to the security guard.")
    wait()
    print("Secuirty Guard: Ach! Humans! We have enough sickness here, get out!")
    wait()
    print("21: Why the hell are you talkin to this guy? He gonna kill us!")
    wait()
    print("Security Guard: Nah. We don't like police brutality here. We leave the killing up to the random monsters, like the janitors.")
    wait()
    print(f"{name}: Odd. More civilized than actual human beings.")
    if "Porscuitto" in inventory:
        securityGuardOptions()
    else:
        hospitalOptions()

def bribe():
    print("You give the security guard the porscuitto.")
    wait()
    print(f"{name}: How about you do us a favor for this?")
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
    print(f"{name}: Hold on, how do we get home with this?")
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

def room199():
    wait()
    print("You are on your way to room 199. When you get there, there's a sick creature in the bed.")
    wait()
    print("Creature: I should have never cooked that chicken medium rare...")
    wait()
    print(f"{name}: Wow, they are just that stupid, aren't they?")
    wait()
    print("21 was busy getting the rocket launcher out of under the bed.")
    wait()
    print("Creature: Screw you, human! That was my secret weapon!")
    wait()
    print("21: For what?")
    wait()
    inventory.append("Rocket Launcher")
    inventory.append("Rocket" * 3)
    print("Creature: Uhh... I dunno!")
    wait()
    print("21: Exactly. Let's get da hell out.")
    wait()
    print("The rocket launcher has been added to your inventory.")
    hospitalOptions()

def finalBossRoom():
    print("You arrive at the room. It's a red room with very sophisticated furnishings, red carpet, red drapes, and brown-red staircases on both sides, both leading to a landing.")
    wait()
    print("21: Aight, here we is... the final room. It shouldn't be too hard. Dis room's locked up in case of emergency.")
    wait()
    print(f"{name}: Emergency?")
    wait()
    print("21: Dere's a room at da top of that landing. We need to blow dat open too. Dere's a switch we gotta pull, it can either bring us back to dat train station you came from, or it can lead to a \"panic room\".")
    wait()
    print(f"{name}: Well, let's get going then, what are we waiting for?")
    wait()
    print("21: Well, da thing is...")
    wait()
    print("21: Dis s$*%'s too quiet, dawg.")
    wait()
    print(f"{name}: What? What do you mean, quiet? Is something going to happen?")
    wait()
    print("21: Maybe... ")
    wait()
    print("...")
    wait()
    print("Out of nowhere, the right wall starts cracking.")
    wait()
    print(f"{name}: W-what's that???")
    wait()
    print("A huge creature breaks out of the wall, and someone's riding on top of it!")
    wait()
    print("21: Oh no, it's her! I shoulda known that broad was gonna pop up!")
    wait()
    print("")

def finalBossWarning():
    print("""
    WARNING: Final boss time! 
    After the dialogue is finished a timer will start.
    You will have FIVE (5) minutes to find the right path and defeat the boss.
    You will have THREE (3) chances to do so.
    Time and lives will be printed every retry.
    If you run out of time or lives... you need to redo everything!
    """)
    wait()
    print("Press any key to continue.")
    wait()
    finalBossRoom()

def hallway12():
    print("21: Alright, we here. Stand back.")
    wait()
    print(f"{name}: What? Why?")
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
    print(f"{name}: No, not really. Why?")
    wait()
    print("21: There's a rocket launcher somewhere in here. We can use that to get out. First to get to the next floor, and second if we need to defend ourselfs.")
    wait()
    print("21: It should be in dat room 199. I know a guy who's sick right now and always keeps one, we can take it from him.")
    wait()
    print(f"{name}: Alright... sounds good I guess.")
    wait()
    print("Find the rocket launcher.")
    hospitalOptions()

def hospitalOptions():
    if "Rocket Launcher" not in inventory:
        while True:
            print("""
            1. Inspect plant
            2. Talk to security guard
            3. Go to room 199""")
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
            3. Leave""")
            option = input("What do you want to do? >> ")
            if option == "1":
                inspectPlant()
            elif option == "2":
                securityGuard()
            elif option == "3":
                hallway12()
            elif option == "44":
                printOutInventory()
                continue
            else:
                print("Invalid input. Try again.")
                wait()
                continue


def secondFloorOptions():
    wait()
    while True:
        print("""
    1. First Door
    2. Second Door
    3. Third Door""")
        door = input("Which door do you want to go through? >>")
        if door == "1":
            secondFloorDoor1()
        elif door == "2":
            secondFloorDoor2()
        elif door == "3":
            hospital()
        else:
            print("Invalid option.")
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
    print("But first, tell me somethin, what's your name?")
    while True:
        global name
        name = str(input("Enter your name. >>"))
        confirm = str(input(f"Is {name} your name?"))
        if confirm in ("Yes"):
            print(f"{name}: My name is {name}. Pleasure to meet you.")
            wait()
            print("21: Hell yeah, you bet it is. You already know me.")
            print("21: So is we on our way now we got everything settled?")
            wait()
            print(f"{name}: Yep... let's get out of here.")
            wait()
            print("With your newfound team member, you open the door to the next floor with confidence in getting out of this place.")
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
    breakRoom()

def breakAfterConversation():
    print("""You're in the break room.
    1. Proceed onward.""")
    while True:
        option = int(input("What do you want to do? >>"))
        if option == 1:
            proceedToFirst()
        else:
            print("Invalid option, try again.")
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
        else:
            print("Invalid option. Try again.")
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
    deathAftermath()

def tryUnlock():
    print("You try unlocking the door...")
    wait()
    print("There's no keyhole! No way out!")
    global triedUnlocking
    triedUnlocking = True
    castleOptions()

def enterCastle():
    print("You enter the castle ever-so-carefully. You're in the foyer now, and there are multiple creatures guarding a big staircase.")
    wait()
    print("You think to yourself that you should probably be very quiet and sneaky if you're going to get out successfully.")
    castleOptions()

def castleOptions():
    global triedUnlocking
    triedUnlocking = False
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
            else:
                print("Invalid input.")
                continue
    elif "Key" in inventory and triedUnlocking is False:
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the left edge of the room.
            4. Try unlocking the front door with the key.""")
            option = input("What do you want to do?")
            if option == "1":
                tryLeaving()
            elif option == "2":
                walkMiddle()
            elif option == "3":
                leftEdge()
            elif option == "4":
                tryUnlock()
            else:
                print("Invalid input.")
                continue
    elif "Key" in inventory and triedUnlocking is True:
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the left edge of the room.""")
            option = input("What do you want to do?")
            if option == "1":
                tryLeaving()
            elif option == "2":
                walkMiddle()
            elif option == "3":
                leftEdge()
            else:
                print("Invalid input.")
                continue
    elif "Key" not in inventory and flag is True:
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the left edge of the room.""")
            option = input("What do you want to do?")
            if option == "1":
                tryLeaving()
            elif option == "2":
                walkMiddle()
            elif option == "3":
                leftEdge()
            else:
                print("Invalid input.")
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
    introOptions()

def railway():
    print("You go back to the railway and wait a little...")
    wait()
    print("No trains! You give up and head back to the front of the castle.")
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
            else:
                print("Invalid option. Try again.")
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