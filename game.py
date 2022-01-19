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
        self.createDiceFrame(master)
        self.createUpperFrame(master)
        self.createLowerFrame(master)
        self.createScoringOptions(master)
        self.createGrandTotal(master)

    def createDiceFrame(self, master):
        self.diceFrm = ttk.LabelFrame(master, text="Yahtzee", labelanchor=N)
        self.diceFrm.grid(row=0, rowspan=3, sticky=N, padx=(10, 5), pady=10)
        self.holdLbl = ttk.Label(self.diceFrm, text="Hold")
        self.holdLbl.grid(padx=10, pady=5)
        self.holdChk1 = ttk.Checkbutton(self.diceFrm)
        self.holdChk1.grid(row=1)
        self.holdChk2 = ttk.Checkbutton(self.diceFrm)
        self.holdChk2.grid(row=2)
        self.holdChk3 = ttk.Checkbutton(self.diceFrm)
        self.holdChk3.grid(row=3)
        self.holdChk4 = ttk.Checkbutton(self.diceFrm)
        self.holdChk4.grid(row=4)
        self.holdChk5 = ttk.Checkbutton(self.diceFrm)
        self.holdChk5.grid(row=5)
        self.diceLbl = ttk.Label(self.diceFrm, text="Dice")
        self.diceLbl.grid(row=0, column=1)
        self.canvas = Canvas(
            self.diceFrm, bd=0, highlightthickness=0, width=75, height=310, bg="Dark Green")
        self.canvas.grid(row=1, column=1, rowspan=5, padx=10)
        self.rollBtn = ttk.Button(self.diceFrm, text="New Round")
        self.rollBtn.grid(row=6, columnspan=2, sticky=NSEW,
                          padx=8, pady=(17, 5))
        self.unholdBtn = ttk.Button(self.diceFrm, text="Unhold All")
        self.unholdBtn.grid(row=7, columnspan=2,
                            sticky=NSEW, padx=8, pady=(5, 5))
        self.rollLbl = ttk.Label(
            self.diceFrm, text="0/3 Rolls", anchor="center")
        self.rollLbl.grid(row=8, columnspan=2, padx=8, pady=(5, 5))
        self.roundLbl = ttk.Label(
            self.diceFrm, text="1/13 Rounds", anchor="center")
        self.roundLbl.grid(row=9, columnspan=2, padx=8, pady=(5, 10))

    def createUpperFrame(self, master):
        self.upperFrm = ttk.LabelFrame(
            master, text="Upper Score", labelanchor=N)
        self.upperFrm.grid(row=0, column=1, sticky=N+E+W, padx=5, pady=(10, 5))
        self.onesLbl = ttk.Label(self.upperFrm, text="Ones:")
        self.onesLbl.grid(sticky=W, padx=10, pady=(5, 0))
        self.onesValueLbl = ttk.Label(self.upperFrm, text="0")
        self.onesValueLbl.grid(row=0, column=1, sticky=E, padx=10, pady=(5, 0))
        self.twosLbl = ttk.Label(self.upperFrm, text="Twos:")
        self.twosLbl.grid(sticky=W, row=1, column=0, padx=10)
        self.twosValueLbl = ttk.Label(self.upperFrm, text="0")
        self.twosValueLbl.grid(row=1, column=1, sticky=E, padx=10)
        self.threesLbl = ttk.Label(self.upperFrm, text="Threes:")
        self.threesLbl.grid(sticky=W, row=2, column=0, padx=10)
        self.threesValueLbl = ttk.Label(self.upperFrm, text="0")
        self.threesValueLbl.grid(row=2, column=1, sticky=E, padx=10)
        self.foursLbl = ttk.Label(self.upperFrm, text="Fours:")
        self.foursLbl.grid(sticky=W, row=3, column=0, padx=10)
        self.foursValueLbl = ttk.Label(self.upperFrm, text="0")
        self.foursValueLbl.grid(row=3, column=1, sticky=E, padx=10)
        self.fivesLbl = ttk.Label(self.upperFrm, text="Fives:")
        self.fivesLbl.grid(sticky=W, row=4, column=0, padx=10)
        self.fivesValueLbl = ttk.Label(self.upperFrm, text="0")
        self.fivesValueLbl.grid(row=4, column=1, sticky=E, padx=10)
        self.sixesLbl = ttk.Label(self.upperFrm, text="Sixes:")
        self.sixesLbl.grid(sticky=W, row=5, column=0, padx=10, pady=(0, 20))
        self.sixesValueLbl = ttk.Label(self.upperFrm, text="0")
        self.sixesValueLbl.grid(
            row=5, column=1, sticky=E, padx=10, pady=(0, 20))
        self.totalLbl = ttk.Label(self.upperFrm, text="Total:")
        self.totalLbl.grid(sticky=W, row=6, column=0, padx=10)
        self.totalValueLbl = ttk.Label(self.upperFrm, text="0")
        self.totalValueLbl.grid(row=6, column=1, sticky=E, padx=10)
        self.bonusLbl = ttk.Label(self.upperFrm, text="Bonus:")
        self.bonusLbl.grid(sticky=W, row=7, column=0, padx=10)
        self.bonusValueLbl = ttk.Label(self.upperFrm, text="0")
        self.bonusValueLbl.grid(row=7, column=1, sticky=E, padx=10)
        self.upperTotalLbl = ttk.Label(
            self.upperFrm, text="Upper Total:      ")
        self.upperTotalLbl.grid(
            sticky=W, row=8, column=0, padx=10, pady=(0, 10))
        self.upperTotalValueLbl = ttk.Label(self.upperFrm, text="0")
        self.upperTotalValueLbl.grid(
            row=8, column=1, sticky=E, padx=10, pady=(0, 10))

    def createLowerFrame(self, master):
        self.lowerFrm = ttk.LabelFrame(
            master, text="Lower Score", labelanchor=N)
        self.lowerFrm.grid(row=1, column=1, rowspan=2,
                           sticky=N, padx=5, pady=(5, 10))
        self.threeOfLbl = ttk.Label(self.lowerFrm, text="Three of a Kind:")
        self.threeOfLbl.grid(sticky=W, padx=10, pady=(5, 0))
        self.threeOfValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.threeOfValueLbl.grid(
            row=0, column=1, sticky=E, padx=10, pady=(5, 0))
        self.fourOfLbl = ttk.Label(self.lowerFrm, text="Four of a Kind:")
        self.fourOfLbl.grid(sticky=W, row=1, column=0, padx=10)
        self.fourOfValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.fourOfValueLbl.grid(row=1, column=1, sticky=E, padx=10)
        self.fullHouseLbl = ttk.Label(self.lowerFrm, text="Full House:")
        self.fullHouseLbl.grid(sticky=W, row=2, column=0, padx=10)
        self.fullHouseValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.fullHouseValueLbl.grid(row=2, column=1, sticky=E, padx=10)
        self.smSraightLbl = ttk.Label(self.lowerFrm, text="Small Straight:")
        self.smSraightLbl.grid(sticky=W, row=3, column=0, padx=10)
        self.smStraightValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.smStraightValueLbl.grid(row=3, column=1, sticky=E, padx=10)
        self.lgStraightLbl = ttk.Label(self.lowerFrm, text="Large Straight:")
        self.lgStraightLbl.grid(sticky=W, row=4, column=0, padx=10)
        self.lgStraightValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.lgStraightValueLbl.grid(row=4, column=1, sticky=E, padx=10)
        self.yahtzeeLbl = ttk.Label(self.lowerFrm, text="Yahtzee:")
        self.yahtzeeLbl.grid(sticky=W, row=5, column=0, padx=10)
        self.yahtzeeValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.yahtzeeValueLbl.grid(row=5, column=1, sticky=E, padx=10)
        self.chanceLbl = ttk.Label(self.lowerFrm, text="Chance:")
        self.chanceLbl.grid(sticky=W, row=6, column=0, padx=10, pady=(0, 20))
        self.chanceValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.chanceValueLbl.grid(
            row=6, column=1, sticky=E, padx=10, pady=(0, 20))
        self.lowerTotalLbl = ttk.Label(self.lowerFrm, text="Lower Total:")
        self.lowerTotalLbl.grid(sticky=W, row=7, column=0, padx=10)
        self.lowerTotalValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.lowerTotalValueLbl.grid(row=7, column=1, sticky=E, padx=10)
        self.yahtzeeBonusLbl = ttk.Label(self.lowerFrm, text="Yahtzee Bonus:")
        self.yahtzeeBonusLbl.grid(sticky=W, row=8, column=0, padx=10)
        self.yahtzeeBonusValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.yahtzeeBonusValueLbl.grid(row=8, column=1, sticky=E, padx=10)
        self.combTotalLbl = ttk.Label(self.lowerFrm, text="Combined Total:")
        self.combTotalLbl.grid(sticky=W, row=9, column=0,
                               padx=10, pady=(0, 10))
        self.combTotalValueLbl = ttk.Label(self.lowerFrm, text="0")
        self.combTotalValueLbl.grid(
            row=9, column=1, sticky=E, padx=10, pady=(0, 10))

    def createScoringOptions(self, master):
        self.optionFrm = ttk.LabelFrame(
            master, text="Scoring Options", labelanchor=N)
        self.optionFrm.grid(row=0, column=2, rowspan=2, sticky=N +
                            E+W, padx=(5, 10), pady=(10, 5))
        self.onesBtn = ttk.Button(self.optionFrm, text="Ones", width=12)
        self.onesBtn.grid(sticky=NSEW, padx=(6, 5), pady=(5, 0))
        self.twosBtn = ttk.Button(self.optionFrm, text="Twos", width=12)
        self.twosBtn.grid(sticky=NSEW, padx=(6, 5))
        self.threesBtn = ttk.Button(self.optionFrm, text="Threes", width=12)
        self.threesBtn.grid(sticky=NSEW, padx=(6, 5))
        self.foursBtn = ttk.Button(self.optionFrm, text="Fours", width=12)
        self.foursBtn.grid(sticky=NSEW, padx=(6, 5))
        self.fivesBtn = ttk.Button(self.optionFrm, text="Fives", width=12)
        self.fivesBtn.grid(sticky=NSEW, padx=(6, 5))
        self.sixesBtn = ttk.Button(self.optionFrm, text="Sixes", width=12)
        self.sixesBtn.grid(sticky=NSEW, padx=(6, 5))
        self.threeOfBtn = ttk.Button(
            self.optionFrm, text="Three of a Kind", width=12)
        self.threeOfBtn.grid(sticky=NSEW, padx=(6, 5))
        self.fourOfBtn = ttk.Button(
            self.optionFrm, text="Four of a Kind", width=12)
        self.fourOfBtn.grid(sticky=NSEW, padx=(6, 5))
        self.fullHouseBtn = ttk.Button(
            self.optionFrm, text="Full House", width=12)
        self.fullHouseBtn.grid(sticky=NSEW, padx=(6, 5))
        self.smStraightBtn = ttk.Button(
            self.optionFrm, text="Small Straight", width=12)
        self.smStraightBtn.grid(sticky=NSEW, padx=(6, 5))
        self.lgStraightBtn = ttk.Button(
            self.optionFrm, text="Large Straight", width=12)
        self.lgStraightBtn.grid(sticky=NSEW, padx=(6, 5))
        self.yahtzeeBtn = ttk.Button(self.optionFrm, text="Yahtzee", width=12)
        self.yahtzeeBtn.grid(sticky=NSEW, padx=(6, 5))
        self.chanceBtn = ttk.Button(self.optionFrm, text="Chance", width=12)
        self.chanceBtn.grid(sticky=NSEW, padx=(6, 5), pady=(0, 5))

    def createGrandTotal(self, master):
        self.grandTotalLbl = ttk.Label(master, text="Grand\nTotal\n0", font=(
            "", "18", "bold"), borderwidth=5, relief="ridge", anchor="center", justify="center", width=12)
        self.grandTotalLbl.grid(
            row=2, column=2, sticky=N+E+W, padx=(5, 10), pady=(5, 10))


# main
game = Game(root)
root.mainloop()