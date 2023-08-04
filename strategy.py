
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

    print('hcard:', hcard)
    print('lcard:', lcard)
    if hcard.rank == Rank('A'):
         print("You have an ACE!!!")
         return 4.0
    
    if (hcard.rank == Rank('K') and ((lcard.rank > Rank('4'))  or (hcard.suit == lcard.suit))):
        print('you have a KING!!!')
        return 4.0

    if (hcard.rank == Rank('Q') and ((lcard.rank > Rank('7'))  or ((hcard.suit == lcard.suit) and (lcard.rank > Rank('5'))))):
        print('you have a Queen!!!')
        return 4.0

    if (hcard.rank == Rank('J') and ((lcard.rank > Rank('9'))  or ((hcard.suit == lcard.suit) and (lcard.rank > Rank('7'))))):
        print('you have a Queen!!!')
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
    
    #Two pair or better.
    if (_class <= 7): # two pair
        # print('Two Pair or better!!!!')
        return 2.0

    #Hidden pair*, except pocket deuces.
    if _class == 8: # Pair
        if hand == Hand('22'):
            # print('Pocket Duces!!!!')
            return 0.0
        else:
            # print('Hidden Pair!!!!')
            return 2.0

    #Four to a flush, including a hidden 10 or better to that flush
    suits = [s.suit for s in current]
    for x in list(Suit):
        # print('Suits:', suits.count(x), x) 
        if suits.count(x) >= 4:
            if (hand[0].suit == x and hand[0].rank >= Rank('T')) or  (hand[1].suit == x and hand[1].rank >= Rank('T')):
                # print('Four to a flush, including a hidden 10 or better to that flush')
                return 2.0
    return 0.0

def round3Bet(playhand, community):
    _eval = Evaluator()
    if len(playhand) != 2 or len(community) != 5:
        raise Exception("wrong number of hand")

    _hand = utils.CalculateHands.converToTreys(playhand)
    _community = utils.CalculateHands.converToTreys(community)
    _current = _eval.evaluate(_community, _hand)
    _class = _eval.get_rank_class(_current)

    current = playhand + community

    # print("Rd3 Class:", _class)
    # Hidden pair or better.
    if (_class <= 8): # pair
        return 1.0

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