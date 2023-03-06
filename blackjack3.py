# Blackjack starter code
import random
# Global constant for the winning number of cards
MAX = 21

# main function
def main():
    # Local variables
    hand1 = 0
    hand2 = 0
    deck = create_deck()
    deal = True

    while deal:
        print("Player 1's turn")
        #num_cards = int(input('Would you like another card? 1.Yes 2.No '))

        #if num_cards == 1:
        hand1 = deal_cards(deck,hand1)
        print('Value of Player 1 hand:', hand1)


        print("Player 2's turn")
        #num_cards = int(input('Would you like another card? 1.Yes 2.No '))
       # if num_cards == 1:
        hand2 = deal_cards2(deck,1,hand2)
        print('Value of Player 2 hand:', hand2)

        if hand1 > 21 and hand2 > 21:
            print("There is no winner")
            deal = False
        elif hand1 > 21:
            print("Player 2 wins")
            deal = False
        elif hand2 > 21:
            print("Player 1 wins")
            deal = False
        else:
            print()

    #TODO - Deal a card to each player and calculate hand value. 
    #Print 'Player 1 was dealt...'
    #Print 'Player 2 was dealt...



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
    new_dictionary = {}

    for suit in suits:
        for key in special_values:
            special = key +'of' + suit
            new_dictionary.update({special:special_values[key]})
    # Create list of all the card values
    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    # Initialize deck
    deck = {}
    for suit in suits:
        for num in numbers:
            if num.isdigit() == False:
                deck.update(new_dictionary)
            elif num.isdigit() == True:
                number = str(num) + 'of' + suit
                deck[number] = num
                deck.update({number:deck[number]})
            #TODO Add the numbers 2-10 to the deck [Hint: you will need to check if the value is numeric]

            #TODO Add the Ace, King, Queen, or Jack values to the deck
    return deck

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value += value

    # Display the value of the hand.
    print('Value of this hand:', hand_value)

def deal_cards2(deck, number, hand):
    # Initialize an accumulator for the hand value.
    hand_value = hand

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
        card, value = random.choice(list(deck.items()))
        print("Player 2 was dealt: ",card)
        hand_value += value

    # Display the value of the hand.
    return hand_value


# TODO Given the player's current hand, the value of the card they were just dealt
# and the name of the card they were just dealt, return the new value of their hand 
# Remember: If a player is dealt an ace, the program should decide the value by:
# The ace will be worth 11 points, uless that makes the player's hand exceed 21 points.
# In that case the ace will be worth 1 point.
#def update_hand_value(hand, value, card):
  

# Call the main function.
main()
