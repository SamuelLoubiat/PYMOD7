from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self.cards = {}
        self.match = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.update({card.card_id: card})
        return f"Card {card.card_id} registered"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.cards.get(card1_id)
        c2 = self.cards.get(card2_id)
        self.match += 1
        if not isinstance(c1, TournamentCard) or not isinstance(c2,
                                                                TournamentCard):
            raise Exception('Invalid card type')

        while c1.health > 0 and c2.health > 0:
            res = c2.defend(c1.attack(c2.card_id)['attacks'])
            if res['health'] > 0:
                c1.defend(c2.attack(c1.card_id)['attacks'])

        winner = c1 if c1.health > 0 else c2
        loser = c2 if c1.health > 0 else c1

        rating_change = 16
        winner.rating += rating_change
        loser.rating -= rating_change

        winner.update_wins(1)
        loser.update_losses(1)
        return {
            'winner': winner.card_id,
            'loser': loser.card_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        lst = []
        for item in self.cards.values():
            lst.append(item)
        return lst

    def generate_tournament_report(self) -> dict:
        all_ratings = [c.rating for c in self.cards.values()]
        avg = sum(all_ratings) / len(all_ratings) if all_ratings else 0

        return {'total_cards': len(self.cards), 'matches_played': self.match,
                'avg_rating': int(avg), 'platform_status': 'active'}
