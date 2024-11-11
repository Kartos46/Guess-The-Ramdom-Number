import random

# Generate a random target number between 1 and 100
target = random.randint(1, 100)

while True:
    # Get user input
    userChoice = input("Guess the target or type 'quit' to exit: ")
    
    # Check if user wants to quit
    if userChoice.lower() == "quit":
        break

    # Convert user input to an integer for comparison
    try:
        userChoice = int(userChoice)
    except ValueError:
        print("Please enter a valid number or 'quit' to exit.")
        continue

    # Check if the guess is correct, too low, or too high
    if userChoice == target:
        print("Success: Correct Guess!")
        break
    elif userChoice < target:
        print("Your guess was too small. Try a bigger number.")
    else:
        print("Your guess was too big. Try a smaller number.")

print("----------------Game Over---------------")
