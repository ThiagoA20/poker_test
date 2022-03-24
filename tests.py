import unittest
from poker_game import *


class TestPokerGame(unittest.TestCase):

    def test_same_suit(self):
        self.assertTrue(same_suit(["TH", "TH", "5H", "5H", "KH"]))
        self.assertFalse(same_suit(["TC", "TH", "5C", "5H", "KH"]))
    
    def test_groups_amount(self):
        self.assertEqual(groups_amount(["TH", "TH", "5H", "5H", "KH"]), {"T": 2, "5": 2, "K": 1})
        self.assertEqual(groups_amount(["TH", "TH", "TH", "TH", "KH"]), {"T": 4, "K": 1})
        self.assertEqual(groups_amount(["TH", "TH", "TH", "5H", "5H"]), {"T": 3, "5": 2})
        self.assertEqual(groups_amount(["TH", "TH", "TH", "5H", "4H"]), {"T": 3, "5": 1, "4": 1})
        self.assertEqual(groups_amount(["TH", "TH", "KH", "5H", "4H"]), {"T": 2, "5": 1, "4": 1, "K": 1})
    
    def test_high_card(self):
        self.assertEqual(high_card(["TH", "TH", "5H", "5H", "KH"]), "K")
        self.assertEqual(high_card(["2H", "2H", "5H", "5H", "2H"]), "5")
        self.assertEqual(high_card(["TH", "AH", "5H", "5H", "KH"]), "A")
    
    def test_check_sequence(self):
        # Royal Straight flush
        self.assertEqual(check_sequence(["TS", "JS", "QS", "KS", "AS"]), [True, True])
        # Straight flush
        self.assertEqual(check_sequence(["9S", "TS", "JS", "QS", "KS"]), [True, False])
        # Without sequence
        self.assertEqual(check_sequence(["TS", "2S", "5S", "3S", "AS"]), [False, False])
    
    def test_classificate(self):
        # Royal Straight flush
        self.assertEqual(PokerHand("TS JS QS KS AS").classificate(), 1)
        # Straight flush
        self.assertEqual(PokerHand("7H 8H 9H TH JH").classificate(), 2)
        # Four of a kind
        self.assertEqual(PokerHand("AC AH AS AD KS").classificate(), 3)
        # Full house
        self.assertEqual(PokerHand("QC QH QC 5H 5H").classificate(), 4)
        # Flush
        self.assertEqual(PokerHand("4C 5C 9C TC JC").classificate(), 5)
        # Straight
        self.assertEqual(PokerHand("7C 8S 9S TC JC").classificate(), 6)
        # Three of a kind
        self.assertEqual(PokerHand("QH QC QD AD 8H").classificate(), 7)
        # Two pair
        self.assertEqual(PokerHand("TC TH 5C 5H KH").classificate(), 8)
        # One pair
        self.assertEqual(PokerHand("TS TD KC JC 7C").classificate(), 9)
        # High card
        self.assertEqual(PokerHand("AC 2H 5C 8H TH").classificate(), 10)


    def test_compare(self):
        # two pair x two pair
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5D 5S AC")) == Result.WIN)
        # one pair x one pair
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JD AS KC TH")) == Result.LOSS)
        # one pair x one pair
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7S JH TH 6D")) == Result.WIN)
        # one pair x two pair
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7H 5H 5C JS")) == Result.LOSS)
        # one pair x one pair
        self.assertTrue(PokerHand("AS AC KH 7D 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS)
        # royal straight flush x four of a kind
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("9C 9H 9S 9D KH")) == Result.WIN)
        # royal straight flush x straight
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JD QC KC AC")) == Result.WIN)
        # royal straight flush x three of a kind
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QC QD AD 8H")) == Result.WIN)
        # four of a kind x straight
        self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("9C TC JS QC KS")) == Result.WIN)
        # four of a kind x three of a kind
        self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("QH QS QC KD 8H")) == Result.WIN)
        # straight x three of a kind
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QD AS 8H")) == Result.WIN)
        # straight flush x four of a kind
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("KH KC KS KD TD")) == Result.WIN)
        # straight flush x flush
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4C 5C 9C TC JC")) == Result.WIN)
        # straight flush x straight
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9S TC JC")) == Result.WIN)


if __name__ == '__main__':
    unittest.main()