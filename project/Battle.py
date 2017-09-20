from project import Pokedex


def att(self, other):
    other.hp = (other.hp - self.attack)
    print('target\'s hp is now: ' + str(other.hp))
    # return 'target\'s hp is now: ' + str(other.hp)

class Battle:
    def battle(attack, other):
        other.hp = (other.hp - attack.attack)
        print('target\'s hp is now: ' + other.hp)

    def att(self, other):
        other.hp = (other.hp - self.attack)
        print('target\'s hp is now: ' + str(other.hp))
        #return 'target\'s hp is now: ' + str(other.hp)

Pikachu = Pokedex.Pokemon('Pikachu', 'Electricity', 35, 5)
Koffing = Pokedex.Pokemon('Seaking', 'Water', 50, 9)
#Pikachu.att(Koffing)
att(Pikachu, Koffing)
Pikachu.retrieve()