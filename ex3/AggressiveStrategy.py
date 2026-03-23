from ex0.CreatureCard import CreatureCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        playable_cards = sorted(hand, key=lambda x: getattr(x, 'cost', 0))

        cards_played = []
        mana_limit = 5
        total_damage = 0
        mana_used = 0

        for card in playable_cards:
            if isinstance(card,
                          CreatureCard) and mana_used + card.cost < mana_limit:
                cards_played.append(card.name)
                mana_used += card.cost
                total_damage += card.attack

        target_attacked = self.prioritize_targets(battlefield)
        if len(target_attacked) == 0:
            target_attacked = battlefield

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": target_attacked,
                "damage_dealt": total_damage
            }
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return [creature for creature in available_targets if
                isinstance(creature, CreatureCard)]
