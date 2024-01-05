"""
DND Dice Simulator

This program simulates rolling dice for DND.
Multiple dices available for rolling.
"""
import random


DICES = {
    'd4': 4,
    'd6': 6,
    'd8': 8,
    'd10': 10,
    'd12': 12,
    'd20': 20,
    'd100': 100
}

def get_input():
    """
    This function gets the user's input number.
    :return: The user's input number.
    """
    while True:
        print(f"Available dices: {', '.join(DICES.keys())}")
        try:
            user_input = input("Enter dice to roll: ")
            if user_input in DICES.keys():
                return user_input
            else:
                print("No such dice type. Please, select from the list below:")
        except ValueError:
            print("Please enter a valid number.")


def roll_dice(dice_type: str):
    """
    This function generates a random number between the min and max values.
    :param dice_type: Dice key from DICES dict. Dict contains max value for each dice.
    :return: The random number.
    """
    return random.randint(1, DICES[dice_type])


def main():
    dice_type = get_input()
    print(f"Rolling {dice_type}...")
    print(f"You rolled {roll_dice(dice_type)}.")


if __name__ == "__main__":
    main()
