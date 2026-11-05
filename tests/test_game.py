"""RPS-001 tests: the nine real rule outcomes and a real request/result round."""

# pytest injects fixtures by their function names; descriptive test names act
# as the test documentation. Keep all other Pylint diagnostics enabled.
# pylint: disable=redefined-outer-name,missing-function-docstring

import pytest

import app as web
from game import determine_winner


@pytest.fixture
def client():
    web.app.config.update(TESTING=True)
    return web.app.test_client()


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner_matches_spec(player, computer, expected):
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
@pytest.mark.parametrize(
    ("player", "outcome", "heading"),
    [
        ("paper", "win", "You win!"),
        ("scissors", "lose", "Computer wins"),
        ("rock", "tie", "It’s a tie"),
    ],
)
def test_submitted_round_uses_real_rules(client, monkeypatch, player, outcome, heading):
    # Fix only the computer's random move; the real determine_winner runs.
    monkeypatch.setattr(web.random, "choice", lambda _moves: "rock")
    response = client.post("/", data={"move": player})
    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert f'data-outcome="{outcome}"' in page
    assert heading in page
    assert "You chose" in page
    assert "Computer chose" in page
