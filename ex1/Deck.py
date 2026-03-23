import random
from typing import List

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class DeckError(Exception):
    pass


class Deck:

    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) < 1:
            raise DeckError("Cannot Draw empty cards list")
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        total_cost: int = 0
        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard):
                spells += 1
        if len(self.cards) > 0:
            avg = total_cost / len(self.cards)
        else:
            avg = 0
        return {'total_cards': len(self.cards), 'creatures': creatures,
                'spells': spells, 'artifacts': artifacts,
                'avg_cost': avg}
