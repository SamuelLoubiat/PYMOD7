from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return super().get_card_info()

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable(available_mana)

    def attack(self, target: str) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass
