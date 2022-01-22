# Dice Game

import random

class Die():

    def __init__(self):
        self.value = 1
    
    def roll(self):
        self.value = random.randint(1,6)  

    def get_die_value(self):
        return self.value

class Player():
    
    def __init__(self):
        self.score = 0

    def roll_dice(self, dice):
        for die in dice:
            die.roll()
    
    def score_dice(self, dice):
        for die in dice:
            if die.get_die_value() == 1:
                self.score += 100
            if die.get_die_value() == 5:
                self.score += 50
        
    def show_dice(self, dice):
        dice_string = "You rolled:"
        for die in dice:
            dice_string += " "
            dice_string += str(die.get_die_value())
        print(dice_string)

    def show_score(self):
        print("Your score is: {}".format(self.score))

    def any_scoring_dice(self, dice):
        scoring_dice = 0
        for die in dice:
            if die.get_die_value() == 1:
                scoring_dice += 1
            if die.get_die_value() == 5:
                scoring_dice += 1
        return(scoring_dice > 0)


def main():
    die1 = Die()
    die2 = Die()
    die3 = Die()
    die4 = Die()
    die5 = Die()
    
    mydice = []
    mydice.append(die1)
    mydice.append(die2)
    mydice.append(die3)
    mydice.append(die4)
    mydice.append(die5)

    myself = Player()

    roll_again = input("Roll dice? [y/n] ")


    while (roll_again == "y"):
        myself.roll_dice(mydice)
        myself.show_dice(mydice)
        myself.score_dice(mydice)
        myself.show_score()
        if (not myself.any_scoring_dice(mydice)):
            break
        roll_again = input("Roll dice? [y/n] ")



if __name__ == "__main__":
    main()
    