# imports
from tkinter import *
from tkinter import ttk
from dice import Dice

# root
root = Tk()
root.title("Yahtzee")
root.geometry("510x530")
root.resizable(height=0, width=0)

# --------------------------------------------------------------------------


class Game:
    def __init__(self, master):
        self.frm = Frame(master)
        self.frm.grid()
        self.master = master
        self.initialize()
        self.reset()
        self.dice = Dice(5, self.canvas)

    def reset(self):
        for chk in self.holdChks:
            chk.config(state="disabled")
        self.unholdBtn.config(state="disabled")
    
    def initialize(self):
        self.createDiceFrame()
        self.createUpperFrame()
        self.createLowerFrame()
        self.createScoringOptions()
        self.createGrandTotal()

    def createDiceFrame(self):
        diceFrm = ttk.LabelFrame(self.master, text="Yahtzee", labelanchor=N)
        diceFrm.grid(row=0, rowspan=3, sticky=N, padx=(10, 5), pady=10)
        holdLbl = ttk.Label(diceFrm, text="Hold")
        holdLbl.grid(padx=10, pady=5)
        self.holdChks = []
        for i in range(5):
            tmpChk = ttk.Checkbutton(diceFrm)
            tmpChk.grid(row=i+1)
            self.holdChks.append(tmpChk)
        diceLbl = ttk.Label(diceFrm, text="Dice")
        diceLbl.grid(row=0, column=1)
        self.canvas = Canvas(diceFrm, bd=0, highlightthickness=0,
                             width=75, height=310, bg="dark green")
        self.canvas.grid(row=1, column=1, rowspan=5, padx=10)
        self.rollBtn = ttk.Button(
            diceFrm, text="Start Game", command=lambda: self.roll())
        self.rollBtn.grid(row=6, columnspan=2, sticky=NSEW,
                          padx=8, pady=(17, 5))
        self.unholdBtn = ttk.Button(diceFrm, text="Unhold All")
        self.unholdBtn.grid(row=7, columnspan=2,
                            sticky=NSEW, padx=8, pady=(5, 5))
        self.rollLbl = ttk.Label(diceFrm, text="0/3 Rolls", anchor="center")
        self.rollLbl.grid(row=8, columnspan=2, padx=8, pady=(5, 5))
        self.roundLbl = ttk.Label(diceFrm, text="1/13 Rounds", anchor="center")
        self.roundLbl.grid(row=9, columnspan=2, padx=8, pady=(5, 10))

    def createUpperFrame(self):
        upperFrm = ttk.LabelFrame(
            self.master, text="Upper Score", labelanchor=N)
        upperFrm.grid(row=0, column=1, sticky=N+E+W, padx=5, pady=(10, 5))
        self.lowerValueLbls = []
        lblText = ["Ones:", "Twos:", "Threes:", "Fours:", "Fives:",
                   "Sixes:", "Total:", "Bonus:", "Upper Total:      "]
        for i in range(9):
            tempLbl = ttk.Label(upperFrm, text=lblText[i])
            tempValueLbl = ttk.Label(upperFrm, text="0")
            if (i == 0):
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(5, 0))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(5, 0))
            elif (i == 5):
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(0, 20))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(0, 20))
            elif (i == 8):
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(0, 10))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(0, 10))
            else:
                tempLbl.grid(row=i, column=0, sticky=W, padx=10)
                tempValueLbl.grid(row=i, column=1, sticky=E, padx=10)
            self.lowerValueLbls.append(tempValueLbl)

    def createLowerFrame(self):
        lowerFrm = ttk.LabelFrame(
            self.master, text="Lower Score", labelanchor=N)
        lowerFrm.grid(row=1, column=1, rowspan=2,
                      sticky=N, padx=5, pady=(5, 10))
        self.lowerValueLbls = []
        lblText = ["Three of a Kind:", "Four of a Kind:", "Full House:", "Small Straight:",
                   "Large Straight:", "Yahtzee:", "Chance:", "Lower Total:", "Yahtzee Bonus:", "Combined Total:"]
        for i in range(10):
            tempLbl = ttk.Label(lowerFrm, text=lblText[i])
            tempValueLbl = ttk.Label(lowerFrm, text="0")
            if (i == 0):
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(5, 0))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(5, 0))
            elif (i == 6):
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(0, 20))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(0, 20))
            elif (i == 9):
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(0, 10))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(0, 10))
            else:
                tempLbl.grid(row=i, column=0, sticky=W, padx=10)
                tempValueLbl.grid(row=i, column=1, sticky=E, padx=10)
            self.lowerValueLbls.append(tempValueLbl)

    def createScoringOptions(self):
        optionFrm = ttk.LabelFrame(
            self.master, text="Scoring Options", labelanchor=N)
        optionFrm.grid(row=0, column=2, rowspan=2, sticky=N +
                       E+W, padx=(5, 10), pady=(10, 5))
        self.scoringOptionBtns = []
        btnText = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind",
                   "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]
        for i in range(13):
            tempBtn = ttk.Button(optionFrm, text=btnText[i], width=12)
            if (i == 0):
                tempBtn.grid(sticky=NSEW, padx=(6, 5), pady=(5, 0))
            elif (i == 12):
                tempBtn.grid(sticky=NSEW, padx=(6, 5), pady=(0, 5))
            else:
                tempBtn.grid(sticky=NSEW, padx=(6, 5))
            self.scoringOptionBtns.append(tempBtn)

    def createGrandTotal(self):
        self.grandTotalLbl = ttk.Label(self.master, text="Grand\nTotal\n0", font=(
            "", "18", "bold"), borderwidth=5, relief="ridge", anchor="center", justify="center", width=12)
        self.grandTotalLbl.grid(
            row=2, column=2, sticky=N+E+W, padx=(5, 10), pady=10)

    def roll(self):
        self.dice.roll()


# main
game = Game(root)
root.mainloop()
