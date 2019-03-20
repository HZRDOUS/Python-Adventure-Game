import time

global name
name = ""
inventory = []

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
    time.sleep(3)
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
            time.sleep(3)
            print("You successfully arrive back at the train station you came from.")
            time.sleep(2)
            gameComplete()
        elif option == "2":
            print("...")
            time.sleep(2)
            print("Are you serious??? ")
            time.sleep(1)
            print("You want to go back??")
            time.sleep(1)
            print("""
            1. Yes
            2. No""")
            goBack = input("Really?? >> ")
            if goBack == "1":
                time.sleep(2)
                print("Wow... well, alright, then.")
                time.sleep(1)
                print("You go back to where you started... for some reason...")
                time.sleep(1)
                global triedUnlocking
                triedUnlocking = True
                castleOptions()

def roomDeath():
    print("You should probably know from your instincts these guys don't take well to reasoning.")
    time.sleep(2)
    print("Aaand you're dead!")
    deathAftermath()

def unlockedRoom():
    print("You enter the unlocked room... but you're greeted to a big surprise!")
    global flag
    flag = True
    time.sleep(2)
    print("A portal that says... back to your home town! Just your luck!")
    time.sleep(2)
    print("Oh yeah, did I mention that there's a bloodthirsty monster guarding that portal!")
    time.sleep(2)
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
                    time.sleep(3)
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
                    time.sleep(1)
                    castleOptions()
                elif option == "2":
                    print("You don't have a key to unlock it.")
                    time.sleep(1)
                    continue
                else:
                    print("Invalid input. Try again.")
                    time.sleep(1)
                    continue



def sneakyBeakyLike():
    print("You sneak around the corners of the cafeteria.")
    print("The creatures are far too distracted to notice you.")
    time.sleep(5)
    print("You snoop around and go to the shiny object... aha! You got it.")
    time.sleep(1)
    print("It's a key!")
    inventory.append("Key")
    time.sleep(3)
    print("The key has been added to your inventory.")
    print("(Handy tip: You can look at your inventory by entering \"44\" at any decision moment.)")
    time.sleep(3)
    print("You slowly make your way back to the entrance. You're now back where you started.")
    rightAfterCafeteria()

def nonchalantCafe():
    print("You enter the cafe like you won't die...")
    time.sleep(3)
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
    time.sleep(1)
    print("You come across a door. You look inside.")
    print("The creatures are having lunch in the cafeteria... it's basically a riot in there!")
    print("However, in the midst of the riot, you see a shimmer of a certain object...")
    print("You aren't sure if it's worth it to go in there.")
    time.sleep(5)
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
    time.sleep(1)
    print("You try some coffee on the desk...")
    time.sleep(2)
    print("You don't like it, so you spit it out.")
    time.sleep(2)
    print("""
    1. Clean it up
    2. Just leave it""")
    cleanUp = input("Clean up your mess? >> ")
    if cleanUp == "1":
        print("You clean up the mess. ")
        time.sleep(1)
        print("A janitor creature approaches you.")
        time.sleep(1)
        print("Janitor: Thanks for cleaning up that mess. I hate when people leave messes like that and don't clean it up!")
        time.sleep(4)
        breakRoom()
    elif cleanUp == "2":
        print("You leave it there like a slob.")
        time.sleep(2)
        print("A janitor creature approaches you. ")
        time.sleep(1)
        print("Janitor: HEY! YOU DIDN'T CLEAN UP YOUR MESS! COME HERE!")
        time.sleep(3)
        print("You try to outrun him, but you can't run faster than him.")
        time.sleep(3)
        print("He eats you, and you die!")
        time.sleep(1)
        deathAftermath()

def secondFloor():
    print("You arrived at the second floor, and are greeted with three doors.")
    time.sleep(4)
    print("21: The hospital should be somewhere in deez three doors. Let's go explorin'.")
    time.sleep(4)
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
    time.sleep(3)
    print("21: Hey, kid...")
    time.sleep(2)
    print("You: Uhm... yes??")
    time.sleep(3)
    print("21: Let me come with you. I be damned if another person die in this place.")
    time.sleep(3)
    print("You: But didn't you say you liked it here?")
    time.sleep(3)
    print("21: I do, but as time goes by I'm gonna get lazier. If I ever do need to go back, I won't be on my grind as much. You feel?")
    time.sleep(4)
    print("21: And besides, sometimes these creatures is annoying. I don't know how long imma take that.")
    time.sleep(4)
    print("You: Well, if you really want to come, I guess you can.")
    time.sleep(3)
    print("21: Good, I woulda finna went anyway, but I'm glad you fine with it.")
    time.sleep(3)
    print("21: We gonna make a great team together, kid.")
    print("But first, tell me somethin, what's your name?")
    while True:
        global name
        name = str(input("Enter your name. >>"))
        confirm = str(input(f"Is {name} your name?"))
        if confirm in ("Yes"):
            print(f"{name}: My name is {name}. Pleasure to meet you.")
            time.sleep(4)
            print("21: Hell yeah, you bet it is. You already know me.")
            print("21: So is we on our way now we got everything settled?")
            time.sleep(6)
            print(f"{name}: Yep... let's get out of here.")
            time.sleep(4)
            print("With your newfound team member, you open the door to the next floor with confidence in getting out of this place.")
            secondFloor()
        else:
            continue

def creatureBrkRoom():
    time.sleep(1)
    print("Creature: Hello, human! What brings you here? ")
    time.sleep(3)
    print("You: I'm trying to get out of here.")
    time.sleep(2)
    print("Creature: I don't supposed you came off that train? After sleeping? You won't believe how many people tell us that before we kill them!")
    time.sleep(3)
    print("...")
    time.sleep(1)
    print("Creature: Ooops. I mean others. They do the killing. I don't like humans. ")
    time.sleep(5)
    print("You: Well, that's comforting, I guess...")
    time.sleep(3)
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
    time.sleep(4)
    print("You: Uhhh, hello? Who is this? ")
    time.sleep(3)
    print("A familiar famous figure turns his chair around.")
    time.sleep(3)
    print("It's no one other than 21 Savage in the flesh!")
    time.sleep(3)
    print("You: Wh- you!?")
    time.sleep(3)
    print("21: Hey there, $&%^@. What's a lil kid doin in this castle? This a dangerous place.")
    time.sleep(3)
    print("You: Can we not swear? This is a school assignment.")
    time.sleep(3)
    print("21: My apologies, kid. But how the hell did you get in here? Dey gonna kill ya!")
    time.sleep(4)
    print("You: I accidentally took a one-way train here. I need to find my way home!")
    time.sleep(3)
    print("21: Aw, man, this the fifth time this week! And four of em didn't make it!")
    time.sleep(3)
    print("You: Aaaah!")
    time.sleep(2)
    print("21: Don't be scared, lil kid, I can see it in your eyes. You gonna make it out alive!")
    time.sleep(3)
    print("You: Really? You think so?")
    time.sleep(3)
    print("21: I dunno. I'm tryna be motivational here.")
    time.sleep(3)
    print("You: Well, that's flattering...")
    time.sleep(2)
    print("You: How did you end up in here? It's really odd seeing you out of all people in this room.")
    time.sleep(4)
    print("""21: Well, they was gonna send me back to the UK, but I ain't want that, so I ended up fleeing on the same train you took.
    Luckily, the monstas recognized me, and now I live here. It's a real bad place, these monstas will find anyone and eat em alive! Tougher
    than Zone 6! And all they feed me is proscuitto. That s**t stretchy as hell, I'm sick of it.""")
    time.sleep(7)
    print("You: Oh, so that's where you went. It doesn't seem good here, and besides, a lot of people miss you, dude.")
    time.sleep(4)
    print("21: I realize dat, but a life without fame is a lot more quiet, so here I am.")
    time.sleep(4)
    print("You: That makes sense... so, do you know how to get out of this place?")
    time.sleep(4)
    print("21: Hell yeah I do. But it ain't gonna be easy. You gotta get to the top floor of dis castle.")
    print("21: There are two floors to go afta this one. Once you at the top there should be a portal back to the train station.")
    print("21: On your way, you gonna meet some nasty creatures, tho. I advise you watch yo back!")
    time.sleep(20)
    print("You: Oh no, what kind of creatures?")
    time.sleep(4)
    print("21: I cannot say, it's too violent. Mr. Shaft will take marks off.")
    time.sleep(4)
    print("Ugh, fine. I'll find out when the time comes but I'm sure it won't be pretty.")
    time.sleep(4)
    print("You: 21: The door behind me is the way to the second floor. It's a hospital, fulla sick creatures.")
    time.sleep(4)
    print("You: ...That's kind of sad. What type of diseases?")
    time.sleep(4)
    print("21: Mostly scurvy. They don't eat no fruit. I been tryna get them to take supplements but they don't know what dat is.")
    print("21: Regardless, you gon have to find a special weapon to break down the barrier to floor three. It's in dat hospital.")
    time.sleep(15)
    print("You: Alright, thank you. ")
    time.sleep(3)
    print("21: Good luck on your travels, child, and I hope you make it back in one piece.")
    time.sleep(4)
    print("You: Didn't think I'd have someone say that to me, but thanks...")
    breakAfterConversation()

def breakRoom():
    print("You're in the break room.")
    time.sleep(1)
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
    time.sleep(1)
    print("You come across a door. You look through, and it's a few creatures having a business meeting.")
    time.sleep(3)
    print("Best not disturb them...")
    time.sleep(2)
    print("You continue creeping to the left... and you come across a break room.")
    time.sleep(3)
    print("The door is unlocked, so you decide to open it. There's a friendly creature sitting there, and a shadowy figure in the chair at a desk.")
    breakRoom()

def tryLeaving():
    print("You try to open the castle door behind you quietly.")
    time.sleep(3)
    print("It doesn't budge. You're stuck.")
    time.sleep(2)
    castleOptions()

def walkMiddle():
    print("You step into the middle of the castle foyer...")
    time.sleep(3)
    print("You die! The guarding monsters don't like intruders.")
    deathAftermath()

def tryUnlock():
    print("You try unlocking the door...")
    time.sleep(3)
    print("There's no keyhole! No way out!")
    global triedUnlocking
    triedUnlocking = True
    castleOptions()

def enterCastle():
    print("You enter the castle ever-so-carefully. You're in the foyer now, and there are multiple creatures guarding a big staircase.")
    time.sleep(2)
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
    time.sleep(2)
    print("You: I fell asleep on a train and got off here. Any way I can get out?")
    time.sleep(2)
    print("Creature: Sorry, kiddo. That's a one-way stop. They only let people get off that train, not on.")
    time.sleep(2)
    print("You: Okay, you're kidding with me, right?")
    time.sleep(2)
    print("Creature: Nope. I wish I was.. this place is less than ideal to be around.")
    time.sleep(2)
    print("You: Huh? What do you mean?")
    time.sleep(2)
    print("Creature: Aw, crap, I've said too much. You go on with your day now, I'll let you find out...")
    time.sleep(2)
    print("You: Uhh... okayyy?")
    print("You return back to where you started.")
    introOptions()

def railway():
    print("You go back to the railway and wait a little...")
    time.sleep(3)
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
    print("Oh no! After falling asleep on the train back home, you accidentally got off a stop at some sort of castle.")
    introOptions()
            
intro()