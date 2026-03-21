from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, spell: dict) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self.health = health
        self.spell = spell

    def play(self, game_state: dict) -> dict:
        info = super().play(game_state)
        return info

    def attack(self, target: str) -> dict:
        return {'attacker': self.name, 'target': target,
                'damage': self._attack, 'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> dict:
        taken = int(incoming_damage / 2)
        return {'defender': self.name, 'damage_taken': taken,
                'damage_blocked': incoming_damage - taken,
                'still_alive': True}

    def get_combat_stats(self) -> dict:
        return {'attack': self._attack, 'health': self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {'caster': self.name, 'spell': spell_name, 'targets': targets,
                'mana_used': self.cost}

    def channel_mana(self, amount: int) -> dict:
        return {'channeled': amount, 'total_mana': 7}

    def get_magic_stats(self) -> dict:
        return {'spell_power': 10, 'mana_cost': self.cost}
