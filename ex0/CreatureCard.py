from .Card import Card, CardError


class CreatureError(CardError):
    pass


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise CreatureError("attack cannot be zero or negative")
        if health <= 0:
            raise CreatureError("health cannot be zero or negative")
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({'type': 'Creature', 'attack': self.attack,
                     'health': self.health})
        return info

    def play(self, game_state: dict) -> dict:
        info = super().play(game_state)
        if game_state['action'] == 'summon':
            info.update({'effect': 'Creature summoned to battlefield'})
        return info

    def attack_target(self, target) -> dict:
        return {'attacker': self.name, 'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': target.health <= self.attack}
