import time

def railway():
    print("You go back to the railway and wait a little...")
    time.sleep(3)
    print("No trains! You give up and head back to the front of the castle.")
    intro().introOptions()

def intro():
    print("Oh no! After falling asleep on the train back home, you accidentally got off a stop at some sort of castle.")
    def introOptions():
        while True:
                print("""1. Go back to the railway to find a way home.
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
    introOptions()
intro()