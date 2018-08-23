import classes
import functions
import random

playing = True

def main():
    global playing
    print("Welcome to Blackjack")

    player_name = input("What's your name? ")
    player_hand = classes.Hand(player_name)
    dealer_hand = classes.Hand("dealer")

    while True:
        try:
            player_total = int(input("How much are you bringing to the table? "))
            player_chips = classes.Chips(player_total)
            break
        except:
            print("We are sorry, this is an inappropriate value for your chips.")

    while True:
        deck = classes.Deck()
        deck.shuffle()

        functions.take_bet(player_chips)
        print("\n")

        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        functions.show_some(player_hand, dealer_hand)
        while playing:
            playing = functions.player_action(deck, player_hand)
            print("\n")
            functions.show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                functions.player_busts(player_hand, dealer_hand, player_chips)
                break
            


        if player_hand.value <= 21:
            functions.show_all(player_hand, dealer_hand)
            input("Press Enter to Continue ...")

            if dealer_hand.value < 17:
                print("The dealer has elected to hit:")
                dealer_hand.add_card(deck.deal())
                functions.show_all(player_hand, dealer_hand)
                input("Press Enter to Continue ...")

            if dealer_hand.value > 21:
                functions.dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                functions.dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value == player_hand.value:
                functions.push(player_hand, dealer_hand, player_chips)

            else:
                functions.player_wins(player_hand, dealer_hand, player_chips)

        if player_chips.total == 0:
            print("You have no more chips to play with, thank you for playing.")
            break

        action = input("Do you wish to play again? (y/n) ")

        if action[0].lower() == "n":
            break

        player_hand.clean_hand()
        dealer_hand.clean_hand()
        playing = True


if __name__ == '__main__':
    main()