from scipy.stats import hypergeom

class MTGManabaseBuilder:
    """
    Instantiate a Manabase Builder.
    
    :param deck_size: size of the deck we want to build a manabase
    :type deck_size: int
    """

    def __init__(self, deck_size):
        self.deck_size = deck_size
        
        self.on_the_play = 7
        self.on_the_draw = 8

    def calculate_hypergeom(self, M, n, N, k):
        """
        Calculate a the Hyper Geometric Distribution for a given set of values (M, n, N)
        
        :param M: The collection size.
        :type number: int

        :param n: The quantity of elements that satisfy the condition you are looking for on the collection.
        :type number: int

        :param N: The quantity of N random elements we are picking from the collection.
        :type number: int

        :param k: The quantity of elements you want that satisfy the condition on the N random elements.
        :type number: int

        Example:
        M = 60  # Total number of cards
        n = 26  # Number of Type I cards (e.g. Swamps) 
        N = 7   # Number of draws (7 cards when you are on the play)
        k = 3   # Number of Type I cards we want in one hand
    
        :return: A probability for the k conditions to be met
        :rtype: int
        """
        rv = hypergeom(M, n, N)
        p = rv.pmf(k)
        return p