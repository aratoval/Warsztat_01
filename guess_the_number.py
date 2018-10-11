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
                    "Zgadnij liczbę z zakresu [{}, {}], {} próba: ".format(
                            mins, maxs, counter)))

            if (10 * answer) % 10 != 0 or answer < 0:
                counter -= 1
                print("Podaj liczbę naturalną z zakresu [{}, {}]".format(mins, maxs))
            elif answer < mins or answer > maxs:
                counter -= 1
                print("Podaj liczbę z zakresu [{}, {}]".format(mins, maxs))
            else:
                answer = int(answer)
                if answer == guess:
                    print("Zgadłeś!")
                elif answer > guess:
                    print("Za dużo!")
                elif answer < guess:
                    print("Za mało!")

        except ValueError:
            counter -= 1
            print("To nie jest liczba.")


game()
