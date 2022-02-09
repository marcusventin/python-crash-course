from random import randint

class Dice:
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)

die = Dice()

die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()