from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

from .Deck import Deck


def main() -> None:
    print('=== DataDeck Deck Builder ===')
    deck = Deck()
    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 8, 8)
    deck.add_card(dragon)
    lightning = SpellCard('Lightning Bolt', 4, 'Legendary', '')
    deck.add_card(lightning)
    mana = ArtifactCard('Mana Crystal', 3, 'Legendary', 8,
                        'Permanent: +1 mana per turn')
    deck.add_card(mana)
    print('\nBuilding deck with different card types...')
    print(f'Deck stats: {deck.get_deck_stats()}')
    print('\nDrawing and playing cards:')

    card = deck.draw_card()

    print(
        f"\nDrew {card.name} ({card.__class__.__name__.replace('Card', '')})")
    print(f"Play result: {card.play({'action': 'summon'})}")

    card = deck.draw_card()

    print(
        f"\nDrew {card.name} ({card.__class__.__name__.replace('Card', '')})")
    print(f"Play result: {card.play({'action': 'summon'})}")

    card = deck.draw_card()

    print(
        f"\nDrew {card.name} ({card.__class__.__name__.replace('Card', '')})")
    print(f"Play result: {card.play({'action': 'summon'})}")

    print(
        '\nPolymorphism in action: Same interface, different card behaviors!')


if __name__ == "__main__":
    main()
