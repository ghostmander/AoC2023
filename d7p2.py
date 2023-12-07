import requests
import os
from dotenv import load_dotenv

load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/7/input', cookies={"session": os.getenv("SESSION")}).text


# pinput = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """


def classify_hand(hand: str) -> int:
    def identify_type(dhand: str) -> int:
        card_counts = [hand.count(card) for card in '23456789TJQKA']
        if 5 in card_counts: return 6
        elif 4 in card_counts: return 5
        elif 3 in card_counts: return 3 + (2 in card_counts)
        else: return card_counts.count(2)
    return max(identify_type(hand.replace('J', c)) for c in '23456789TQKA')


def main(inp):
    transform_hand = lambda h: h.translate(str.maketrans('23456789TJQKA', 'ABCDEFGHIJKLM'))
    hands = [(hand, int(bet)) for hand, bet in (line.split() for line in inp)]
    hands.sort(key=lambda h: (classify_hand(h[0]), transform_hand(h[0])))
    total_winnings = sum((bet * i) for i, (*_, bet) in enumerate(hands, 1))
    print(total_winnings)


main(pinput.strip('\n').split('\n'))
