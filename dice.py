from die import Die
import random

class Dice:
    def __init__(self, size = 50):
        self.die1 = Die(size)
        self.die2 = Die(size)
        self.die3 = Die(size)
        self.die4 = Die(size)
        self.die5 = Die(size)
        self.setSize(size)
        self.setValues()
        self.dieArray = [self.die1, self.die2, self.die3, self.die4, self.die5]

    def __str__(self):
        strDice = str(self.die1) + "-" + str(self.die2) + "-" + str(self.die3) + "-" + str(self.die4) + "-" + str(self.die5)
        return strDice

    def setValues(self):
        self.die1.setValue()
        self.die2.setValue()
        self.die3.setValue()
        self.die4.setValue()
        self.die5.setValue()

    def setSize(self, size):
        self.die1.setSize(size)
        self.die2.setSize(size)
        self.die3.setSize(size)
        self.die4.setSize(size)
        self.die5.setSize(size)

    def sort(self):
        swapped = True
        j = len(self.dieArray) - 1
        while j > 0 and swapped:
            swapped = False
            for i in range(0, j):
                if self.dieArray[i].value > self.dieArray[i + 1].value:
                    self.dieArray[i].value, self.dieArray[i + 1].value = self.dieArray[i + 1].value, self.dieArray[i].value
                    swapped = True
            j = j - 1

    def roll(self, c):
        # self.hold()
        # self.unHold()
        for i in range(0, len(self.dieArray)):
            if self.dieArray[i].hold == False:
                self.dieArray[i].value = random.randint(1, 6)
        self.draw(c)

    def draw(self, c, x = 13, y = 10):
        self.die1.draw(c, self.die1.value, x, y)
        self.die2.draw(c, self.die2.value, x, y + 60)
        self.die3.draw(c, self.die3.value, x, y + 120)
        self.die4.draw(c, self.die4.value, x, y + 180)
        self.die5.draw(c, self.die5.value, x, y + 240)