"""
Ordem: VALOR+NAIPE
Valores: 2, 3, 4, 5, 6, 7, 8, 9, T(10), J(valete), Q(rainha), K(rei), A(ace).
Naipes: S(espadas), H(copas), D(ouros), C(paus).

1. ROYAL STRAIGHT FLUSH = 5 maiores valores com o mesmo naipe
2. STRAIGHT FLUSH = 5 cartas com valores em sequência com o mesmo naipe
3. FOUR OF A KIND = 4 cartas com o mesmo valor
4. FULL HOUSE = um trio de cartas com o mesmo valor e uma dupla com o mesmo valor
5. FLUSH = 5 cartas com o mesmo naipe, mas não em sequência
6. STRAIGHT = 5 cartas com valores em sequência
7. THREE OF A KIND = três cartas com o mesmo valor
8. TWO PAIR = dois pares de cartas com o mesmo valor
9. ONE PAIR = um par de cartas com o mesmo valor
10. HIGH CARD = carta com maior valor das 5

verificar se todos tem o mesmo naipe:
1. maior sequência --> ROYAL STRAIGHT FLUSH
2. sequencia --> STRAIGHT FLUSH
3. sem sequência --> FLUSH

verificar quantas cartas são iguais:
- fazer um loop para adicionar em um dicionário, se a chave já existir acrescenta +1, se não, cria a chave
- verificar se existe um quarteto --> FOUR OF A KIND
- verificar se existe um trio e uma dupla --> FULL HOUSE
- verificar se existem duas duplas --> TWO PAIR
- verificar se existe uma dupla --> ONE PAIR

verificar maior carta do mão:
- carta com maior valor das 5 --> HIGH CARD

enum
multiprocessing
# code smell 1 -> too many parameters
# code smell 2 -> too deep nesting
# code smell 3 -> not the right structure
# code smell 4 -> wildcard imports
# code smell 5 -> not using main function
# code smell 6 -> using self when it's not needed
"""
from enum import Enum


class Result(Enum):
    LOSS: int = 0
    WIN: int = 1


class PokerHand:
    
    def __init__(self, hand: str):
       self.hand = hand.split(" ")

    
    def compare_with(self, hand2: str):
        "Return result LOSS(0) if the hand2 is high than the hand1, otherwise, return WIN(1)"
        
        comparision_result: object = Result(value=0)
        return comparision_result
    

poker_hand_1 = PokerHand("TC TH 5C 5H KH")
poker_hand_2 = PokerHand("9C 9H 5C 5H AC")

print(poker_hand_1.compare_with(poker_hand_2) == Result.LOSS)