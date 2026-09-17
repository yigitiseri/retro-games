# TUĞLA

The 1976 brick cabinet — black field, four colour bands, a bat and a ball —
with one rule of its own: **the ball heats up**.

## Play

Open `index.html` in any browser. No build step and no dependencies: the two
fonts are served from this repository, so the page makes no third-party requests
at all (and falls back to system fonts if the files are missing).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Move the bat | Arrow keys / A D, or the ◀ ▶ buttons | Drag anywhere on the screen |
| Serve | Space or Enter | Tap |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

Dragging works anywhere on the glass, not just on the bat, so your thumb never
covers the thing you are aiming.

## Heat

The ball warms while it is away from your bat, and hitting it cools it back to
nothing. The gauge along the floor shows how hot it is; the notch on that gauge
is the threshold.

| | Cold ball | Hot ball (past the notch) |
| --- | --- | --- |
| Speed | base | up to 1.65× |
| Bricks per hit | 1 | 2 — it burns through to whatever is behind |
| Score | face value | doubled |

So the tunnel is the point. Dig up one side, let the ball loose in the roof, and
every brick it touches up there is worth double and takes its neighbour with it
— but it comes back down faster than you last saw it.

## Rules

- Three balls. Lose all three and the run ends.
- Bricks are worth 10, 30, 50 and 70 by row, hardest rows highest.
- Clearing a wall is worth 100 × the wall number, then the next wall loads a
  little faster.
- **Break through to the ceiling and your bat is halved** — the 1976 rule, kept.
- Best score is kept in `localStorage` on the device that set it.

## Notes on the code

The ball moves in sub-steps of at most 1.5 pixels per frame rather than one
jump, so a hot ball cannot pass through a brick between frames. Horizontal and
vertical movement are resolved separately, which is what makes the ball bounce
off the side of a brick correctly instead of always reversing vertically.
Bricks are laid out on whole pixels and the wall is centred: at 160 pixels
across, a fractional brick width rounds neighbours together and the mortar line
disappears.
