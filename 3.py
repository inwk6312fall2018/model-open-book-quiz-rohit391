def deal_cards(self, number: int):
    for _ in range(0, number):
        for player in self.players:
            card = self.deck.draw()
            player.hand.append(card)
            print("Dealt {} to player {}".format(card, player))

deal_cards()

     
