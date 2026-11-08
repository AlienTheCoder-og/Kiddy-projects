import time

def nearestMultiple(num):
    if num >= 4:
        num = num + (4 - (num % 4))
    else:
        num = 4
    return num

def lose():
    print("\nYou Lose!")
    print("Game over!")
    exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if xyz[i] - xyz[i - 1] != 1:
            if xyz[i] - xyz[i - 1] == 0 or xyz[i] - xyz[i - 2] == 0:
                return True
            return False
        i += 1
    return True

def checkSimilarity(xyz):
    i = 1
    while i < len(xyz):
        if xyz[i] - xyz[i - 1] == 0 or xyz[i] - xyz[i - 2] == 0:
            return True
        i += 1
    return False

def start():
    xyz = []
    last = 0

    while True:
        print("\nTo take the first turn, type 'F'")
        print("To take the second turn, type 'S'")
        user_choice = input("> ")
        if user_choice.lower() == "f":
            while True:
                if last == 20:
                    lose()

                print("Your turn.")
                inp = int(input("How many numbers would you like to enter? (1-3)\n> "))

                if 1 <= inp <= 3:
                    comp = 4 - inp
                else:
                    print("You have disrespected the rules, hence you are disqualified!")
                    lose()

                for i in range(inp):
                    xyz.append(int(input(f"Enter your number number {i+1}: ")))

                print(xyz)
                last = xyz[-1]

                if not (check(xyz)):
                    print("Oh buddy, ya shouldn't have cheated...")
                    time.sleep(1)
                    lose()

                if checkSimilarity(xyz):
                    for i in range(inp):
                        del xyz[-1]
                    if len(xyz) == 0:
                        last = 0
                    else:
                        last = xyz[-1]
                    comp = 4
                    print("\nNow you will get rekt for not succumbing to the rules.")

                if last == 21:
                    lose()

                print("\nComputer's turn.")
                time.sleep(1)
                for i in range(1, comp+1):
                    xyz.append(last + i)

                print("Numbers after computer's turn:", xyz)
                last = xyz[-1]


        elif user_choice.lower() == "s":
            comp = 1
            last = 0

            while last < 20:
                print("\nComputer's turn...")
                time.sleep(1)
                for i in range(1, comp + 1):
                    xyz.append(last + i)

                print("Numbers after computer's turn:", xyz)

                if xyz[-1] == 20:
                    lose()

                print("Your turn.")
                inp = int(input("How many numbers would you like to enter? (1-3)\n> "))

                if not(1 <= inp <= 3):
                    print("You have disrespected the rules, hence you are disqualified!")
                    lose()

                for i in range(inp):
                    xyz.append(int(input(f"Enter your number number {i+1}: ")))

                if not check(xyz):
                    print("Oh buddy, ya shouldn't have cheated...")
                    time.sleep(1)
                    lose()

                if checkSimilarity(xyz):
                    for i in range(inp):
                        del xyz[-1]
                    print("\nNow you will get rekt for not succumbing to the rules.")

                last = xyz[-1]

                near = nearestMultiple(last)
                comp = near - last

                if comp == 4:
                    comp = 3

            print("\n\nCONGRATULATULATIONS!!! \nYOU WON!")
            exit(0)

        else:
            print("Wrong choice. Please enter F or S")

game = True
while game:
    ans = input("Would you like to play a game of 21 number? (yes/no): ")
    if ans.lower() == 'yes':
        start()

    elif ans.lower() == 'no':
        next_ans = input("Would you like to quit the game? (yes/no): ")
        if next_ans.lower() == 'yes':
            exit(0)
        elif next_ans.lower() == 'no':
            continue
        else:
            print("\nIncorrect choice. Please enter correct answer (yes/no).\n")
            continue

    else:
        print("\nIncorrect choice. Please enter correct answer (yes/no).\n")
        continue