# imports
from re import M
from tkinter import *
from tkinter import ttk

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
        self.createDiceFrame()
        self.createUpperFrame()
        self.createLowerFrame()
        self.createScoringOptions()
        self.createGrandTotal()

    def createDiceFrame(self):
        diceFrm = ttk.LabelFrame(self.master, text="Yahtzee", labelanchor=N)
        diceFrm.grid(row=0, rowspan=3, sticky=N, padx=(10, 5), pady=10)
        self.holdLbl = ttk.Label(diceFrm, text="Hold")
        self.holdLbl.grid(padx=10, pady=5)
        holdChks = []
        for i in range(5):
            tmpChk = ttk.Checkbutton(diceFrm)
            tmpChk.grid(row=i+1)
            holdChks.append(tmpChk)
        self.diceLbl = ttk.Label(diceFrm, text="Dice")
        self.diceLbl.grid(row=0, column=1)
        self.canvas = Canvas(diceFrm, bd=0, highlightthickness=0,
                             width=75, height=310, bg="Dark Green")
        self.canvas.grid(row=1, column=1, rowspan=5, padx=10)
        self.rollBtn = ttk.Button(diceFrm, text="New Round")
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
        self.upperLbls = []
        self.upperValueLbls = []
        lblText = ["Ones", "Twos", "Threes", "Fours", "Fives"]
        for i in range(5):
            tempLbl = ttk.Label(upperFrm, text=lblText[i])
            tempLbl.grid(row=i, column=0, sticky=W, padx=10)
            self.upperLbls.append(tempLbl)
            tempValueLbl = ttk.Label(upperFrm, text="0")
            tempValueLbl.grid(row=i, column=1, sticky=E, padx=10)
            self.upperValueLbls.append(tempValueLbl)
        sixesLbl = ttk.Label(upperFrm, text="Sixes:")
        sixesLbl.grid(sticky=W, row=5, column=0, padx=10, pady=(0, 20))
        self.upperLbls.append(sixesLbl)
        sixesValueLbl = ttk.Label(upperFrm, text="0")
        sixesValueLbl.grid(row=5, column=1, sticky=E, padx=10, pady=(0, 20))
        self.upperValueLbls.append(sixesValueLbl)
        self.totalLbl = ttk.Label(upperFrm, text="Total:")
        self.totalLbl.grid(sticky=W, row=6, column=0, padx=10)
        self.totalValueLbl = ttk.Label(upperFrm, text="0")
        self.totalValueLbl.grid(row=6, column=1, sticky=E, padx=10)
        self.bonusLbl = ttk.Label(upperFrm, text="Bonus:")
        self.bonusLbl.grid(sticky=W, row=7, column=0, padx=10)
        self.bonusValueLbl = ttk.Label(upperFrm, text="0")
        self.bonusValueLbl.grid(row=7, column=1, sticky=E, padx=10)
        self.upperTotalLbl = ttk.Label(
            upperFrm, text="Upper Total:      ")
        self.upperTotalLbl.grid(
            sticky=W, row=8, column=0, padx=10, pady=(0, 10))
        self.upperTotalValueLbl = ttk.Label(upperFrm, text="0")
        self.upperTotalValueLbl.grid(
            row=8, column=1, sticky=E, padx=10, pady=(0, 10))

    def createLowerFrame(self):
        lowerFrm = ttk.LabelFrame(
            self.master, text="Lower Score", labelanchor=N)
        lowerFrm.grid(row=1, column=1, rowspan=2,
                      sticky=N, padx=5, pady=(5, 10))
        self.upperLbls = []
        self.upperValueLbls = []
        lblText = ["Three of a Kind", "Four of a Kind", "Full House",
                   "Small Straight", "Large Straight", "Yahtzee"]
        for i in range(6):
            tempLbl = ttk.Label(lowerFrm, text=lblText[i])
            tempLbl.grid(row=i, column=0, sticky=W, padx=10)
            self.upperLbls.append(tempLbl)
            tempValueLbl = ttk.Label(lowerFrm, text="0")
            tempValueLbl.grid(row=i, column=1, sticky=E, padx=10)
            self.upperValueLbls.append(tempValueLbl)
        chanceLbl = ttk.Label(lowerFrm, text="Chance:")
        chanceLbl.grid(sticky=W, row=6, column=0, padx=10, pady=(0, 20))
        self.upperLbls.append(chanceLbl)
        chanceValueLbl = ttk.Label(lowerFrm, text="0")
        chanceValueLbl.grid(row=6, column=1, sticky=E, padx=10, pady=(0, 20))
        self.upperValueLbls.append(chanceValueLbl)
        self.lowerTotalLbl = ttk.Label(lowerFrm, text="Lower Total:")
        self.lowerTotalLbl.grid(sticky=W, row=7, column=0, padx=10)
        self.lowerTotalValueLbl = ttk.Label(lowerFrm, text="0")
        self.lowerTotalValueLbl.grid(row=7, column=1, sticky=E, padx=10)
        self.yahtzeeBonusLbl = ttk.Label(lowerFrm, text="Yahtzee Bonus:")
        self.yahtzeeBonusLbl.grid(sticky=W, row=8, column=0, padx=10)
        self.yahtzeeBonusValueLbl = ttk.Label(lowerFrm, text="0")
        self.yahtzeeBonusValueLbl.grid(row=8, column=1, sticky=E, padx=10)
        self.combTotalLbl = ttk.Label(lowerFrm, text="Combined Total:")
        self.combTotalLbl.grid(sticky=W, row=9, column=0,
                               padx=10, pady=(0, 10))
        self.combTotalValueLbl = ttk.Label(lowerFrm, text="0")
        self.combTotalValueLbl.grid(
            row=9, column=1, sticky=E, padx=10, pady=(0, 10))

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
            tempBtn.grid(sticky=NSEW, padx=(6, 5))
            self.scoringOptionBtns.append(tempBtn)

    def createGrandTotal(self):
        self.grandTotalLbl = ttk.Label(self.master, text="Grand\nTotal\n0", font=(
            "", "18", "bold"), borderwidth=5, relief="ridge", anchor="center", justify="center", width=12)
        self.grandTotalLbl.grid(
            row=2, column=2, sticky=N+E+W, padx=(5, 10), pady=(5, 10))


# main
game = Game(root)
root.mainloop()
