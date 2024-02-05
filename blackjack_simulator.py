import random

# Cards
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Basic Strategy (includes splits and doubles)
def basic_strategy(player_hand, dealer_card):
    player_value = sum_hand(player_hand)
    if len(player_hand) == 2:
        if player_hand[0][0] == player_hand[1][0]:  # Possible split
            if player_hand[0][0] in ['8', 'Ace']:
                return 'split'
        if player_value in [9, 10, 11]:
            return 'double'
    if player_value < 12:
        return 'hit'
    if player_value == 12 and dealer_card[0] in ['2', '3']:
        return 'hit'
    if 13 <= player_value <= 16 and dealer_card[0] in ['7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
        return 'hit'
    return 'stand'

def sum_hand(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[0] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card[0] == 'Ace':
            value += 11
            aces += 1
        else:
            value += int(card[0])
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def play_hand(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player's turn
    action = basic_strategy(player_hand, dealer_hand[0])
    if action == 'split':
        hand1 = [player_hand[0], deck.pop()]
        hand2 = [player_hand[1], deck.pop()]
        if play_individual_hand(deck, hand1) == 'bust' and play_individual_hand(deck, hand2) == 'bust':
            return 'dealer'
    elif action == 'double':
        player_hand.append(deck.pop())
        if sum_hand(player_hand) > 21:
            return 'dealer'
    else:
        if play_individual_hand(deck, player_hand) == 'bust':
            return 'dealer'

    # Dealer's turn
    while sum_hand(dealer_hand) <= 16:
        dealer_hand.append(deck.pop())

    # Determine winner
    if sum_hand(dealer_hand) > 21:
        return 'player'
    if sum_hand(player_hand) > sum_hand(dealer_hand):
        return 'player'
    return 'dealer'

def play_individual_hand(deck, hand):
    while basic_strategy(hand, deck[-1]) == 'hit':
        hand.append(deck.pop())
        if sum_hand(hand) > 21:
            return 'bust'
    return 'stand'

wins = 0
# Run simulation x amount of tries
tries = 100000
for _ in range(tries):
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    if play_hand(deck) == 'player':
        wins += 1
print(f"Player won {wins} out of {tries} tries ({round((wins/tries) * 100, 2)}%)")


