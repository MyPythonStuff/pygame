global x
x = 5


class pet:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        print(self.name)

    def setname(self, name):
        self.name = name

class laptop:
    def __init__(self):
        print('i am the laptop constructor')
        global x
        print('global', x)
