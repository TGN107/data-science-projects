import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    score = {'player': 0, 'computer': 0}

    while True:
        print(f"\nScore - You: {score['player']}  Computer: {score['computer']}")
        player_choice = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if player_choice == 'q':
            print("\nFinal Score:")
            print(f"You: {score['player']}  Computer: {score['computer']}")
            print("Thanks for playing!")
            break
            
        if player_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif wins[player_choice] == computer_choice:
            print("You win!")
            score['player'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()