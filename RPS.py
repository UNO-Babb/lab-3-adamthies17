#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play = "Y"
  while play == "Y":
    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    #Ask the user if they would like to play again.

    player = input("Choose rock, paper, or scissors (R/P/S): ")

    computer = random.choice( ["R", "P", "S"] )

    if player == computer:
      print("TIE")
      ties = ties + 1
    elif player == "R" and computer == "S":
      print("Dang, you won. I chose S.")
      wins = wins + 1
    elif player == "R" and computer == "P":
      print("Ha! You lost dude. I chose P!")
      losses = losses + 1
    elif player == "P" and computer == "R":
      print("Dang, you won. I chose R.")
      wins = wins + 1
    elif player == "P" and computer == "S":
      print("You lost dude. I chose S.")
      losses = losses + 1
    elif player == "S" and computer == "P":
      print("Dang, you won. I chose P.")
      wins = wins + 1
    elif player == "S" and computer == "R":
      print("Loser! I chose R!")
      losses = losses + 1
    else:
      print("Invalid choice.")
    play = input("Play again? (Y/N): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
