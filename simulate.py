__author__ = 'David Stonely'
from ultimatepoker import Game
import sys
from uthsim import Uthsim

try:
    simulateTimes = int(sys.argv[1])
except IndexError or ValueError:
    print ("Error: Input simulations times. Usage: python simulate.py [times]")
    exit(1)


basicsim100 = Uthsim(stack=12000,  ante=100, name="Sim100")
basicsim25 = Uthsim(stack=12000,  ante=25, name="Sim25")

result100 = True
result25 = True

for i in range(simulateTimes):
    game = Game(False)
    gain, bet = game.playGame()

    if (result100):
        result100 = basicsim100.process_game(gain=gain, bet=bet)
        if (result100 == False):
            print("================== Basic 100 Game ===============", i)
            # break

    if (result25):
        result25 = basicsim25.process_game(gain=gain, bet=bet)
        if (result25 == False):
            print("================== Basic 25 Game ===============", i)
            # break    


    if ((result25 == False) & (result100 == False)):
        print("No more active sims")
        break


basicsim100.print_summary()
basicsim25.print_summary()

