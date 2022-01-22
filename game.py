# imports
from tkinter import *
from tkinter import ttk
from dice import Dice
from collections import Counter

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
        self.intRolls = 0
        self.intRounds = 0
        self.bonus = False
        self.scoringOptionVars = [0] * 13
        self.initialize()
        self.dice = Dice(5, self.canvas)

    def initialize(self):
        self.createDiceFrame()
        self.createUpperFrame()
        self.createLowerFrame()
        self.createScoringOptions()
        self.createGrandTotal()
        self.disableHoldChecks()
        self.disableScoringOptions()

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
        self.rollBtn = ttk.Button(diceFrm, text="New Game")
        self.rollBtn.config(command=lambda: self.roll())
        self.rollBtn.grid(row=6, columnspan=2, sticky=NSEW,
                          padx=8, pady=(17, 5))
        self.unholdBtn = ttk.Button(
            diceFrm, text="Unhold All", command=lambda: self.unholdAll(), state="disabled")
        self.unholdBtn.grid(row=7, columnspan=2,
                            sticky=NSEW, padx=8, pady=(5, 5))
        self.rollLbl = ttk.Label(
            diceFrm, text="0/3 Rolls", anchor="center")
        self.rollLbl.grid(row=8, columnspan=2, padx=8, pady=(5, 5))
        self.roundLbl = ttk.Label(
            diceFrm, text="Round 0/13", anchor="center")
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
            if i == 0:
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(5, 0))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(5, 0))
            elif i == 5:
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(0, 20))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(0, 20))
            elif i == 8:
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
        self.lowerValueLbls = []
        self.lowerIntVars = []
        lblText = ["Three of a Kind:", "Four of a Kind:", "Full House:", "Small Straight:",
                   "Large Straight:", "Yahtzee:", "Chance:", "Lower Total:", "Yahtzee Bonus:", "Combined Total:"]
        for i in range(10):
            self.lowerIntVars.append(IntVar())
            tempLbl = ttk.Label(lowerFrm, text=lblText[i])
            tempValueLbl = ttk.Label(
                lowerFrm, text="0", textvariable=self.lowerIntVars[i])
            if i == 0:
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(5, 0))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(5, 0))
            elif i == 6:
                tempLbl.grid(row=i, column=0, sticky=W, padx=10, pady=(0, 20))
                tempValueLbl.grid(row=i, column=1, sticky=E,
                                  padx=10, pady=(0, 20))
            elif i == 9:
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
            tempBtn = ttk.Button(
                optionFrm, text=btnText[i], width=12, command=lambda option=btnText[i]: self.score(option))
            if i == 0:
                tempBtn.grid(sticky=NSEW, padx=(6, 5), pady=(5, 0))
            elif i == 12:
                tempBtn.grid(sticky=NSEW, padx=(6, 5), pady=(0, 5))
            else:
                tempBtn.grid(sticky=NSEW, padx=(6, 5))
            self.scoringOptionBtns.append(tempBtn)

    def createGrandTotal(self):
        self.grandTotalLbl = ttk.Label(self.master, text="Grand\nTotal\n0", font=(
            "", "18", "bold"), borderwidth=5, relief="ridge", anchor="center", justify="center", width=12)
        self.grandTotalLbl.grid(
            row=2, column=2, sticky=N+E+W, padx=(5, 10), pady=10)

    def updateRound(self):
        self.intRounds += 1
        self.roundLbl.config(text="Round " + str(self.intRounds) + "/13")

    def updateRolls(self, reset):
        if reset:
            self.intRolls = 0
            self.rollLbl.config(text="0/3 Rolls")
        else:
            self.intRolls += 1
            self.rollLbl.config(text=str(self.intRolls) + "/3 Rolls")

    def roll(self):
        text = self.rollBtn.cget("text")
        if text == "Play Again":
            self.newGame()
        else:
            self.dice.roll(self.holdChkVars)
            self.enableHoldChecks()
            self.unholdBtn.config(state="normal")
            self.enableScoringOptions()
            if text == "New Game" or text == "Start Round":
                self.updateRound()
            elif text == "Roll":
                self.updateRolls(False)
            self.rollBtn.config(text="Roll")
            if self.intRolls == 3:
                self.disableHoldChecks()
                self.rollBtn.config(state="disabled")
                self.unholdBtn.config(state="disabled")

    def unholdAll(self):
        for i in range(5):
            self.holdChkVars[i].set(0)

    def enableHoldChecks(self):
        for chk in self.holdChks:
            chk.config(state="normal")

    def disableHoldChecks(self):
        for chk in self.holdChks:
            chk.config(state="disabled")

    def enableScoringOptions(self):
        for i in range(13):
            if (self.scoringOptionVars[i] == 0):
                self.scoringOptionBtns[i].config(state="normal")

    def disableScoringOptions(self):
        for btn in self.scoringOptionBtns:
            btn.config(state="disabled")

    def score(self, option):
        score = 0
        values = self.dice.getValues()
        if option == "Ones":
            self.scoringOptionVars[0] = 1
            score = Counter(values)[1]
            self.upperIntVars[0].set(score)
        elif option == "Twos":
            self.scoringOptionVars[1] = 1
            score = Counter(values)[2] * 2
            self.upperIntVars[1].set(score)
        elif option == "Threes":
            self.scoringOptionVars[2] = 1
            score = Counter(values)[3] * 3
            self.upperIntVars[2].set(score)
        elif option == "Fours":
            self.scoringOptionVars[3] = 1
            score = Counter(values)[4] * 4
            self.upperIntVars[3].set(score)
        elif option == "Fives":
            self.scoringOptionVars[4] = 1
            score = Counter(values)[5] * 5
            self.upperIntVars[4].set(score)
        elif option == "Sixes":
            self.scoringOptionVars[5] = 1
            score = Counter(values)[6] * 6
            self.upperIntVars[5].set(score)
        elif option == "Three of a Kind":
            self.scoringOptionVars[6] = 1
            if len(set(values)) <= 3:
                score = self.dice.getTotal()
            self.lowerIntVars[0].set(score)
        elif option == "Four of a Kind":
            self.scoringOptionVars[7] = 1
            if len(set(values)) <= 2:
                score = self.dice.getTotal()
            self.lowerIntVars[1].set(score)
        elif option == "Full House":
            self.scoringOptionVars[8] = 1
            triplet, pair = Counter(values).most_common(2)
            if triplet[1] == 3 and pair[1] == 2:
                score = 25
            self.lowerIntVars[2].set(score)
        elif option == "Small Straight":
            self.scoringOptionVars[9] = 1
            for i in range(len(values)):
                temp = values[0:i] + values[i+1:]
                if sorted(temp) == list(range(min(temp), max(temp)+1)):
                    score = 30
                    break
            self.lowerIntVars[3].set(score)
        elif option == "Large Straight":
            self.scoringOptionVars[10] = 1
            if sorted(values) == list(range(min(values), max(values)+1)):
                score = 40
            self.lowerIntVars[4].set(score)
        elif option == "Yahtzee":
            self.scoringOptionVars[11] = 1
            if len(set(values)) == 1:
                score = 50
            self.lowerIntVars[5].set(score)
        elif option == "Chance":
            self.scoringOptionVars[12] = 1
            score = self.dice.getTotal()
            self.lowerIntVars[6].set(score)
        self.updateScore(option, score)
        self.disableScoringOptions()
        if self.intRounds < 13:
            self.newRound()
        else:
            self.endGame()

    def updateScore(self, option, score):
        if (option == "Ones" or option == "Twos" or option == "Threes" or option == "Fours"
                or option == "Fives" or option == "Sixes"):
            self.upperIntVars[6].set(self.upperIntVars[6].get()+score)
        elif (option == "Three of a Kind" or option == "Four of a Kind" or option == "Full House"
                or option == "Small Straight" or option == "Large Straight" or option == "Yahtzee" or option == "Chance"):
            self.lowerIntVars[7].set(self.lowerIntVars[7].get()+score)
        if self.upperIntVars[6].get() >= 63:
                self.upperIntVars[7].set(35)
        self.upperIntVars[8].set(self.upperIntVars[6].get()+self.upperIntVars[7].get())
        values = self.dice.getValues()
        if len(set(values)) == 1 and self.bonus:
            self.lowerIntVars[8].set(self.lowerIntVars[8].get()+100)
        self.lowerIntVars[9].set(self.lowerIntVars[7].get()+self.lowerIntVars[8].get())
        if option == "Yahtzee":
                self.bonus = True       
        grandTotal = "Grand\nTotal\n" + \
            str(self.upperIntVars[8].get()+self.lowerIntVars[9].get())
        self.grandTotalLbl.config(text=grandTotal)

    def newRound(self):
        self.unholdAll()
        self.disableHoldChecks()
        self.unholdBtn.config(state="disabled")
        self.canvas.delete("all")
        self.rollBtn.config(text="Start Round", state="normal")
        self.updateRolls(True)

    def endGame(self):
        self.disableHoldChecks()
        self.unholdBtn.config(state="disabled")
        self.rollBtn.config(text="Play Again", state="normal")

    def newGame(self):
        self.canvas.delete("all")
        self.rollBtn.config(text="Start Round")
        self.intRounds = -1
        self.updateRound()
        self.updateRolls(True)
        self.bonus = False
        for i in range(13):
            if i < 9:
                self.upperIntVars[i].set(0)
            if i < 10:
                self.lowerIntVars[i].set(0)
            self.scoringOptionVars[i] = 0
        self.enableScoringOptions()
        self.grandTotalLbl.config(text="Grand\nTotal\n0")


# main
game = Game(root)
root.mainloop()
