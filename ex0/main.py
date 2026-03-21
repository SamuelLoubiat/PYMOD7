from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    card = CreatureCard('Fire Dragon', 5,
                        'Legendary', 7, 5)
    print(card.get_card_info())

    print('\nPlaying Fire Dragon with 6 mana available:')
    print(f'Playable: {card.is_playable(6)}')
    print(f"Play result: {card.play({'action': 'summon'})}")

    print('\nFire Dragon attacks Goblin Warrior:')
    goblin = CreatureCard('Goblin Warrior', 5,
                          'Legendary', 7, 5)
    print(f'Attack result: {card.attack_target(goblin)}')

    print('\nTesting insufficient mana (3 available):')
    print(f'Playable: {card.is_playable(3)}')

    print('\nAbstract pattern successfully demonstrated!')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
