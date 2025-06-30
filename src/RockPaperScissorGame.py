import random

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game rules"""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def get_user_choice():
    """Prompt user for valid input"""
    while True:
        user_input = input("Your choice (rock/paper/scissors): ").lower().strip()
        if user_input in ("rock", "paper", "scissors", "r", "p", "s"):
            return {"r": "rock", "p": "paper", "s": "scissors"}.get(user_input[0], user_input)
        print("Invalid choice. Please enter rock, paper, or scissors.")

def main():
    user_score = 0
    computer_score = 0
    
    print("=" * 40)
    print("ROCK-PAPER-SCISSORS GAME".center(40))
    print("=" * 40)
    print("Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beat Paper")
    print("- Paper beats Rock")
    print("- Same choice is a tie")
    print("=" * 40)
    
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = determine_winner(user_choice, computer_choice)
        
        print("\n" + "=" * 40)
        print(f"Your choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        print("-" * 40)
        
        if result == "tie":
            print("It's a TIE!")
        elif result == "user":
            print("You WIN! 🎉")
            user_score += 1
        else:
            print("Computer WINS! 🤖")
            computer_score += 1
            
        print(f"\nScore: You {user_score} | Computer {computer_score}")
        print("=" * 40)
        
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again not in ("y", "yes"):
            print("\n" + "=" * 40)
            print("FINAL SCORE:".center(40))
            print(f"You: {user_score}".center(40))
            print(f"Computer: {computer_score}".center(40))
            print("\nThanks for playing! Goodbye 👋")
            print("=" * 40)
            break

if __name__ == "__main__":
    main()