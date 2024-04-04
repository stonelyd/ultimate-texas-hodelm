
from enum import Enum 

class Result(Enum):
    Neither = 2
    Win = 1
    Loss = 0
    

class Uthsim:
    def __init__(self, stack, ante, name):
        self.name = name
        self.runs = 0
        self.stack = stack
        self.ante = ante
        self.totalGain = 0
        self.totalBet = 0
        self.maxStack = 0
        self.wins = 0
        self.losses = 0
        self.pushes = 0
        self.winstreak = 0
        self.winstreakaccum = 0
        self.losstreak = 0
        self.losstreakaccum = 0
        self.lastResult = Result.Neither
        self.thisResult = Result.Neither
        self.numwinstreaks = 0
        self.numlossstreaks = 0
        
        self.maxwinstreak = 0
        self.maxlosestreak = 0

    def process_game(self, gain, bet):

        self.runs += 1
        self.totalGain += gain
        self.totalBet += bet
        self.stack += (gain * self.ante) 
        if (self.stack > self.maxStack):
            self.maxStack = self.stack



        if (gain > 0):            
            # print("Win")
            
            self.thisResult = Result.Win
            self.wins += 1 
            self.winstreak += 1
                
            # self.winstreakaccum = self.winstreakaccum + self.winstreak    
            # self.losestreak = 0
            # print ("Winstreak:", self.winstreak, "WinstreakAccum:", self.winstreakaccum)    
                       
        elif (gain < 0):
            # print("Loss")
            self.thisResult = Result.Loss
            self.losses += 1
            self.losstreak += 1
                
            # self.losestreakaccum = self.losestreakaccum + self.losestreak                
            # self.winstreak = 0        
            # print ("Losestreak:", self.losestreak, "LossStreakAccum:", self.losestreakaccum)

        else:
            # print("Push")
            self.thisResult = Result.Neither
            self.pushes += 1      


        if (self.lastResult == Result.Win):
            if (self.thisResult == Result.Loss):
                self.winstreakaccum = self.winstreakaccum + self.winstreak
                self.numwinstreaks += 1
                self.winstreak = 0
                # print ("Winstreak:", self.winstreak, "WinstreakAccum:", self.winstreakaccum)

        if (self.lastResult == Result.Loss):
            if (self.thisResult == Result.Win):
                self.losstreakaccum = self.losstreakaccum + self.losstreak
                self.numlossstreaks += 1
                self.losstreak = 0
                # print ("Losestreak:", self.losstreak, "LossStreakAccum:", self.losstreakaccum)


        if (self.losstreak > self.maxlosestreak):
            self.maxlosestreak = self.losstreak

        if (self.winstreak > self.maxwinstreak):
            self.maxwinstreak = self.winstreak


        self.lastResult = self.thisResult

        print(self.name, "-> Stack: ", self.stack)

        if (self.stack < 0):
            print("No Money left!!!")
            return False
        else:
            return True    
        
        
        
    def print_summary(self):
        print ("=============Simulation Result================ Runs:", self.runs)
        print ("Wins:", self.wins, " Losses:", self.losses, " Push:", self.pushes)
        print ("Max Win Streak:", self.maxwinstreak, "Max Lose Streak:", self.maxlosestreak)
        print ("Average Win Streak:", self.winstreakaccum / self.numwinstreaks , "Average Loss Streak:", self.losstreakaccum / self.numlossstreaks)
        print ("totalGain: ", self.totalGain)
        print ("totalBet: ", self.totalBet)
        print ("Ratio: ", self.totalGain/self.totalBet)
        print ("Stack: ", self.stack)
        print ("maxStack: ", self.maxStack)

        