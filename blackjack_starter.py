# Blackjack starter code

# Global constant for the winning number of cards
MAX = 21

# main function
def main():
    # Local variables
    hand1 = 0
    hand2 = 0
    deck = create_deck()

    #TODO - Deal a card to each player and calculate hand value. 
    #Print 'Player 1 was dealt...'
    #Print 'Player 2 was dealt...'



    #TODO Determine the winner.
    #Print either:
    #Print 'There is no winner' or
    #'Player 1 wins' or
    #'Player 2 wins'


# The create_deck function creates a deck of cards and
# returns the deck.
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    # Create list of all the card values
    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    # Initialize deck
    deck = {}
    for suit in suits:
        for num in numbers:
            #TODO Add the numbers 2-10 to the deck [Hint: you will need to check if the value is numeric]

            #TODO Add the Ace, King, Queen, or Jack values to the deck
    return deck

# TODO Given the player's current hand, the value of the card they were just dealt
# and the name of the card they were just dealt, return the new value of their hand 
# Remember: If a player is dealt an ace, the program should decide the value by:
# The ace will be worth 11 points, uless that makes the player's hand exceed 21 points.
# In that case the ace will be worth 1 point.
def update_hand_value(hand, value, card):
  

# Call the main function.
main()


