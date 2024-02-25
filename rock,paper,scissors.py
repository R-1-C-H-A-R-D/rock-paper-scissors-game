import random

options = ("rock","paper","scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock,paper,scissors): ")

    print (f"Player: {player}")
    print (f"Computer: {computer}")

    if player == computer:
        print ("It's a draw")
    elif player == "rock" and computer == "scissors":
        print ("You win!!!")
    elif player == "paper" and computer =="rock":
        print ("You win!!!")
    elif player == "scissors" and computer == "paper":
        print ("You win!!!")
    else:
        print ("You lose!!!")
    
    play_again = input ("Want to play again?? (yes or no): ").lower()

    if not play_again == "yes":
        running = False

print ("Thank you for playing, have a nice day.")

