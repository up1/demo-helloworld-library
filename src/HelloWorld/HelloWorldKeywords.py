class HelloWorldKeywords(object):
    def __init__(self):
        self.name = "Noname"

    def say_hi(self):
        print("Say hi " + self.name)

    def say_hi2(self, name):
        self.name = name
        print("Say hi " + self.name)
