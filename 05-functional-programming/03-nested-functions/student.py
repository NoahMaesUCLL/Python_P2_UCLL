from util import *

def count_older_than(people, min_age):
    def is_older(person):
        return person.age >= min_age 

    return count(people, is_older)

def indices_of_cards_with_suit(cards, suit):
    def has_suit(card):
        return card.suit == suit
    
    # indicies = []
    # for i in range(len(cards)):
    #     if has_suit(cards[i]):
    #         indicies.append(i)

    # return indicies

    return indices_of(cards, has_suit) 