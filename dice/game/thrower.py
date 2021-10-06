import random

# TODO: Define the Thrower class here.

class thrower:

    def __init__(self):
        
        self.dice = []


    # you will need function called 'throw_dice()'
    def throw_dice(self):

        self.dice.clear()
        self.dice.append(random.sample(range(1,6), 5)) 
        

    # you will need function called 'get_points()'
    def get_points(self):

        points = 0

        if self.rolls == 1:
            points += 100
        elif self.rolls == 5:
            points += 50

        return points
        

    # you will need function called 'can_throw()'
    def can_throw(self):

        if 1 in self.rolls:

    