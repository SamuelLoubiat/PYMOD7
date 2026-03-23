from ex2.EliteCard import EliteCard


def main() -> None:
    print('=== DataDeck Ability System ===')

    print('\nEliteCard capabilities:')
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    card = EliteCard('Arcane Warrior', 4, 'Legendary', 5, 10, {})
    print("\nCombat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f'Defense result: {card.defend(5)}')
    print('\nMagic phase:')
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy 1', 'Enemy 2'])}")
    print(f'Mana channel: {card.channel_mana(3)}')
    print('\nMultiple interface implementation successful!')


if __name__ == "__main__":
    main()
