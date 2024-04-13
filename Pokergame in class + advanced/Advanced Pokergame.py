import random

class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank, must be one of {Card.RANKS}")
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit, must be one of {Card.SUITS}")
        self.rank = rank
        self.suit = suit

    def __gt__(self, other):
        return Card.RANKS.index(self.rank) > Card.RANKS.index(other.rank)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, count):
        if count > len(self.cards):
            raise ValueError("Not enough cards in the deck")
        drawn_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn_cards

    def return_cards(self, cards):
        self.cards.extend(cards)
        self.shuffle()

class Hand:
    def __init__(self, deck, num_cards=5):
        self.cards = deck.draw(num_cards)
        self.cards.sort()

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def evaluate_hand(self):
        if self.is_royal_flush():
            return "Royal Flush"
        if self.is_straight_flush():
            return "Straight Flush"
        if self.is_four_of_a_kind():
            return "Four of a Kind"
        if self.is_full_house():
            return "Full House"
        if self.is_flush():
            return "Flush"
        if self.is_straight():
            return "Straight"
        if self.is_three_of_a_kind():
            return "Three of a Kind"
        if self.is_two_pair():
            return "Two Pair"
        if self.is_pair():
            return "Pair"
        return "High Card"

    def hand_ranks(self):
        return [Card.RANKS.index(card.rank) for card in self.cards]

    def is_flush(self):
        suit = self.cards[0].suit
        return all(card.suit == suit for card in self.cards[1:])

    def is_straight(self):
        ranks = self.hand_ranks()
        return sorted(ranks) == list(range(min(ranks), min(ranks) + 5))

    def rank_counts(self):
        ranks = self.hand_ranks()
        return {rank: ranks.count(rank) for rank in set(ranks)}

    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_royal_flush(self):
        return self.is_straight_flush() and Card.RANKS.index(self.cards[0].rank) == 8

    def is_four_of_a_kind(self):
        return 4 in self.rank_counts().values()

    def is_three_of_a_kind(self):
        return 3 in self.rank_counts().values()

    def is_pair(self):
        return 2 in self.rank_counts().values()

    def is_two_pair(self):
        return list(self.rank_counts().values()).count(2) == 2

    def is_full_house(self):
        counts = self.rank_counts().values()
        return 3 in counts and 2 in counts

# Example of how to use the enhanced game:
deck = Deck()
hand = Hand(deck)
print(f"Hand: {hand}")
print(f"Hand Evaluation: {hand.evaluate_hand()}")
