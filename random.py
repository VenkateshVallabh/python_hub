import random

# List of players
players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

# Randomly select the imposter
imposter = random.choice(players)

# Game loop
while True:
    # Display the players
    print("Players:")
    for player in players:
        print(player)
    print()

    # Prompt the user to vote
    vote = input("Who do you want to vote off? ")

    # Check if the voted player is in the list of players
    if vote in players:
        # Check if the voted player is the imposter
        if vote == imposter:
            print("Congratulations! You caught the imposter!")
            break
        else:
            print("Oops! That player is not the imposter.")
            players.remove(vote)
    else:
        print("Invalid player. Please try again.")

    # Check if there are any players left
    if len(players) == 1:
        print("Game over! The imposter won.")
        break
