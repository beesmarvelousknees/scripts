'''
The Monty Hall Problem
See movie '21' for reference.
'''
import random

# Track the total number of game plays.
games_played = 0

# Track the total number of cars won.
cars_won = 0

# Play the game 10000 times
while games_played < 10000:

    # Setup doors and shuffle the rewards.
    doors = ["Goat", "Goat", "Car"]
    random.shuffle(doors)

    # I always choose the first door.
    my_choice = doors[0]

    # Remove one Goat.
    i = 1
    while i < len(doors):
        if doors[i] == "Goat":
            del doors[i]
            break
        i += 1

    # Switch my choice
    my_choice = doors[1]

    # Increment the number of games played.
    games_played += 1

    # Check if won car, if so increment number of cars won.
    if my_choice == "Car":
        cars_won += 1

# When the desired number of games have been played, check car win %
percent_won = cars_won / games_played * 100
print(f"You won the car {percent_won}% of the time!")


