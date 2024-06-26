
from poker import Card
from poker import Rank
from poker import Hand
from poker import Suit
import utils
from treys import Evaluator

def round1Bet(hand):


    if len(hand) != 2:
        raise Exception("wrong number of hand")
    hcard, lcard = sorted(hand, reverse=True)


    # print('hcard:', hcard)
    # print('lcard:', lcard)
    if hcard.rank == Rank('A'):
        # print("R1: ACE!!!")
        return 4.0
    
    if ( (hcard.rank == Rank('K')) and (lcard.rank > Rank('4'))):
        # print('R1: KING + 5 or better!!!')
        return 4.0

    if ( (hcard.rank == Rank('K')) and (hcard.suit == lcard.suit) ):
        # print('r1: KING + Suited !!!')
        return 4.0

    if hcard.rank == lcard.rank: # Pair
        if hand == Hand('22'):
            # print('Pocket Duces!!!!')
            return 0.0
        else:
            # print('R1: Pocket Pair!!!!')
            # print('hcard:', hcard)
            # print('lcard:', lcard)
            return 4.0        

    if (hcard.rank == Rank('Q') and ((lcard.rank > Rank('7'))  or ((hcard.suit == lcard.suit) and (lcard.rank > Rank('5'))))):
        # print('you have a Queen!!!')
        return 4.0

    if (hcard.rank == Rank('J') and ((lcard.rank > Rank('9'))  or ((hcard.suit == lcard.suit) and (lcard.rank > Rank('7'))))):
        # print('you have a Queen!!!')
        return 4.0    
    # if hcard.getRank() == 'J' and (Card.VALUES[lcard.getRank()] > 9 or (hcard.getSuit() == lcard.getSuit()) and Card.VALUES[lcard.getRank()] > 7):
    
    return 0.0


def round2Bet(hand, community):
    _eval = Evaluator()
    if len(hand) != 2 or len(community) != 3:
        raise Exception("wrong number of hand")

    
    _hand = utils.CalculateHands.converToTreys(hand)
    _community = utils.CalculateHands.converToTreys(community)
    _current = _eval.evaluate(_community, _hand)
    _class = _eval.get_rank_class(_current)

    current = hand + community

    # print("Class:", _class)
    
    #strieght or better.
    if (_class <= 6): # strieght
        return 2.0
    
    #Two pair or better.
    if (_class == 7): # two pair
        # print('Two Pair')
        for c in hand:
            for xx in community:
                if c.rank == xx.rank:
                    return 2.0
        return 0.0

    #Hidden pair*, except pocket deuces.
    if _class == 8: # Pair
        if hand == Hand('22'):
            # print('Pocket Duces!!!!')
            return 0.0
        else:
            for c in hand:
                 for xx in community:
                    if c.rank == xx.rank:                      
                        return 2.0
            return 0.0

    #Four to a flush, including a hidden 10 or better to that flush
    suits = [s.suit for s in current]
    for x in list(Suit):
        # print('Suits:', suits.count(x), x) 
        if suits.count(x) >= 4:
            if (hand[0].suit == x and hand[0].rank >= Rank('T')) or  (hand[1].suit == x and hand[1].rank >= Rank('T')):
                # print('Four to a flush, including a hidden 10 or better to that flush')
                # print ("Player: " + ", ".join([str(c) for c in hand]))
                # print ("Community: " + ", ".join([str(c) for c in community]))
                return 2.0
    return 0.0

def round3Bet(hand, community):
    _eval = Evaluator()
    if len(hand) != 2 or len(community) != 5:
        raise Exception("wrong number of hand")

    _hand = utils.CalculateHands.converToTreys(hand)
    _community = utils.CalculateHands.converToTreys(community)
    _current = _eval.evaluate(_community, _hand)
    _class = _eval.get_rank_class(_current)

    current = hand + community

    # print("Rd3 Class:", _class)
    # Hidden pair or better.
    if (_class <= 8): # pair
        for c in hand:
            for xx in community:
                if c.rank == xx.rank:                      
                    return 1.0
                    
        return 0.0

    # #Less than 21 cards dealer outs beat you
    # minCardRankValueinHand = min([Card.VALUES[c.getRank()]for c in current.hand])
    # numOfCardsPairDealer = 15   # num of cards that can pair dealer to beat you (since you don't have hidden pair)
    # if current.type == HandType.PAIR:
    #     numOfCardsPairDealer = 12

    # numOfCardsLarger = 0
    # hcard, lcard = sorted(playhand, key=lambda c: Card.VALUES[c.getRank()])
    # trial = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    # for t in trial:
    #     if Card.VALUES[t] > Card.VALUES[hcard.getRank()] and Card.VALUES[t] > minCardRankValueinHand:
    #         numOfCardsLarger += 1
    # numOfCardsLarger *= 4

    # if numOfCardsLarger + numOfCardsPairDealer < 21:
    #     return 1.0
    # else:
    #     return 0.0

    return 0.0