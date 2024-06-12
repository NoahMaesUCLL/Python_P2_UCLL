from util import *

def group_by_suit(cards):
    suits = {}

    for card in cards:
        if card.suit not in suits:
            suits[card.suit] = []
        
        suits[card.suit].append(card)

    return suits

def group_by_suit(cards):
    return group_by(cards, lambda card: card.suit)

def group_by_value(cards):
    values = {}

    for card in cards:
        if card.value not in values:
            values[card.value] = []

        values[card.value].append(card)

    return values

def group_by_value(cards):
    return group_by(cards, lambda card: card.value)

def partition_by_color(cards):
    black_cards = []
    red_cards = []

    black_suits = ["spades", "clubs"]

    for card in cards:
        if card.suit in black_suits:
            black_cards.append(card)
        else:
            red_cards.append(card)
    
    return (black_cards, red_cards)

def partition_by_color(cards):
    return partition(cards, lambda card: card.suit in ['clubs', 'spades'])