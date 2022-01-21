from die import Die

class Dice:
    def __init__(self, size, canvas):
        self.diceArray = []
        self.size = size
        for i in range(self.size):
            d = Die(canvas)
            self.diceArray.append(d)

    def roll(self, holdChkVars):
        for i in range(self.size):
            if holdChkVars[i].get() == 0:
                self.diceArray[i].roll()
        self.draw()

    def draw(self, x = 13, y = 10):
        for i in range(self.size):
            d = self.diceArray[i]
            d.draw(x, y + i * 60)

    def getValues(self):
        values = []
        for i in range(self.size):
            values[i].append(self.diceArray[i].value)