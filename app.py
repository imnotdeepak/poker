# 1 player poker
# Game detects the value of your hand
# Output should show your final hand and the score
# Phase 1: player needs to choose two cards to get rid of to get the final score - completed
# Phase 2: system automatically finds the best score - in progress

import random

class Card (object):
    def __init__(self, name, value, suit, symbol):
        self.value = value
        self.suit = suit
        self.name = name
        self.symbol = symbol
        self.showing = False
    def __repr__(self):
        if self.showing:
            return self.symbol
        else:
            return "Card"

class Deck (object):
    def shuffle(self, times = 1):
        random.shuffle(self.cards)
        print("Deck shuffled")

    def deal(self):
        return self.cards.pop(0)

class StandardDeck(Deck):
    def __init__(self):
        self.cards = []
        suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
        values = {
                 "Two":2,
                 "Three":3,
                 "Four":4,
                 "Five":5,
                 "Six":6,
                 "Seven":7,
                 "Eight":8,
                 "Nine":9,
                 "Ten":10,
                 "Jack":11,
                 "Queen":12,
                 "King":13,
                 "Ace":14
                 }
        
        for name in values:
            for suit in suits:
                symbolIcon = suits[suit]
                if values[name] < 11:
                    symbol = str(values[name]) + symbolIcon
                else:
                    symbol = name[0] + symbolIcon
                self.cards.append(Card(name, values[name], suit, symbol))

    def __repr__(self):
        return "Standard deck of cards/n{0} cards remaining".format(len(self.cards))

class Player(object):
    def __init__(self):
        self.cards = []

    def cardCount(self):
        return len(self.cards)
    
class PokerScorer(object):
    def __init__(self, cards):
        if not len(cards) == 5:
            return "Error: Wrong number of cards"
        self.cards = cards

    def flush(self):
        suits = [card.suit for card in self.cards]
        if len(set(suits)) == 1:
            return True
        return False
    
    def straight(self):
        value = [card.value for card in self.cards]
        values.sort()

        if not len(set(values)) == 5:
            return False

        if value[4] == 14 and value[3] == 5 and value[2] == 4 and value[1] == 3 and value[0] == 2:
            return 5
        else: 
            if not value[0] + 1 == value[1]: return False
            if not value[1] + 1 == value[2]: return False
            if not value[2] + 1 == value[3]: return False
            if not value[3] + 1 == value[4]: return False

        return values[4]

    def highCardValue(self):
        value = [card.value for card in self.cards]
        highCard = None
        for card in self.cards:
            if highCard is None:
                highCard = card
            elif highCard.value < card.value:
                highCard = card
        return highCard

    def highestCount(self):
        count = 0
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) > count:
                count = values.count(value)
        return count

    def pairs(self):
        pairs = []
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2 and value not in pairs:
                pairs.append(value)

    def fourKind(self):
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 4:
                return True

    def fullHouse(self):
        two = False
        three = False

        values = [card.value for card in self.cards]
        if values.count(values) == 2:
            two == True
        elif values.count(values) == 3:
            three == True

        if two and three:
            return True

        return False

    def interpreterPoker():
        player = Player()

        points = 100
        handCost = 5

        end = False
        while not end:
            print("you have {0} points".format(points))
            print()

            points -= 5
            deck = StandardDeck()
            deck.shuffle()

            for i in range(5):
                player.addCard(deck.deal())

            for card in player.cards:
                card.showing = True
            print(player.cards)

            validInput = False
            while not validInput:
                print("Which cards do you want to discard?")
                print("Just hit return to hold, or type exit to fold")
                inputStr = input()

                if inputStr == "exit":
                    end = True
                    break

                try:
                    inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]

                    for inp in inputList:
                        if inp > 6:
                            continue
                        if inp < 1:
                            continue

                    for inp in inputList:
                        player.cards[inp-1] = deck.deal()
                        player.cards[inp-1].showing = True
                    
                    validInput = True

                except:
                    print("Input error: use commas to seperate the cards you want to hold")

            print(player.cards)
            score = PokerScorer(player.cards)
            straight = score.straight()
            flush = score.flush
            highestCount = score.highestCount
            pairs = score.pairs

            if straight and flish and straight == 14:
                print("You just got a royal flush!")
                points += 2000
            elif straight and flush:
                print("You just got a straight flush!")
                points += 500
            elif score == score.fourKind:
                print("You just got a four of a kind!")
                points += 250
            elif score == score.fullHouse:
                print("You just got a full house!")
                points += 150
            elif score == score.flush:
                print("You just got a flush")
                points += 25
            elif score == score.straight:
                print("You just got a straight")
                points += 20
            elif highestCount == 3:
                print("You just got a three of a kind")
                points += 15
            elif len(pairs) == 2:
                print("You just got a 2 pair")
                points += 10
            elif pairs and pairs[0] > 10:
                print("You just got a jack or higher")
                points += 5

            player.cards=[]
            print()

if __name__ == "__main__":
    game = PokerScorer()
    print(game.interpreterPoker())
