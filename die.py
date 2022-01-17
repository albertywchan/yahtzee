import random

class Die:
    def __init__(self, size = 50):
        self.value = random.randint(1,6)
        self.size = size
        self.radius = self.size / 5
        self.gap = self.radius / 2
        self.hold = False
        self.setSize(size)
        self.setValue()

    def __str__ (self):
        strValue = str(self.value)
        return strValue

    def setValue(self):
        if self.value >= 1 or self.value <= 6:
            self.value = self.value + 0
        else:
            self.value = 1

    def setSize(self, size):
        if self.size >= 30 or self.size <= 100:
            self.size = self.size + 0
        else:
            self.size = 50

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, c, v, x, y):
            s = self.size
            r = self.radius
            g = self.gap
            self.value = v
            c.create_rectangle(x, y, x+s, y+s, width = 2, outline = "Black", fill = "White")
            if self.value == 1:
                c.create_oval(x+r+2*g, y+r+2*g, x+2*r+2*g, y+2*r+2*g, fill = "Black")
            elif self.value == 2:
                c.create_oval(x+g, y+g, x+r+g, y+r+g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+2*r+3*g, x+3*r+3*g, y+3*r+3*g, fill = "Black")
            elif self.value == 3:
                c.create_oval(x+g, y+g, x+r+g, y+r+g, fill = "Black")
                c.create_oval(x+r+2*g, y+r+2*g, x+2*r+2*g, y+2*r+2*g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+2*r+3*g, x+3*r+3*g, y+3*r+3*g, fill = "Black")
            elif self.value == 4:
                c.create_oval(x+g, y+g, x+r+g, y+r+g, fill = "Black")
                c.create_oval(x+g, y+2*r+3*g, x+r+g, y+3*r+3*g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+g, x+3*r+3*g, y+r+g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+2*r+3*g, x+3*r+3*g, y+3*r+3*g, fill = "Black")
            elif self.value == 5:
                c.create_oval(x+r+2*g, y+r+2*g, x+2*r+2*g, y+2*r+2*g, fill = "Black")
                c.create_oval(x+g, y+g, x+r+g, y+r+g, fill = "Black")
                c.create_oval(x+g, y+2*r+3*g, x+r+g, y+3*r+3*g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+g, x+3*r+3*g, y+r+g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+2*r+3*g, x+3*r+3*g, y+3*r+3*g, fill = "Black")
            else:
                c.create_oval(x+g, y+g, x+r+g, y+r+g, fill = "Black")
                c.create_oval(x+g, y+r+2*g, x+r+g, y+2*r+2*g, fill = "Black")
                c.create_oval(x+g, y+2*r+3*g, x+r+g, y+3*r+3*g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+g, x+3*r+3*g, y+r+g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+r+2*g, x+3*r+3*g, y+2*r+2*g, fill = "Black")
                c.create_oval(x+2*r+3*g, y+2*r+3*g, x+3*r+3*g, y+3*r+3*g, fill = "Black")