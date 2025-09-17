import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    
    # Define the winning rules
    if (user == 'rock' and computer == 'scissor') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissor' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock Paper Scissor Game!")
    print("Choices: rock, paper, scissor")

    while True:
        user_choice = input("\nEnter your choice (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print("Thanks for playing. Goodbye!")
            break

        if user_choice not in ['rock', 'paper', 'scissor']:
            print("Invalid choice. Please choose rock, paper, or scissor.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
