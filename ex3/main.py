from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory

def main():
    print('=== DataDeck Game Engine ===')
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print('\nConfiguring Fantasy Card Game...')
    print(f'Factory: {factory.__class__.__name__}')
    print(f'Strategy: {strategy.__class__.__name__}')
if __name__ == "__main__":
    main()