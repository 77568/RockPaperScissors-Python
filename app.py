import random
while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    possible_choices = ["rock", "paper", "scissors"]
    if user_choice not in possible_choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(possible_choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win! Rock smashes scissors. 🎉")
        else:
            print("You lose! Paper covers rock. 😞")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win! Paper covers rock. 🎉")
        else:
            print("You lose! Scissors cuts paper. 😞")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win! Scissors cuts paper. 🎉")
        else:
            print("You lose! Rock smashes scissors. 😞")
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break