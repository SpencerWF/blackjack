import classes

def take_bet(chips):
    """

    """
    successful_bet = True
    while successful_bet:
        bet_amount = input("How much do you wish to bet? ")
        successful_bet = chips.make_bet(bet_amount)

def take_hit(deck, hand):
    """
    Adds a card to the player's hand, adjustments for aces are done in the class
    """
    hand.add_card(deck.deal())

def player_action(deck, hand):
    playing = True

    while True:
        action = input("Do you wish to hit, or stand? (h/s) ")

        if action[0].lower() == "h":
            take_hit(deck, hand)

        elif action[0].lower() == "s":
            print("Player Stands Dealer's Turn.")
            playing = False

        else:
            print("Not an action, please retry.")
            continue
        break

    return playing


def show_some(player, dealer):
    print("Dealer is showing the {}".format(dealer.hand_cards[0].__str__()))
    print("The dealer has 1 card hidden")
    print(player.__str__())

def show_all(player, dealer):
    print(dealer.__str__())
    print(player.__str__())


def player_busts(player, dealer, chips):
    chips.bet = 0
    print("Unfortunately you have busted.  Your total is {}.".format(chips.total))

def player_wins(Player, dealer, chips):
    chips.win_bet()
    print("Congratulations, you won! Your new total is {}.".format(chips.total))

def dealer_busts(player, dealer, chips):
    chips.win_bet()
    print("Congratulations, you won! The dealer busted. Your new total is {}.".format(chips.total))

def dealer_wins(player, dealer, chips):
    chips.bet = 0
    print("The dealer has won. Your total is {}.".format(chips.total))

def push(player, dealer, chips):
    chips.return_bet()
    print("There was a push.  Your bet is returned, your total is {}.".format(chips.total))