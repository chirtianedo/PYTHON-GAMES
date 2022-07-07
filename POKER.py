#["Hearts", "Diamonds", "Spades", "Clubs"]

#["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#"A of Clubs"
from random import shuffle

class Card:
    def __init__ (self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
       return f"{self.value} of {self.suit}"

c= Card("A", "Heart")
c2 = Card("10", "Spades")



class Deck:
    def __init__ (self):
        suits=["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        self.cards=[Card(value, suit) for suit in suits for value in values]
#         for suit in suits:
#             for value in values:
#               self.cards.append(Card(value, suit))
#         print (self.cards)
    def __repr__(self):
        return f" Deck of {self.count()} cards"
    def __iter__ (self):
        return iter(self.cards)
    
    def count (self):
        return len(self.cards)
    
    def _deal (self, num):
        count = self.count() 
        actual = min([count, num])
        if count == 0:
            raise ValueError ("All Cards have been dealt")
        if num == 0:
            raise ValueError ("You cannot deal Zero cards, please try again")
        cards =  self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
