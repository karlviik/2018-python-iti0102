"""Simple game of blackjack."""
from textwrap import dedent
import requests

BASE = "https://deckofcardsapi.com/api/deck"


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Construct object with given vars."""
        self.value = value
        self.suit = suit
        self.code = code

    def __repr__(self):
        """Print output."""
        return self.code


class Hand:
    """Simple class for holding hand information."""

    def __init__(self):
        """Construct with blank variables."""
        self.cards = []
        self.score = 0
        self.aces = 0

    def calculate_score(self, card):
        """Calculate score based on given rules."""
        if card.value.isdigit():
            addition = int(card.value)
        elif card.value != "ACE":
            addition = 10
        else:
            addition = 11
            self.aces += 1
        self.score += addition
        if self.score > 21 and self.aces:
            self.score -= 10
            self.aces -= 1

    def add_card(self, card: Card):
        """Add the new card to the hand and calculate new score."""
        self.cards.append(card)
        self.calculate_score(card)


class Deck:
    """Deck of cards. Provided via api over the network."""

    def __init__(self, shuffle=False):
        """
        Tell api to create a new deck.

        :param shuffle: if shuffle option is true, make new shuffled deck.
        """
        self.shufflecheck = shuffle
        if not shuffle:
            request = requests.get(f"{BASE}/new").json()
        else:
            request = requests.get(f"{BASE}/new/shuffle").json()
        self.deck_id = request["deck_id"]
        self.remaining = request["remaining"]
        self.is_shuffled = request["shuffled"]

    def shuffle(self):
        """Shuffle the deck."""
        self.is_shuffled = requests.get(f"{BASE}/{self.deck_id}/shuffle").json()["shuffled"]

    def draw(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        new_card = requests.get(f"{BASE}/{self.deck_id}/draw").json()["cards"]
        if new_card:
            new_card = new_card[0]
            return Card(new_card["value"], new_card["suit"], new_card["code"])
        return "aa" + 5

class BlackjackController:
    """Blackjack controller. For controlling the game and data flow between view and database."""

    def __init__(self, deck: Deck, view: 'BlackjackView'):
        """
        Start new blackjack game.

        :param deck: deck to draw cards from.
        :param view: view to communicate with.
        """
        self.deck = deck
        self.view = view
        if not self.deck.is_shuffled:
            self.deck.shuffle()
        self.player = Hand()
        self.dealer = Hand()
        self.state = {"dealer": self.dealer, "player": self.player}
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())
        self.player_loop()

    def player_loop(self):
        """Loop for player control, calls dealer loop if required conditions are met."""
        while True:
            if self.player.score == 21:
                self.view.player_won(self.state)
                break
            elif self.player.score < 21:
                if self.view.ask_next_move(self.state) == "H":
                    self.player.add_card(self.deck.draw())
                    continue
                else:
                    self.dealer_loop()
                    break
            else:
                self.view.player_lost(self.state)
                break

    def dealer_loop(self):
        """Dealer loop."""
        while True:
            if self.dealer.score > self.player.score:
                if self.dealer.score > 21:
                    self.view.player_won(self.state)
                else:
                    self.view.player_lost(self.state)
                break
            else:
                self.dealer.add_card(self.deck.draw())


class BlackjackView:
    """Minimalistic UI/view for the blackjack game."""

    def ask_next_move(self, state: dict) -> str:
        """
        Get next move from the player.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :return: parsed command that user has choses. String "H" for hit and "S" for stand
        """
        self.display_state(state)
        while True:
            action = input("Choose your next move hit(H) or stand(S) > ")
            if action.upper() in ["H", "S"]:
                return action.upper()
            print("Invalid command!")

    def player_lost(self, state):
        """
        Display player lost dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You lost")

    def player_won(self, state):
        """
        Display player won dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You won")

    def display_state(self, state, final=False):
        """
        Display state of the game for the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :param final: boolean if the given state is final state. True if game has been lost or won.
        """
        dealer_score = state["dealer"].score if final else "??"
        dealer_cards = state["dealer"].cards
        if not final:
            dealer_cards_hidden_last = [c.__repr__() for c in dealer_cards[:-1]] + ["??"]
            dealer_cards = f"[{','.join(dealer_cards_hidden_last)}]"

        player_score = state["player"].score
        player_cards = state["player"].cards
        print(dedent(
            f"""
            {"Dealer score":<15}: {dealer_score}
            {"Dealer hand":<15}: {dealer_cards}

            {"Your score":<15}: {player_score}
            {"Your hand":<15}: {player_cards}
            """
        ))


if __name__ == '__main__':
    BlackjackController(Deck(), BlackjackView())  # start the game.
