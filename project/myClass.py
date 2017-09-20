class MyClass:
    global g
    self.fuck = 5
    def __init__(self, name):
        print('constructor printed')
        pet = name

    def getname(self):
        print(self.pet)

    def setglobal(self, glob):
        global g
        g = glob

    def getglobal(self):
        return g

    def getclass(self):
        return self.fuck