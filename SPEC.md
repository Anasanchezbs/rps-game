# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- **Prediction:** Player paper vs. computer rock → `win`, because paper covers rock. This matches the expected results table.
- **Scope:** Implement `determine_winner(player, computer)` in `game.py`. It returns `win`, `lose`, or `tie` from the player's perspective, matching the nine expected results above. Keep the supplied interface and server. No scoring, storage, accounts, new framework, or AI API.
- **Valid losing round (positive case):** Player scissors vs. computer rock → `lose`, because rock crushes scissors. This is a normal, correct result, not an error.
- **Rejected input (negative case):** A missing move or an unsupported move such as `lizard` → HTTP 400 with a helpful message, without calling the rules.
- **Tests:**
  - Unit (`unit` marker): all nine results written out literally in `tests/test_game.py`.
  - Integration (`integration` marker): submit a real round with the computer's move fixed, then check that both choices and the correct result appear. Reuse the supplied 400 tests for bad input.
  - E2E (`e2e` marker): in `tests/e2e/test_round.py`, a real browser plays a round, checks the result, then plays again. Only the computer's move is fixed; the real rules are used.
- **Done when:** the full `.venv/bin/python check.py` passes (not `--fast`), the diff has been reviewed, and no checks were weakened.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: https://github.com/Anasanchezbs/rps-game/issues/1
- Pull request / CI: add actual URLs when they exist.
- Implementation: `game.py` implements `determine_winner(player, computer)` using a table of which move beats which. The supplied interface and server are unchanged.
- Tests: `tests/test_game.py` (nine literal unit cases plus an integration round that uses the real rules) and `tests/e2e/test_round.py` (real-browser round and replay). The supplied missing/invalid-move tests in `tests/test_shell.py` were kept and still pass (HTTP 400).
- Full local check (`.venv/bin/python check.py`): Black PASS (11 files), Pylint PASS, non-browser pytest 25 passed, Chromium browser 6 passed. Before the final run, Black and Pylint caught a missing final newline and duplicated test lines, which were fixed without weakening any checks.
- One test explained: `("scissors", "rock", "lose")` checks that scissors loses to rock. It would catch rules written backwards, such as comparing the computer's move against the player's.
- Played round: I chose rock, the computer chose paper → "Computer wins." This is correct because paper covers rock. Earlier, scissors vs. scissors → "It's a tie," because the moves matched.
- Keyboard/replay: In Safari, Option + Tab moved between the buttons and Enter played a round (plain Tab only focused the address bar). Choosing again started a new, independent round.
- Help received: Used Claude to understand the workflow and to draft the rule function, tests, and this record. I reviewed them, ran the checks, and played the game myself.