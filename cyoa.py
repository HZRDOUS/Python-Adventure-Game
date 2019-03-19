import time

name = ""
inventory = []

def printOutInventory():
    global inventory
    print("You have the following things in your inventory:")
    for item in inventory:
        print(f'- {item}')
    print("-" * 30 + "\n")

# inventory.append("Porscuitto")

def deathAftermath():
    while True:
        print("""
        1. Replay
        2. Quit""")
        tryAgain = int(input("Try again?? >> "))
        if tryAgain == 1:
            intro()
        elif tryAgain == 2:
            break
        else:
            print("Bad input!")
            continue

def rightEdge():
    print("You decide to sneak on the right.")
    time.sleep(1)
    print("You come across a door. You look inside.")
    print("The creatures are having lunch in the cafeteria...")
    time.sleep(2)
    print("")

def leftEdge():
    print("huifeie")

def tryLeaving():
    print("You try to open the castle door behind you quietly.")
    time.sleep(3)
    print("It doesn't budge. You're stuck.")
    enterCastle().castleOptions()

def walkMiddle():
    print("You step into the middle of the castle foyer...")
    time.sleep(3)
    print("You die! The guarding monsters don't like intruders.")
    deathAftermath()


def enterCastle():
    print("You enter the castle ever-so-carefully. You're in the foyer now, and there are multiple creatures guarding a big staircase.")
    time.sleep(2)
    print("You think to yourself that you should probably be very quiet and sneaky if you're going to get out successfully.")
    def castleOptions():
        while True:
            print("""
            1. Go back out of the castle.
            2. Walk to the middle of the room and ignore your instincts.
            3. Creep around the right edge of the room.
            4. Creep around the left edge of the room.""")
            option = int(input("What do you want to do?"))
            if option == 1:
                tryLeaving()
            elif option == 2:
                walkMiddle()
            elif option == 3:
                rightEdge()
            elif option == 4:
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
    intro().introOptions()

def railway():
    print("You go back to the railway and wait a little...")
    time.sleep(3)
    print("No trains! You give up and head back to the front of the castle.")
    intro().introOptions()

def intro():
    print("Oh no! After falling asleep on the train back home, you accidentally got off a stop at some sort of castle.")
    def introOptions():
        while True:
            print("""
            1. Go back to the railway to find a way home.
            2. Talk to a bystanding creature
            3. Go up to the castle steps and enter.""")
            option = int(input("What do you want to do? >>"))
            if option == 1:
                railway()
            elif option == 2:
                talk1()
            elif option == 3:
                enterCastle()
            else:
                "Invalid option. Try again."
            continue
    

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
        door = int(input("Which door do you want to go through? >>"))
        if door == 1:
            secondFloorDoor1()
        elif door == 2:
            secondFloorDoor2()
        elif door == 3:
            hospital()
        else:
            print("Invalid option.")
            continue

    
def savage21():
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
    print("You: Aww, that's kind of sad. What type of diseases?")
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
            time.sleep(8)
            print(f"{name}: Yep... let's get out of here.")
            time.sleep(4)
            print("With your newfound team member, you open the door to the next floor with confidence in getting out of this place.")
            secondFloor()
        else:
            continue


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
            
savage21()