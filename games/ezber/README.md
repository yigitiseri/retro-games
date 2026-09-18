# EZBER

Four lamps on a dark console. Simon, with the one rule everybody knows taken out.

## Play

Open `index.html` in any browser. No build step and no dependencies: the two
fonts are served from this repository, so the page makes no third-party requests
at all.

## Controls

| Action | Phone | Desktop |
| --- | --- | --- |
| Answer | Tap the quarter of the panel | `1` `2` `3` `4` |
| Hear it again | REPLAY | — |
| Pause | PAUSE | `P` |
| Restart | RESTART | `R` |

## The sequence never grows

In Simon the list gets longer every round, so the game is a test of how much you
can hold. Here it is **always five**, and every round **exactly one step
changes** — to a lamp it was not before, and nothing tells you which.

So you are not memorising a list. You are holding a shape in your head and
watching for the thing that moved. Get it right and the next round moves a
different step. Get it wrong and you have three tries in total.

Everything else follows from that:

- **The length is not the difficulty.** Five is easy. Five that keeps
  rearranging itself is not.
- **You lose by forgetting.** Nothing chases you and nothing shoots. It is the
  only cabinet here that ends that way.
- **Playback tightens every round** — measured, 0.46s a lamp at the start and
  0.32s by round nine — so late on you are catching a change you barely had time
  to hear.
- **REPLAY hands the round back to you once**, and costs you that round's points.
  It is there for the round where you blinked, not as a crutch.

## Scoring

A cleared round pays ten times the round number, so surviving deep is worth far
more than surviving wide. The HUD carries your best run.

## Notes on the code

The mutation picks a position at random and then picks a lamp for it in a loop
until it lands on one that is different from what was there — without that loop,
roughly a quarter of rounds would silently change nothing and the player would be
punished for being right.

The four pads are quadrants of the panel, so the touch target is a quarter of the
screen each. There are no buttons to miss, which is what makes this one playable
one-handed on a train.
