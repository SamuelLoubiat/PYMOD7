from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, card_id: str,
                 rating: int, health: int, attacks: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.health = health
        self.attacks = attacks
        self.win = 0
        self.losses = 0
        print(f"\n{name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {rating}")
        print(f"- Record: {self.win}-{self.losses}")

    def play(self, game_state: dict) -> dict:
        return {'card_id': self.card_id, 'action': 'played', 'game_state': game_state}

    def get_card_info(self) -> dict:
        return super().get_card_info()

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable(available_mana)

    def attack(self, target: str) -> dict:
        return {'target': target, 'attacks': self.attacks}

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage * 0.8
        if self.health <= 0:
            return {'health': 0}
        return {'health': self.health}

    def get_combat_stats(self) -> dict:
        return {'health': self.health, 'attacks': self.attacks}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.win += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {'card_id': self.card_id, 'rating': self.rating, 'win': self.win, 'losses': self.losses}

    def get_tournament_stats(self) -> dict:
        return self.get_rank_info()
