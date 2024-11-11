1. Import and Set Target:

python Code:-

import random
target = random.randint(1, 100)

•This imports the random module, which is used to generate random numbers.
•target is set to a random integer between 1 and 100. This is the number the user will try to guess.

2. Loop for User Input:

python Code:- 

while True:
    userChoice = input("Guess the target or type 'quit' to exit: ")

•The program enters a while loop that keeps running until the user either guesses the number or types "quit" to stop.
•input() prompts the user to enter a guess or type "quit" to exit.

3. Check for Quit Option:

python Code:-

if userChoice.lower() == "quit":
    break

•If the user inputs "quit" (in any case), the loop breaks, and the game ends.

4. Convert Input and Handle Errors:

python Code:-

try:
    userChoice = int(userChoice)
except ValueError:
    print("Please enter a valid number or 'quit' to exit.")
    continue

•The program tries to convert userChoice to an integer.
•If the input is not a valid number, it throws a ValueError, prints an error message, and prompts the user again without exiting the game.

5. Check Guess Against Target:

python Code:-

if userChoice == target:
    print("Success: Correct Guess!")
    break
elif userChoice < target:
    print("Your guess was too small. Try a bigger number.")
else:
    print("Your guess was too big. Try a smaller number.")

•If userChoice matches target, the user has guessed correctly, and the program prints a success message and breaks the loop.
•If userChoice is less than target, the program informs the user that the guess is too low.
Otherwise, if userChoice is greater than target, the program informs the user that the guess is too high.

6. Game Over:

python Code:-

print("----------------Game Over---------------")

•After the user guesses correctly or chooses to quit, the game prints a "Game Over" message.
