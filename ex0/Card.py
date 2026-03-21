from abc import ABC, abstractmethod
from enum import Enum


class CardError(Exception):
    pass


class CardRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if name == "":
            raise CardError("name cannot be empty")
        self.name = name
        if cost <= 0:
            raise CardError("cost cannot be zero or negative")
        self.cost = cost
        if rarity not in [r.value for r in CardRarity]:
            raise CardError(
                f"Invalid rarity. Must be one of:"
                f" {[r.value for r in CardRarity]}")
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name, 'mana_used': self.cost}

    def get_card_info(self) -> dict:
        return {'name': self.name, 'cost': self.cost, 'rarity': self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
