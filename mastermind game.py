import random

attempts = 0
secret_num = random.randint(1000, 100000)
correct = ['X'] * 5

print("Welcome to BRAIN RING!!!")
print("Guess the correct secret number(length of 5).")

while True:
    try:
        guess = int(input())
        if 1000 > guess > 99999:
            print("Your guess is just wrong, the number is a 5-digit one.")
            continue

    except ValueError:
        print("Please enter numerical values only.")
        continue

    attempts += 1

    if guess == secret_num:
        print("Congratulations! You guessed the secret number correctly!")
        print(f"It took you only {attempts} tries!")
        break

    guess_str = str(guess)
    secret_str = str(secret_num)

    count = 0

    if len(guess_str) != 5:
        print("Your guess is wrong. Choose another.")
        continue

    for i in range(5):
        if guess_str[i] == secret_str[i]:
            count += 1
            correct[i] = guess_str[i]

    if count == 1:
        print(f"Not quite the right number, you did get {count} digit correctly.")
    else:
        print(f"Not quite the right number, you did get {count} digits correctly.")

    print("Correctly placed digits as of now:")
    print(" ".join(correct))

    print()


