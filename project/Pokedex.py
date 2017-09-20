cin = 0
class Pokemon:
    def __init__(self, name, typ, hp, attack):
        self.name = name
        self.typ = typ
        self.hp = hp
        self.attack = attack

    def retrieve(self):
        print('This pokemon is called ' + self.name + ' and is a ' + self.typ + ' type with ' + str(self.hp)
              + 'hp and an attack of ' + str(self.attack))

class Person:
    def __init__(self, name):
        global cin
        cin = cin + 1
        self.name = name
    def getCin(self):
        print(cin)
    def setName(self, name):
        self.name = name
    def getName(self):
        print(self.name)
# pokemon1 = Pokemon('Charmander', 'Fire', 30, 5)
# pokemon2 = Pokemon('Squirtle', 'Water', 23, 2)
# #print(pokemon1.att(pokemon2))
# pokemon1.retrieve()
# pokemon2.retrieve()
