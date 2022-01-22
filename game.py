# imports
from tkinter import *
from tkinter import ttk
from dice import Dice
from collections import Counter
from PIL import Image, ImageTk

# root
root = Tk()
root.title("Yahtzee")
root.resizable(height=0, width=0)
root.call('wm', 'iconphoto', root._w, PhotoImage(file="dice.png"))

# ---------------------------------------------------------------------------------------------------------------


class Game:
    def __init__(self, master):
        self.frm = Frame(master)
        self.frm.pack()
        self.master = master
        self.initialize()

    def initialize(self):
        # variables
        self.holdChks = []
        self.holdChkVars = []
        self.rolls = 0
        self.rounds = 0
        self.upperIntVars = []
        self.lowerIntVars = []
        self.scoringOptionBtns = []
        self.scoringOptionVars = [0] * 13
        self.bonus = False
        # dice image
        diceImg = Image.open("dice.png")
        self.resizedDiceImg = ImageTk.PhotoImage(
            diceImg.resize((63, 63), Image.ANTIALIAS))
        # create frames
        self.createFirstFrame()
        self.createSecondFrame()
        self.createThirdFrame()
        self.disableHoldChecks()
        self.disableScoringOptions()
        # initialize dice
        self.dice = Dice(5, self.canvas)

    def createFirstFrame(self):
        firstFrm = ttk.LabelFrame(self.master, text="Yahtzee", labelanchor=N)
        firstFrm.pack(side="left", anchor=N, padx=(10, 5), pady=10)
        diceFrm = ttk.Frame(firstFrm)
        diceFrm.pack()
        holdChkFrm = ttk.Frame(diceFrm)
        holdChkFrm.pack(side="left", pady=10)
        for i in range(5):
            self.holdChkVars.append(IntVar())
            tmpChk = ttk.Checkbutton(holdChkFrm, variable=self.holdChkVars[i])
            tmpChk.pack(padx=5, pady=20)
            self.holdChks.append(tmpChk)
        self.canvas = Canvas(diceFrm, bd=0, highlightthickness=0,
                             width=75, height=310, bg="dark green")
        self.canvas.pack(side="left", pady=10)
        self.rollBtn = ttk.Button(
            firstFrm, text="New Game", command=lambda: self.roll(), width=12)
        self.rollBtn.pack(fill="both", padx=5, pady=8)
        self.unholdBtn = ttk.Button(
            firstFrm, text="Unhold All", command=lambda: self.unholdAll(), state="disabled")
        self.unholdBtn.pack(fill="both", padx=5, pady=8)
        self.rollLbl = ttk.Label(firstFrm, text="0/3 Rolls", anchor="center")
        self.rollLbl.pack(fill="both", padx=5, pady=8)
        self.roundLbl = ttk.Label(firstFrm, text="Round 0/13", anchor="center")
        self.roundLbl.pack(fill="both", padx=5, pady=8)

    def createSecondFrame(self):
        secondFrm = ttk.Frame(self.master)
        secondFrm.pack(side="left", anchor=N, padx=5, pady=10)
        # upper frame
        upperFrm = ttk.LabelFrame(secondFrm, text="Upper Score", labelanchor=N)
        upperFrm.pack()
        upperLeftFrm = ttk.Frame(upperFrm)
        upperLeftFrm.pack(side="left")
        upperRightFrm = ttk.Frame(upperFrm)
        upperRightFrm.pack(side="left")
        lblText = ["Ones:", "Twos:", "Threes:", "Fours:", "Fives:",
                   "Sixes:", "Total:", "Bonus:", "Upper Total:      "]
        for i in range(9):
            self.upperIntVars.append(IntVar())
            tempLbl = ttk.Label(
                upperLeftFrm, text=lblText[i], anchor=W, width=12)
            tempValueLbl = ttk.Label(
                upperRightFrm, text="0", textvariable=self.upperIntVars[i], anchor=E, width=3)
            if i == 0:
                tempLbl.pack(padx=10, pady=(5, 0))
                tempValueLbl.grid(padx=5, pady=(5, 0))
            elif i == 5:
                tempLbl.pack(padx=10, pady=(0, 20))
                tempValueLbl.grid(padx=5, pady=(0, 20))
            elif i == 8:
                tempLbl.pack(padx=10, pady=(0, 10))
                tempValueLbl.grid(padx=5, pady=(0, 10))
            else:
                tempLbl.pack()
                tempValueLbl.grid(padx=10)
        # gap to fill
        gap = Canvas(secondFrm, bg="white", height=2, width=12)
        gap.pack(fill="both")
        # lower frame
        lowerFrm = ttk.LabelFrame(secondFrm, text="Upper Score", labelanchor=N)
        lowerFrm.pack()
        lowerLeftFrm = ttk.Frame(lowerFrm)
        lowerLeftFrm.pack(side="left")
        lowerRightFrm = ttk.Frame(lowerFrm)
        lowerRightFrm.pack(side="left")
        lblText = ["Three of a Kind:", "Four of a Kind:", "Full House:", "Small Straight:",
                   "Large Straight:", "Yahtzee:", "Chance:", "Lower Total:", "Yahtzee Bonus:", "Combined Total:"]
        for i in range(10):
            self.lowerIntVars.append(IntVar())
            tempLbl = ttk.Label(
                lowerLeftFrm, text=lblText[i], anchor=W, width=12)
            tempValueLbl = ttk.Label(
                lowerRightFrm, text="0", textvariable=self.lowerIntVars[i], anchor=E, width=3)
            if i == 0:
                tempLbl.pack(padx=10, pady=(5, 0))
                tempValueLbl.pack(padx=10, pady=(5, 0))
            elif i == 6:
                tempLbl.pack(padx=10, pady=(0, 20))
                tempValueLbl.pack(padx=10, pady=(0, 20))
            elif i == 9:
                tempLbl.pack(padx=10, pady=(0, 10))
                tempValueLbl.pack(padx=10, pady=(0, 10))
            else:
                tempLbl.pack()
                tempValueLbl.pack(padx=10)

    def createThirdFrame(self):
        thirdFrm = ttk.Frame(self.master)
        thirdFrm.pack(side="left", anchor=N, padx=(5, 10), pady=10)
        btnFrm = ttk.LabelFrame(
            thirdFrm, text="Scoring Options", labelanchor=N)
        btnFrm.pack()
        btnText = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind",
                   "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]
        for i in range(13):
            tempBtn = ttk.Button(
                btnFrm, text=btnText[i], command=lambda option=btnText[i]: self.score(option), width=12)
            if i == 0:
                tempBtn.pack(fill="both", padx=5, pady=(5, 0))
            elif i == 12:
                tempBtn.pack(fill="both", padx=5, pady=(0, 5))
            else:
                tempBtn.pack(fill="both", padx=5)
            self.scoringOptionBtns.append(tempBtn)
        gap = Canvas(thirdFrm, bg="white", height=2, width=12)
        gap.pack(fill="both")
        self.grandTotalLbl = ttk.Label(thirdFrm, text="Grand\nTotal\n0", font=(
            "", "18", "bold"), borderwidth=5, relief="ridge", anchor="center", justify="center", width=12)
        self.grandTotalLbl.pack()
        imgLbl = Label(thirdFrm, image=self.resizedDiceImg)
        imgLbl.pack(side="bottom", fill="both", expand="yes", ipady=5)

    def updateRound(self):
        self.rounds += 1
        self.roundLbl.config(text="Round " + str(self.rounds) + "/13")

    def updateRolls(self, reset):
        if reset:
            self.rolls = 0
            self.rollLbl.config(text="0/3 Rolls")
        else:
            self.rolls += 1
            self.rollLbl.config(text=str(self.rolls) + "/3 Rolls")

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
            if self.rolls == 3:
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
            if self.scoringOptionVars[i] == 0:
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
        if self.rounds < 13:
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
        # lower bonus
        if self.upperIntVars[6].get() >= 63:
            self.upperIntVars[7].set(35)
        self.upperIntVars[8].set(
            self.upperIntVars[6].get()+self.upperIntVars[7].get())
        # yahtzee bonus
        values = self.dice.getValues()
        if len(set(values)) == 1 and self.bonus:
            self.lowerIntVars[8].set(self.lowerIntVars[8].get()+100)
        self.lowerIntVars[9].set(
            self.lowerIntVars[7].get()+self.lowerIntVars[8].get())
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
        self.rounds = -1
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
