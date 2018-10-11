#!/usr/bin/env python3

from random import randint


def game():

    mins = 1
    maxs = 100
    guess = randint(mins, maxs)
    answer = 0
    counter = 0

    while answer != guess:

        counter += 1
        try:
            answer = float(input(
                    "Guess the number in the range [{}, {}], {} attempt: ".format(
                            mins, maxs, counter)))

            if (10 * answer) % 10 != 0 or answer < 0:
                counter -= 1
                print("Enter a natural number in the range [{}, {}]".format(mins, maxs))
            elif answer < mins or answer > maxs:
                counter -= 1
                print("Enter a number in the range [{}, {}]".format(mins, maxs))
            else:
                answer = int(answer)
                if answer == guess:
                    print("You guessed!")
                elif answer > guess:
                    print("Too much!")
                elif answer < guess:
                    print("Too small!")

        except ValueError:
            counter -= 1
            print("This is not a number.")


game()
