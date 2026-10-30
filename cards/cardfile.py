SUITS: list[str] = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS: list[int] = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
]

class Card:
    def __init__(self, rank: int, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return (
            self.rank_index == other.rank_index
        )

    def __lt__(self, other: "Card") -> bool:
        return self.rank_index < other.rank_index

    def __gt__(self, other: "Card") -> bool:
        return self.rank_index > other.rank_index

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
