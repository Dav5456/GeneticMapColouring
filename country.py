class Country:
    def __init__(self,name,borders):
        self.name = name
        self.borders = borders
    
    def getBorders(self):
        return self.borders

    def addBorder(self,border):
        self.borders.append(border)
    
    def clearBorders(self):
        self.borders = []

    def seti(self, i):
        self.i = i

    def geti(self):
        return self.i

    def getName(self):
        return self.name