from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.total_cards = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        deck_data = self.factory.create_themed_deck(3)
        self.total_cards = len(deck_data['deck'])
        hand = deck_data['deck']
        formatted_hand = [f"{c.name} ({c.cost})" for c in hand]
        turn_result = self.strategy.execute_turn(hand, ['Enemy1'])
        turn_result['hand'] = formatted_hand
        self.turns_simulated += 1
        self.total_damage += turn_result['actions']['damage_dealt']

        return turn_result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name()
            if self.strategy else None,
            'total_damage': self.total_damage,
            'cards_created': self.total_cards,
        }
