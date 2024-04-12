import random

class RockPaperScissors:
    def __init__ (self, ):
        self.choices = ["rock", "paper", "scissors"]

    def get_player_choice(self):
        player_choice = (input(f"Please enter your choice ({self.choices}) > ")).lower()
        if player_choice in self.choices:
            print(f"Your choice: {player_choice}")
            return player_choice
        print("Please enter a valid choice.")
        return self.get_player_choice()
    
    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        print(f"computer_choice: {computer_choice}")
        return computer_choice
    
    def decide_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a Tie!"
        
        win_situations = (["rock", "scissors"], ["scissors", "paper"], ["paper", "rock"])
        for situation in win_situations:
            if player_choice == situation[0] and computer_choice == situation[1]:
                return "congratulations! You won!!!!"
        return "Sorry, You lost..."
    
    def play(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print("\n")
        print(self.decide_winner(player_choice, computer_choice))
        print("\n")


game = RockPaperScissors()
while True:
    game.play()
    
    continue_game = input ("Do you want to play again? Press any key to continue or press 'q' to quit the game. > ")
    if continue_game.lower() == "q" :
        print("\n")
        break
    else:
        print("\n")
        continue