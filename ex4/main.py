from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print('=== DataDeck Tournament Platform ===')

    print('\nRegistering Tournament Cards...')
    dragon = TournamentCard("Fire Dragon", 3, "Legendary",
                            "dragon_001", 1200, 10, 5)
    wizard = TournamentCard("Ice Wizard", 3, "Legendary",
                            "wizard_001", 1150, 3, 1)
    tournament = TournamentPlatform()
    tournament.register_card(dragon)
    tournament.register_card(wizard)

    print("\nCreating tournament match...")
    print('Match result: '
          f'{tournament.create_match("dragon_001", "wizard_001")}')

    print('\nTournament Leaderboard:')
    sorted_cards = sorted(tournament.get_leaderboard(), key=lambda x: x.rating,
                          reverse=True)
    for i, card in enumerate(sorted_cards, start=1):
        print(f'{i}. {card.name} - Rating: {card.rating}'
              f' ({card.win}-{card.losses})')

    print('\nPlatform Report:')
    print(tournament.generate_tournament_report())
    print('=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!')


if __name__ == '__main__':
    main()
