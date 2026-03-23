from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, card_id: str,
                 rating: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.health = health
        self.win = 0
        self.losses = 0
        print(f"\n{name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {rating}")
        print(f"- Record: {self.win}-{self.losses}")

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return super().get_card_info()

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable(available_mana)

    def attack(self, target: str) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage * 0.8
        if self.health <= 0:
            return {'health': 0}
        return {'health': self.health}

    def get_combat_stats(self) -> dict:
        pass

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.win += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        pass
