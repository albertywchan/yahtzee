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
        self.strRolls = StringVar()
        self.strRounds = StringVar()
        self.frm = Frame(master)
        self.frm.grid()
        self.master = master
        self.initialize()
        self.reset()
        self.dice = Dice(5, self.canvas)

    def reset(self):
        self.intRolls = 0
        self.strRolls.set("0/3 Rolls")
        self.intRounds = 0
        self.strRounds.set("Round 0/13")
        for chk in self.holdChks:
            chk.config(state="disabled")
        self.rollBtn.config(text="Start Game")
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
        self.holdChkVars = []
        for i in range(5):
            self.holdChkVars.append(IntVar())
            tmpChk = ttk.Checkbutton(diceFrm, variable=self.holdChkVars[i])
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
        self.unholdBtn = ttk.Button(
            diceFrm, text="Unhold All", command=lambda: self.unholdAll())
        self.unholdBtn.grid(row=7, columnspan=2,
                            sticky=NSEW, padx=8, pady=(5, 5))
        self.rollLbl = ttk.Label(
            diceFrm, textvariable=self.strRolls, anchor="center")
        self.rollLbl.grid(row=8, columnspan=2, padx=8, pady=(5, 5))
        self.roundLbl = ttk.Label(
            diceFrm, textvariable=self.strRounds, anchor="center")
        self.roundLbl.grid(row=9, columnspan=2, padx=8, pady=(5, 10))

    def createUpperFrame(self):
        upperFrm = ttk.LabelFrame(
            self.master, text="Upper Score", labelanchor=N)
        upperFrm.grid(row=0, column=1, sticky=N+E+W, padx=5, pady=(10, 5))
        self.upperValueLbls = []
        self.upperIntVars = []
        lblText = ["Ones:", "Twos:", "Threes:", "Fours:", "Fives:",
                   "Sixes:", "Total:", "Bonus:", "Upper Total:      "]
        for i in range(9):
            self.upperIntVars.append(IntVar())
            tempLbl = ttk.Label(upperFrm, text=lblText[i])
            tempValueLbl = ttk.Label(
                upperFrm, text="0", textvariable=self.upperIntVars[i])
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
            self.upperValueLbls.append(tempValueLbl)

    def createLowerFrame(self):
        lowerFrm = ttk.LabelFrame(
            self.master, text="Lower Score", labelanchor=N)
        lowerFrm.grid(row=1, column=1, rowspan=2,
                      sticky=N, padx=5, pady=(5, 10))
        self.upperValueLbls = []
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
            self.upperValueLbls.append(tempValueLbl)

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
        if (self.intRounds == 0):
            self.intRounds = 1
            self.strRounds.set("Round " + str(self.intRounds) + "/13")
            for chk in self.holdChks:
                chk.config(state="normal")
            self.rollBtn.config(text="Roll")
            self.unholdBtn.config(state="normal")
            self.dice.roll(self.holdChkVars)
        else:
            self.dice.roll(self.holdChkVars)
            self.intRolls += 1
            self.strRolls.set(str(self.intRolls) + "/3 Rolls")
            if (self.intRolls == 3):
                self.rollBtn.config(state="disabled")
                self.unholdBtn.config(state="disabled")

    def unholdAll(self):
        for i in range(5):
            self.holdChkVars[i].set(0)

    def score(self, option):
        score = 0
        print(option)
        if option == "Ones":
            for i in range(5):
                if self.dice.diceArray[i].value == 1:
                    score += 1
            self.upperIntVars[0].set(score)
            self.scoringOptionBtns[0].config(state="disabled")
        elif option == "Twos":
            for i in range(5):
                if self.dice.diceArray[i].value == 2:
                    score += 2
            self.upperIntVars[1].set(score)
            self.scoringOptionBtns[1].config(state="disabled")
        self.update(option, score)

    def update(self, option, score):
        if (option == "Ones" or option == "Twos"):
            self.upperIntVars[6].set(self.upperIntVars[6]+score)
            self.upperIntVars[6].set(self.upperIntVars[6]+self.upperIntVars[7])


# main
game = Game(root)
root.mainloop()
