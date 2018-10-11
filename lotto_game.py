from random import shuffle


def lotto_game():
    user_number_list = []
    lotto_number = [i for i in range(1, 50)]
    shuffle(lotto_number)
    lotto_number =lotto_number[:6]

    while len(user_number_list) < 6:

        try:

            user_number = input("Podaj {} liczbę: ".format(len(user_number_list)+1))
            user_number = int(str(user_number))

            if user_number < 1:
                print("Liczba za mała!")
            elif user_number > 49:
                print("Liczba za duża!")
            elif user_number in user_number_list:
                print("Taka liczba została już podana!")
            else:
                user_number_list.append(user_number)

        except ValueError:
            print("To nie jest liczba!")

    user_number_list.sort()
    print("Twoje liczby to: ", user_number_list)
    print("Wylosowane liczby to: ", lotto_number)

    hits = 0
    for i in user_number_list:
        if i in lotto_number:
            hits += 1



    if hits > 2:
        print("Ilość trafień {}".format(hits))

lotto_game()
