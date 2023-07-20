import random
def play_game():
    lowest = 1
    highest = 10
    max_guesses = 5
    hidden_num = random.randint(lowest, highest)

    print(f"pick a number between the range 1 to 10.")

    for guess_count in range(max_guesses):
        guess = int(input("enter a number to start the game: "))

        if guess < hidden_num:
            print("Too low")
        elif guess > hidden_num:
            print("Too high")
        else:
            print(f"You find it right in {guess_count + 1} try ")
            return

    print(f"Sorry, you ran out of guesses the desired number was {hidden_num}, if you want to continue please rerun "
          f"the programme.")


play_game()
