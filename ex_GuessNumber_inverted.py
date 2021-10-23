"""
Let the user think of a number in the range 1-1000 and the computer will keep guessing. He will do this in 
a maximum of 10 moves (provided the player is not cheating).

The player's task will be to answer "Too small", "Too big" or "You win".

"""

print("Think about a number from 0 to 1000. I'll find it out in max 10 guesses. Press Enter")
min_guess = 0
max_guess = 1000


try:
    while True:
        guess = int((max_guess - min_guess) / 2) + min_guess
        print("Is it", guess, "?")
        print("""Your answer:
          1 - too big
          2 - too small
          3 - you guessed correctly!
              """)


        user_answer = int(input())

        if user_answer == 3:
           print("I won!")
           break
        else:

            if user_answer == 1:
                max_guess = guess - 1
                if min_guess > max_guess:
                    print("You are cheating")
                else:
                    pass

            elif user_answer == 2:
                min_guess = guess + 1
                if min_guess > max_guess:
                    print("You are cheating")
                else:
                    pass
except ValueError:
    print("Only numbers please!")








