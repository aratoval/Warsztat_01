def game():

    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")
    answer = ""

    mins = 0
    maks = 1000
    counter = 0

    while answer != "zgadłeś":

        counter += 1
        guess = int((maks - mins) / 2) + mins
        print("Próba {}, zgaduję: {}".format(counter, guess))
        answer = input()

        if answer == "zgadłeś":
            print("Wygrałem!")

        elif answer == "za dużo":
            maks = guess

        elif answer == "za mało":
            mins = guess

        else:
            print("nie oszukuj!")


game()
