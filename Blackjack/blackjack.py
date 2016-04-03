# RULES: see https://www.blackjackinfo.com/blackjack-rules/
# 4 decks, natural blackjack pays 3:2,
# insurance not offered, double after split is offered, repslit is not allowed
# dealer hits on a soft 17


## TODO: ...
# - figure out how to handle soft aces - soft means at least one ace is 11 not 1)
# - handle incorrect inputs (eg check type.. http://www.tldp.org/LDP/LG/issue83/evans.html)
# - handle blackjacks vs 21
# - handle double-down and splits
# - add a helper to get recommended move (eg: what are the probabilities?)
# - add a stats tracker, number of hands, number of wins


import pydealer
import time

BLACKJACK_RANKS = {
    "Ace": 11,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


deck1 = pydealer.Deck(ranks = BLACKJACK_RANKS)
deck2 = pydealer.Deck(ranks = BLACKJACK_RANKS)
deck3 = pydealer.Deck(ranks = BLACKJACK_RANKS)
deck4 = pydealer.Deck(ranks = BLACKJACK_RANKS)

stack = pydealer.Stack(ranks = BLACKJACK_RANKS)
stack += deck1
stack += deck2
stack += deck3
stack += deck4
stack.shuffle(times = 3)

player_hand = pydealer.Stack()
player_hand_split = pydealer.Stack()
dealer_hand = pydealer.Stack()

def hand_value(hand):
    value = 0
    aces_count = 0
    values_array= []
    best_value = 0
    for card in hand:
        value += BLACKJACK_RANKS[card.value]
        if card.value == "Ace":
            aces_count += 1
    values_array.append(value)
    best_value = value
    counter = aces_count
    while counter > 0:
        value -= 10
        values_array.append(value)
        if best_value > 21:
            best_value = value
        counter -= 1
    return { "best_value" : best_value, "possible_values" : values_array }

def hand_str(hand):
    return ', '.join( map(str, hand) )

def hand_value_str(hand):
    a = hand_value(hand)
    s = str(a["best_value"])
    if len(a["possible_values"]) > 1:
        s += " [possible values with aces: "
        s += ', '.join( map(str, a["possible_values"]) )
        s = s + "]"
    return s


player_bank = 1000
initial_bet = 0
continue_game = True

print "\n*** Blackjack ***"


while(continue_game == True):

    initial_bet = 0

    print "Your bank balance: " + str(player_bank)
    bet_repsonse = raw_input("How much do you bet? (Or hit 'q' to quit): ")
    if bet_repsonse == 'q':
        continue_game = 'False'
        break
    else:
        initial_bet = int(bet_repsonse)
        if initial_bet > player_bank:
            print "You can't bet more money than you have in the bank!"
            continue
        elif initial_bet == 0 or initial_bet < 0:
            print "You need to bet something to play!"
            continue
        else: player_bank = player_bank - initial_bet


    player_hand = stack.deal(num = 2, end = 'top')
    dealer_hand = stack.deal(num = 2, end = 'top')

    print "Your hand: " + hand_str(player_hand) + ". Total = " + hand_value_str(player_hand)
    print "Dealer upcard: " + str(dealer_hand[0]) + ". Total = " + str(BLACKJACK_RANKS[ dealer_hand[0].value ])



    # players turn:

    end_player_turn = False
    has_player_doubled = False

    while(end_player_turn == False):
        player_hand_value = hand_value(player_hand)
        # check if double-down or split is possible:
        if player_hand_value["best_value"] > 21:
             print "YOU ARE BUST!"
             end_player_turn = True
        elif player_hand_value["best_value"] == 21:
            end_player_turn = True
            if player_hand.size == 2:
                print "Your hand: Blackjack!"
        else :
            player_action = raw_input("Would you like to: Hit (h), Stand (s): ")  # double-down (d) or split (p):")
            if player_action == "s":
                end_player_turn = True
            elif player_action == "h":
                player_hand += stack.deal(num = 1, end = 'top')
            elif player_action == "d":
                has_player_doubled = True
        # if double down (only if you have two cards) - upto double the bet (or less) and get only one more card
        # if split, (only if a pair- any 10s is a pair) create two new hands from each card. deal another card to each
        #    spliting aces only gets one more card - and can't get a two card blackjack (just 21)
        #    double after split is possible
            else:
                print "please just type a letter"
        print "Your hand: " + hand_str(player_hand) + ". Total = " + hand_value_str(player_hand)


    time.sleep(1)


    # dealer turn:
    print ""
    end_dealer_turn = False

    while(end_dealer_turn == False):
        dealer_hand_value = hand_value(dealer_hand)
        if dealer_hand_value["best_value"] > 21: break
        print "Dealer hand: " + hand_str(dealer_hand) + ". Total = " + hand_value_str(dealer_hand)
        # if all player hands are bust, skip
        if dealer_hand_value["best_value"] > 21:
            print "DEALER IS BUST!"
            end_dealer_turn = True
        elif dealer_hand_value["best_value"] < 17:
            print "Dealer hits."
            dealer_hand += stack.deal(num = 1, end = 'top')
            print "Dealer hand: " + hand_str(dealer_hand) + ". Total = " + hand_value_str(dealer_hand)
        else:
            print "Dealer stands."
            end_dealer_turn = True
        time.sleep( 1 )


    # who won:
    player_hand_value = hand_value(player_hand)
    dealer_hand_value = hand_value(dealer_hand)

    if player_hand_value["best_value"] > 21:
        print "You lose (You are bust)"
    elif dealer_hand_value["best_value"] > 21:
        print "You win (Dealer is bust)"
        player_bank += (initial_bet * 2)
    elif player_hand_value["best_value"] > dealer_hand_value["best_value"]:
        print "You win (" + hand_value_str(player_hand) + " beats " + hand_value_str(dealer_hand) + ")"
        if player_hand.size == 2 and player_hand_value["best_value"] == 21:
            print "BLACKJACK! (Pays 3:2)"
            player_bank += int(initial_bet * 2.5)
        else:
            player_bank += (initial_bet * 2)
    elif player_hand_value["best_value"] < dealer_hand_value["best_value"]:
        print "You lose (" + hand_value_str(player_hand) + " loses to " + hand_value_str(dealer_hand) + ")"
    elif player_hand_value["best_value"] == dealer_hand_value["best_value"]:
        print "Push (you and dealer both have " + hand_value_str(player_hand) + ")"
        player_bank += initial_bet
    else:
        print "Something went wrong"


    if player_bank <= 0:
        print "\nOH NO! You ran out of money! Better luck next time."
        continue_game = False
    else:
        print "\nNext hand!"
        stack.add( player_hand.deal(num = player_hand.size) , end = 'bottom' )
        stack.add( dealer_hand.deal(num = dealer_hand.size) , end = 'bottom' )
