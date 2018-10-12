from random import randint


def dice(type_dice):
    correct_dice_value = [3, 4, 6, 8, 10, 12, 20, 100]

    if "D" in type_dice.upper():
        how_many, other = type_dice.upper().split("D")
    else:
        raise ValueError("Format error")

    if "-" in how_many:
        raise ValueError("Value error")

    elif how_many == "":
        how_many = 1

    else:
        how_many = int(how_many)

    if "+" in other:
        dice_value, modifier = other.split("+")
        dice_value = int(dice_value)
        modifier = int(modifier)

    elif "-" in other:
        dice_value, modifier = other.split("-")
        dice_value = int(dice_value)
        modifier = -int(modifier)

    else:
        dice_value = int(other)
        modifier = 0

    if dice_value in correct_dice_value:
        roll = sum([randint(1, dice_value) for i in range(how_many)]) + modifier
    else:
        raise TypeError("Dice type error")

    return roll


if __name__ == "__main__":
    testing_list = ["d3", "2d3", "1d3", "d3+2", "d100-10", "2d12+33", "d3-4", "k2", "-2D+1", "d7"]
    for i in testing_list:
        try:
            print(dice(i))
        except Exception as e:
            print(e)
