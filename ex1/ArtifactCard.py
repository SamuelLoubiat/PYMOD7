from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        info = super().play(game_state)
        if game_state['action'] == 'summon':
            info.update(self.activate_ability())
        return info

    def activate_ability(self) -> dict:
        return {'effect': self.effect}
