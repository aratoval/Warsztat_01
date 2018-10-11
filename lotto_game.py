from random import shuffle


def lotto_game():
    user_number_list = []
    lotto_number = [i for i in range(1, 50)]
    shuffle(lotto_number)
    lotto_number =lotto_number[:6]

    while len(user_number_list) < 6:

        try:

            user_number = float(input(
                    "Enter the {} number from the range [1, 49]: ".format(
                            len(user_number_list)+1)))

            if user_number < 1:
                print("The number is too small!")
            elif user_number > 49:
                print("The number is too big!")
            elif user_number in user_number_list:
                print("Such number has already been given!")
            elif (10 * user_number) % 10 != 0:
                print("Enter a natural number between [1, 49]!")
            else:
                user_number_list.append(int(user_number))

        except ValueError:
            print("This is not a number!")

    user_number_list.sort()
    lotto_number.sort()
    print("\nYour numbers are:    {}".format(user_number_list))
    print("The numbers drawn are: {}".format(lotto_number))

    hits = 0
    for i in user_number_list:
        if i in lotto_number:
            hits += 1

    if hits > 2:
        print("Number of hits: {}".format(hits))


if __name__ == "__main__":
    lotto_game()
