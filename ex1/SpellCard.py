from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        info = super().play(game_state)
        if game_state['action'] == 'summon':
            info.update(self.resolve_effect([]))
        return info

    def resolve_effect(self, targets: list) -> dict:
        return {'effect': f'Deal {self.cost} damage to target', 'targets': targets}
