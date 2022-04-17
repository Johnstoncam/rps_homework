from models.player import Player

choices_list = ["rock", "paper", "scissors"]

def game(player1, player2):    

    if player1.choice in choices_list and player2.choice in choices_list:

        if player1.choice != player2.choice:
            
            while player1.choice == "rock":
                if player2.choice == "scissors":
                    return player1
                return player2
                
            while player1.choice == "paper":
                if player2.choice == "rock":
                    return player1
                return player2
            
            while player1.choice == "scissors":
                if player2.choice == "paper":
                    return player1
                return player2
            
        return None

    return "Choose: rock, paper or scissors."