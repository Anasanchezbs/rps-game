"""RPS-001: the rules for one round of Rock, Paper, Scissors. See SPEC.md."""

# Each move maps to the move it beats.
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective.

    The supplied web page accepts only 'rock', 'paper', and 'scissors'.
    """
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "win"
    return "lose"
