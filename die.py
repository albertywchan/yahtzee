import random

class Die:
    def __init__(self, canvas):
        self.value = random.randint(1,6)
        self.canvas = canvas
        self.length = 50
        self.radius = self.length / 5
        self.gap = self.radius / 2
        self.hold = False

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, x, y):
            c = self.canvas
            l = self.length
            r = self.radius
            g = self.gap
            c.create_rectangle(x, y, x+l, y+l, width = 2, outline = "Black", fill = "White")
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