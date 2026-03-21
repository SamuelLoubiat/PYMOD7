from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return CreatureCard()

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        pass