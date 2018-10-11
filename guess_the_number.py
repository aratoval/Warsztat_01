#!/usr/bin/env python3

from random import randint


def game():

    guess = randint(1, 100)
    answer = 0

    while answer != guess:

        try:
            answer = input("Zgadnij liczbę: ")
            answer = int(str(answer))  # zabezpieczenie przed liczbami rzeczywistymi
            if answer == guess:
                print("Zgadłeś!")
            elif answer > guess:
                print("Za dużo!")
            elif answer < guess:
                print("Za mało!")

        except ValueError:
            print("To nie jest liczba.")


game()
