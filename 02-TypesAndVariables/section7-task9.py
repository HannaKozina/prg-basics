import random

dice_roll = random.randint(1,6)
print(dice_roll)

dice_roll_special = dice_roll == 1 or dice_roll == 6

print(dice_roll_special)