__author__ = 'David Stonely'
from ultimatepoker import Game
import sys
from uthsim import Uthsim

try:
    simulateTimes = int(sys.argv[1])
except IndexError or ValueError:
    print ("Error: Input simulations times. Usage: python simulate.py [times]")
    exit(1)


basicsim = Uthsim(stack=12000,  ante=100)
stack = 200000
ante = 100
totalGain = 0
totalBet = 0
maxStack = 0
wins = 0
losses = 0
pushes = 0
winstreak = 0
losestreak = 0
maxwinstreak = 0
maxlosestreak = 0


for i in range(simulateTimes):
    print("================== Game ===============", i)
    game = Game(False)
    gain, bet = game.playGame()
    # print (gain)
    totalGain += gain
    totalBet += bet
    stack += (gain * ante) 
    if (stack > maxStack):
        maxStack = stack

    if (gain > 0):
        wins += 1 
        winstreak += 1
        losestreak = 0
    elif (gain < 0):
        losses += 1
        losestreak += 1
        winstreak = 0        
    else:
        pushes += 1          

    if (losestreak > maxlosestreak):
        maxlosestreak = losestreak

    if (winstreak > maxwinstreak):
        maxwinstreak = winstreak

    if (stack < 0):
        print("No Money left!!!")
        break


print ("=============Simulation Result================")
print ("Wins:", wins, " Losses:", losses, " Push:", pushes)
print ("Max Win Streak:", maxwinstreak, "Max Lose Streak:", maxlosestreak)
print ("Runs:", simulateTimes," totalGain: ", totalGain)
print ("Runs:", simulateTimes," totalBet: ", totalBet)
print ("Runs:", simulateTimes," Ratio: ", totalGain/totalBet)
print ("Runs:", simulateTimes," Stack: ", stack)
print ("Runs:", simulateTimes," maxStack: ", maxStack)

