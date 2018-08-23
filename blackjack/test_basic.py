import unittest
from lib import classes

class TestLib(unittest.TestCase):

    def test_card(self):
        deck_list = []
        total_value = 0

        for suit in classes.suits:
            for rank in classes.ranks:
                deck_list.append(classes.Card(suit, rank))

        for card in deck_list:
            total_value += card.value

        self.assertEqual(total_value, 380)

    def test_hand(self):
        hand = classes.Hand("tester")
        ace_spades = classes.Card("Spades", "Ace")
        queen_hearts = classes.Card("Hearts", "Queen")
        hand.add_card(ace_spades)
        hand.add_card(queen_hearts)

        early_value = hand.value

        three_clubs = classes.Card("Clubs", "Three")
        hand.add_card(three_clubs)

        self.assertEqual(early_value - hand.value, 7)


if __name__ == '__main__':
    unittest.main()