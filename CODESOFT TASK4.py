import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("Choose one: rock, paper, or scissors")
        
        user_choice = input("Your choice: ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again: rock, paper, or scissors")
            user_choice = input("Your choice: ").lower()
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'user':
            print("You win!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nFinal Score")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("Thank you for playing!")

# Run the main function
if __name__ == "__main__":
    main()
