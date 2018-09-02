class Animal(object):

    def __init__(self, name):
        self.name = name

    def speak(self):
        print self.name, 'says', self.sound()

class Cow(Animal):
    def __init__(self, name):
        super(Cow, self).__init__(name)

    def sound(self):
        return 'moo'