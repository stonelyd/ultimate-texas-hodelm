'''
Royal flush	500 to 1
Straight flush	50 to 1
Four of a kind	10 to 1
Full house	3 to 1
Flush	3 to 2
Straight	1 to 1
'''

#     MAX_TO_RANK_CLASS: dict[int, int] = {
#         MAX_ROYAL_FLUSH: 0,
#         MAX_STRAIGHT_FLUSH: 1,
#         MAX_FOUR_OF_A_KIND: 2,
#         MAX_FULL_HOUSE: 3,
#         MAX_FLUSH: 4,
#         MAX_STRAIGHT: 5,
#         MAX_THREE_OF_A_KIND: 6,
#         MAX_TWO_PAIR: 7,
#         MAX_PAIR: 8,
#         MAX_HIGH_CARD: 9
#     }

class BlindBet:
    Table = {
            9: 0.0,
            8: 0.0,
            7: 0.0,
            6: 0.0,
            5: 1.0,
            4: 1.5,
            3: 3.0,
            2: 10.0,
            1: 50.0,
            0: 500.0
    }


