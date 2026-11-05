"""RPS-001 real-browser round and replay using the real determine_winner."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_round_and_replay_in_real_browser(page: Page, live_server, monkeypatch):
    """A real click plays a round with real rules; choosing again starts anew."""
    # Fix only the computer's random move; real rules and real HTTP are used.
    monkeypatch.setattr(web.random, "choice", lambda _moves: "rock")
    page.goto(live_server)

    page.get_by_role("button", name="Paper", exact=True).click()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "win")
    expect(page.locator("body")).to_contain_text("You win!")
    expect(page.get_by_text("You chose", exact=True)).to_be_visible()
    expect(page.get_by_text("Computer chose", exact=True)).to_be_visible()

    # Replay: a second choice starts a new, independent round.
    page.get_by_role("button", name="Scissors", exact=True).click()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "lose")
    expect(page.locator("body")).to_contain_text("Computer wins")
