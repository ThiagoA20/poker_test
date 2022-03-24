from enum import Enum


class Result(Enum):
    LOSS: int = 0
    WIN: int = 1


def same_suit(hand: list) -> bool:
    """Store the value of the first suit, if every card has the same suit, return True, otherwise, the function will return False"""
    result = True
    initial_card: str = list(hand[0])[1]
    for card in hand:
        if list(card)[1] != initial_card:
            result = False
            break
    return result


def groups_amount(hand: list) -> dict:
    """Store the amount of groups of cards"""
    cards = {}
    for card in hand:
        if list(card)[0] in cards:
            cards[list(card)[0]] += 1
        else:
            cards[list(card)[0]] = 1
    return cards


def high_card(hand: list) -> str:
    """Return the card that have the highest number"""
    cards = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    highest = 1
    for card in hand:
        if cards[list(card)[0]] > highest:
            highest = cards[list(card)[0]]
    for card in cards:
        if cards[card] == highest:
            return card


def check_sequence(hand: list) -> list[bool, bool]:
    """Check if a sequence exists and if it's the highest"""
    cards = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    sequence = []
    for card in hand:
        sequence.append(cards[list(card)[0]])
    sequence.sort()
    result = []
    i = 0
    while i < len(sequence) - 1:
        if sequence[i] + 1 != sequence[i + 1]:
            result.append(False)
            break
        i += 1
    if len(result) == 0:
        result.append(True)
    if result[0] == True and 13 in sequence:
        result.append(True)
    else:
        result.append(False)
    return result



class PokerHand:
    
    def __init__(self, hand: str):
       self.hand = hand.split(" ")
       self.same_suit: bool = same_suit(self.hand)
       self.groups_amount: dict = groups_amount(self.hand)
       self.highest_card: str = high_card(self.hand)
       self.check_sequence: list[bool, bool] = check_sequence(self.hand)


    def classificate(self, highestSum=False) -> int:
        """Check the parameters of the hand and return the class"""
        result = {"ROYAL_STRAIGHT_FLUSH": 1, "STRAIGHT_FLUSH": 2, "FOUR_OF_A_KIND": 3, "FULL_HOUSE": 4, "FLUSH": 5, "STRAIGHT": 6, "THREE_OF_A_KIND": 7, "TWO_PAIR": 8, "ONE_PAIR": 9}
        cards = {"2": 13, "3": 12, "4": 11, "5": 10, "6": 9, "7": 8, "8": 7, "9": 6, "T": 5, "J": 4, "Q": 3, "K": 2, "A": 1}
        if highestSum == True:
            cardSum = [cards[list(card)[0]] for card in self.hand]
            return sum(cardSum)
        if self.same_suit == True:
            if self.check_sequence[0] == True and self.check_sequence[1] == True:
                return result["ROYAL_STRAIGHT_FLUSH"]
            elif self.check_sequence[0] == True and self.check_sequence[1] == False:
                return result["STRAIGHT_FLUSH"]
            else:
                return result["FLUSH"]
        else:
            if self.check_sequence[0] == True:
                return result["STRAIGHT"]
            else:
                four = 0
                three = 0
                two = 0
                for card in self.groups_amount:
                    if self.groups_amount[card] == 4:
                        four = 1
                    elif self.groups_amount[card] == 3:
                        three += 1
                    elif self.groups_amount[card] == 2:
                        two += 1
                if four == 1:
                    return result["FOUR_OF_A_KIND"]
                elif three == 1 and two == 1:
                    return result["FULL_HOUSE"]
                elif three == 1 and two == 0:
                    return result["THREE_OF_A_KIND"]
                elif two == 2:
                    return result["TWO_PAIR"]
                elif two == 1:
                    return result["ONE_PAIR"]
                else:
                    return cards[self.highest_card] + 9


    def compare_with(self, hand2: object):
        """Return result LOSS(0) if the hand2 is high than the hand1, otherwise, return WIN(1)"""

        if hand2.classificate() < self.classificate():
            comparision_result: object = Result(value=0)
        elif hand2.classificate() == self.classificate():
            if hand2.classificate(highestSum=True) < self.classificate(highestSum=True):
                comparision_result: object = Result(value=0)
            else:
                 comparision_result: object = Result(value=1)
        else:
            comparision_result: object = Result(value=1)
        return comparision_result
    

# poker_hand_1 = PokerHand("TC TH 5C 5H TH")
# print(poker_hand_1.classificate())
# poker_hand_2 = PokerHand("9C 9H 5C 5H AC")
# print(poker_hand_2.classificate())

# print(poker_hand_1.compare_with(poker_hand_2) == Result.WIN)