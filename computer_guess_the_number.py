def game():

    print("Think of a number from 0 to 1000, and I will guess it in max. 10 attempts!")
    answer = ""

    mins = 0
    maks = 1000
    counter = 0
    answer_list = ["you guessed", "less", "more"]

    while answer != answer_list[0]:

        counter += 1
        guess = int((maks - mins) / 2) + mins
        print("List of words {}".format(answer_list))
        print("{} attempt, I'm guessing: {}".format(counter, guess))
        answer = input()

        if answer == answer_list[0]:
            print("I win!")

        elif answer == answer_list[1]:
            maks = guess

        elif answer == answer_list[2]:
            mins = guess

        else:
            print("Do not cheat!")


game()
