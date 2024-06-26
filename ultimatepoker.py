
import random
from bet import Bet
import strategy
from poker import Hand
from poker import Card
from treys import Evaluator
from treys import Card as tCard
import utils
from BlindBetTable import BlindBet

class Game:
    def __init__(self, stdout):
        self._deck = list(Card)
        random.shuffle(self._deck)
        self._bet = Bet(1.0)
        self._dealer = []
        self._player = []
        self._community = []
        self._gain = 0
        self.stdout = stdout
        self._eval = Evaluator()
        self._playerScore = 9999
        self._dealerScore = 9999
        self._tPlayer = []
        self._tCommunity = []
        self._tDealer = []
        self._playerClass = 0
        self._dealerClass = 0

    def startRound1(self):
        self._player = [self._deck.pop() for __ in range(2) ]
        self._dealer = [self._deck.pop() for __ in range(2) ]
        self._bet.play = strategy.round1Bet(self._player)  # 0 or 4
        if self.stdout:
            print ("***************************")
            print ("Round1: ")
            print ("Dealer: " + ", ".join([str(c) for c in self._dealer]))
            print ("Player: " + ", ".join([str(c) for c in self._player]))
            print ("==Play Bet==")
            print ("\t", self._bet.play)

    def startRound2(self):
        self._community = [self._deck.pop() for __ in range(3)]
        if self._bet.play == 0:
            self._bet.play = strategy.round2Bet(self._player, self._community)
        if self.stdout:
            print ("\nRound2: ")
            print ("Dealer: " + ", ".join([str(c) for c in self._dealer]))
            print ("Player: " + ", ".join([str(c) for c in self._player]))
            print ("Community: " + ", ".join([str(c) for c in self._community]))
            print ("==Play Bet==")
            print ("\t", self._bet.play)

    def startRound3(self):
        self._community = self._community + [self._deck.pop() for __ in range(2)]
        # print(self._community)

        if self._bet.play == 0:
            self._bet.play = strategy.round3Bet(self._player, self._community)

        if self.stdout:
            print ("\nRound3: ")
            print ("Dealer: " + ", ".join([str(c) for c in self._dealer]))
            print ("Player: " + ", ".join([str(c) for c in self._player]))
            print ("Community: " + ", ".join([str(c) for c in self._community]))
            print ("==Play Bet==")
            print ("\t", self._bet.play)            

        self._tPlayer = utils.CalculateHands.converToTreys(self._player)
        self._tCommunity = utils.CalculateHands.converToTreys(self._community)
        self._tDealer = utils.CalculateHands.converToTreys(self._dealer)

        self._playerScore = self._eval.evaluate(self._tCommunity, self._tPlayer)
        self._dealerScore = self._eval.evaluate(self._tCommunity, self._tDealer)
        self._playerClass = self._eval.get_rank_class(self._playerScore)
        self._dealerClass = self._eval.get_rank_class(self._dealerScore)

        if self._bet.play != 0:
            # result = compareHands(self._playerHand, self._dealerHand)
            result = 1
            if (self._playerScore < self._dealerScore):
                self._gain = self.gainFromWin()
                if self.stdout:
                    print ("Player Win!")
            elif (self._playerScore > self._dealerScore):
                self._gain = self.gainFromLose()
                if self.stdout:
                    print ("Player Lose!")
            else:
                self._gain = 0
                if self.stdout:
                    print ("Push")
        else:
            self._gain = self.gainFromLoseFold()
            # if self.stdout:
            # print ("Player Fold!")
        
        if (self._playerClass <= 1):  # Print out big hands
            print("PlayerScore:", self._playerScore, "   Player Class:", self._playerClass, " ", self._eval.class_to_string(self._playerClass))
            print("DealerScore:", self._dealerScore, "   Dealer Class:", self._dealerClass, " ", self._eval.class_to_string(self._dealerClass))
            print("Gain: ", self._gain)
            print ("Dealer: " + ", ".join([str(c) for c in self._dealer]))
            print ("Player: " + ", ".join([str(c) for c in self._player]))
            print ("Community: " + ", ".join([str(c) for c in self._community]))



    def gainFromWin(self):
        res = self._bet.play + BlindBet.Table[self._playerClass] * self._bet.blind
        if self._dealerClass <= 8:
            # print("Dealer Did not Qualify!")
            res += self._bet.ante  
        else:
            # print("Dealer Did not Qualify!")
            res += 0 # Dealer needs to qualify
        return res
  
    def gainFromLose(self):
         res = 0 - self._bet.play - self._bet.blind
         if self._dealerClass <= 8:
            res -= self._bet.ante
         else:
            # print("Dealer Did not Qualify!")
            res -= 0 # Dealer needs to qualify
         return res

    def gainFromLoseFold(self):
         res = 0 - self._bet.ante - self._bet.blind
        #  res -= self._bet.ante if self._dealerClass >= 8 else 0 # Dealer needs to qualify
         return res    

    def playGame(self):
        # print('-------------- R1 -----------------------------')
        self.startRound1()
        # print('-------------- R2 -----------------------------')
        self.startRound2()
        # print('-------------- R3 -----------------------------')
        self.startRound3()
        if self.stdout:
            print ("\n==GAIN THIS ROUND==")
            print ("\t", self._gain)
        return self._gain, (self._bet.blind + self._bet.ante + self._bet.play)

if __name__ == '__main__':
    game = Game()
    game.playGame()
