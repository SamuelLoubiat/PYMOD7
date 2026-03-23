from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    print('=== DataDeck Game Engine ===')
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game_engine = GameEngine()
    game_engine.configure_engine(factory, strategy)

    print('\nConfiguring Fantasy Card Game...')
    print(f'Factory: {factory.__class__.__name__}')
    print(f'Strategy: {strategy.get_strategy_name()}')
    print(f'Available types: {factory.get_supported_types()}')

    print('\nSimulating aggressive turn...')
    turn_info = game_engine.simulate_turn()
    print(f"Hand: {turn_info['hand']}")

    print("\nTurn execution:")
    print(f"Strategy: {turn_info['strategy']}")
    print(f"Actions: {turn_info['actions']}")

    print("\nGame Report:")
    print(game_engine.get_engine_status())

    print(
        '\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!')


if __name__ == "__main__":
    main()
