class User:
    name = ''

    def __init__(self):
        self.name = None

    def getName(self):
        return self.name

    def setName(self, name):
        if name != '':
            self.name = name
