class newClass:
    pet = ''
    def __init__(self):
        print('constructor printed')
        pet = self
    def getname(self):
        global pet
        print(pet)