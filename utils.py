__author__ = 'monica_wang'

from treys import Card as tCard

class CalculateHands:
    def __init__(self, dealer, player, community):
        self.dealer = dealer
        self.player = player
        self.community = community

    def comparePlayerWin(self):

        return True

    def dealerQualifies(dealer, community):

        return True

    def gainFromBlindBet(player, community, blind):

        return blind

    def converToTreys(hand):

        _temp = [str(c).replace('♥', 'h').replace('♣', 'c').replace('♦', 'd').replace('♠', 's') for c in  hand]
        tHand = [tCard.new(d) for d in _temp]
        return tHand








