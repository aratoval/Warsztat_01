#!/usr/bin/env python3

from random import randint


def game():

    mins = 1
    maxs = 100
    guess = randint(mins, maxs)
    answer = 0

    while answer != guess:

        try:
            answer = float(input("Zgadnij liczbę z zakresu [{}, {}]: ".format(mins, maxs)))
#            answer = int(str(answer))  # zabezpieczenie przed liczbami rzeczywistymi
            if (10 * answer) % 10 == 0:
                answer = int(answer)
                if answer == guess:
                    print("Zgadłeś!")
                elif answer > guess:
                    print("Za dużo!")
                elif answer < guess:
                    print("Za mało!")
            else:
                print("Podaj liczbę naturalną z zakresu [{}, {}]".format(mins, maxs))

        except ValueError:
            print("To nie jest liczba.")


game()
