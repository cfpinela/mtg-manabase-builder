from enum import Enum

class DeckDistribution:
    """
    Instantiate a Deck Distribution Class.

    :param deck_size: size of the deck we want to build a manabase
    :type deck_size: int

    :param deck_dict: dictionary representing the different 
    :type deck_dict: dict
    """

    def __init__(self, deck_size):
        self.deck_size = deck_size

class CardType(Enum):
    Land = 1
    Creature = 2
    Artifact = 3
    Enchantment = 4
    Planeswalker = 5
    Instant = 6
    Sorcery = 7


class MTGCard:
    """
    Instantiate a representation of a MTG Card for the deck distribution
    
    :param card_name: Name of the card
    :type card_name: str

    :param is_permanent: True or False if the card is a permanent
    :type is_permanent: boolean
    """

    def __init__(self, card_name, is_permanent):
        self.card_name = card_name
        self.is_permanent = is_permanent