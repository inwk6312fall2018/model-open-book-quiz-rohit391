     
def deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'A': 'Ace','2':'Two','3':'Three','4':'Four','5':'Five','6': 'Six','7': 'Seven','8': 'Eight',
             '9': 'Nine','10': 'Ten','J': 'Jack','Q': 'Queen','K': 'King'}
    cards = []
    for suit in suits:
        for rank,name in ranks.items():
            cards.append(list((suit, rank, name)))
    print('Generated deck of cards for the table')
    print(cards)
    

deck()
