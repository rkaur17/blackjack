# Blackjack starter code

# Global constant for the winning number of cards
MAX = 21

# main function
def main():
    # Local variables
    hand1 = 0
    hand2 = 0
    value_1 = 0
    value_2 = 0
    card_1 = 0
    card_2 = 0
    deck = create_deck()

    while hand1 <= MAX:
        card_1, value_1 = deck.popitem()
        print('Player 1 was dealt: ',card_1,':',value_1)
        hand1 = update_hand_value(hand1, value_1, card_1)
        card_2, value_2 = deck.popitem()
        print('Player 2 was dealt: ',card_2,':',value_2)
        hand2 = update_hand_value(hand2, value_2, card_2)
    print("Value of Player 1's hand: ",hand1)
    print("Value of Player 2's hand: ",hand2)

    if hand1 > MAX and hand2 > MAX:
        print('There is no winner. ')
    elif hand1 > MAX and hand2 <= MAX:
        print('Player 2 wins! ')
    else:
        print('Player 1 wins! ')


# The create_deck function creates a deck of cards and
# returns the deck.
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}
    new_dictionary = {}

    for suit in suits:
        for key in special_values:
            special = key + 'of' + suit
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

    return deck

def update_hand_value(hand, value, card):
    if "Ace" in card_1:
        hand1 = hand1 + 1
    else:
        hand1+=int(value_1)
    return hand1
  

# Call the main function.
main()

