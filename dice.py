from random import randint


def dice(type_dice):
    correct_dice_value = [3, 4, 6, 8, 10, 12, 20, 100]

    how_many, other = type_dice.upper().split("D")

    if how_many == "":
        how_many = 1

    else:
        how_many = int(how_many)

    if "+" in other:
        dice_value, correction = other.split("+")
        dice_value = int(dice_value)
        correction = int(correction)

    elif "-" in other:
        dice_value, correction = other.split("-")
        dice_value = int(dice_value)
        correction = -int(correction)

    else:
        dice_value = int(other)
        correction = 0

    roll = sum([randint(1, dice_value) for i in range(how_many)]) + correction

    return roll


if __name__ == "__main__":
    testing_list = ["d3", "2d3", "1d3", "d3+2", "d100-10", "2d12+33", "d3-4"]
    for i in testing_list:
        print(dice(i))
