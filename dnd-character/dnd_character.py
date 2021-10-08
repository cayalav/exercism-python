import random


def best_3_of_4():
    rolls = [0] * 4

    for i in range(0, 3):
        rolls[i] = random.randint(1, 6)

    rolls.sort()

    return rolls[1] + rolls[2] + rolls[3]



def modifier(num):
    return int((num - 10) // 2)



class Character:


    def __init__(self):
        self.strength     = best_3_of_4()
        self.dexterity    = best_3_of_4()
        self.constitution = best_3_of_4()
        self.intelligence = best_3_of_4()
        self.wisdom       = best_3_of_4()
        self.charisma     = best_3_of_4()

        self.hitpoints = 10 + modifier(self.constitution)

        pass


    def ability(self):
        ability_ID = random.randint(1, 6)
        if   ability_ID == 1:    return self.strength
        elif ability_ID == 2:    return self.dexterity
        elif ability_ID == 3:    return self.constitution
        elif ability_ID == 4:    return self.intelligence
        elif ability_ID == 5:    return self.wisdom
        elif ability_ID == 6:    return self.charisma