import random

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "not the competitor!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "Yay you win!"
    else:
        return "sorry!"
def play_game():
    print("Welcome to the Game!")
    
    user_choice = input("Enter your choice : ")
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice")
        user_choice = input("Enter your choice: ")
    
    comp_choice = computer_choice()
    print(f"Computer chose: {comp_choice}")
    result = determine_winner(user_choice, comp_choice)
    print(result)

if __name__ == "__main__":
    play_game()
