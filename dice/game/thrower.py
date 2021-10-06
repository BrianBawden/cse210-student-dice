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
        points = self.dice.count(1) * 100 + self.dice.count(5) * 50

        return points
        

    # you will need function called 'can_throw()'
    def can_throw(self):

        if 1 in self.dice or 5 in self.dice:
            return True
        else:
            return False

    