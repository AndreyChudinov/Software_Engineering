import random


def roll_dice():
    dice_value = random.randint(1, 6)

    print(f"Значение кубика: {dice_value}")

    if dice_value == 5 or dice_value == 6:
        print("Вы победили")
    elif dice_value == 3 or dice_value == 4:
        print("Повторный бросок...")
        roll_dice()
    else:
        print("Вы проиграли")


if __name__ == '__main__':
    roll_dice()