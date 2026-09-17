# LOKMA

A covered market at night: stalls for walls, lanterns over the junctions, a
carpet floor. You are collecting lokma while the market tries to catch you.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Steer | Arrow keys / WASD | Swipe the screen, or the D-pad |
| Start / resume | Space or Enter | Tap |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## The tray

This is the whole game, and it is not the game it looks like.

- Lokma you pick up **ride on a tray. They are not scored yet.**
- **A full tray is slow.** Your speed drops from 50 down to a floor of 26 as it
  fills — the gauge under the maze is your weight.
- You bank a tray by standing on **the counter**, the brass tile in the middle.
- Banking pays more per lokma the more you are carrying: **10** each up to
  three, **15** each from four, **25** each from eight.
- **Getting caught spills the tray.** Everything on it scatters back into the
  market, and you lose a life.

So the question is never "can I reach that one", it is "am I too heavy to still
be out here". A market is only cleared when the floor is empty *and* your tray
is empty, so every level ends with one last walk to the counter.

## The four of them

Each chaser is a different rule for picking its next cell, not one pursuit
algorithm in four colours. They arrive one per market, up to four.

| | | |
| --- | --- | --- |
| **Kedi** | red, ears | Shortest path to you, always. No tricks, no let-up. |
| **Bekçi** | purple | Walks a round of the lanterns, and only breaks off to chase when you come within five cells. |
| **Çırak** | teal | Ignores where you are and paths to the cell **four ahead of the way you are facing** — it is cutting you off, not following you. |
| **Köpek** | brass, ears | Wanders at junctions, then lunges: inside three cells it jumps from 30 to 44 speed. Empty-handed you are quicker than the lunge, so it can be outrun; three lokma on the tray and it cannot. |

Every chaser speeds up by 2.5 each market, but the ramp **stops at 47** —
just under your empty-handed 50. So no matter how deep the run goes, dropping
your tray and running is always an escape. The pressure past that point comes
from there being four of them, not from them simply being faster than you.


None of them may reverse unless it is the only way out, which is what makes
their paths readable enough to plan against.

## Notes on the code

Every chaser decision comes from one breadth-first distance field over the
maze — the same 15×11 flood fill, run from a different target per personality.
That is why Çırak can ambush with the same code that makes Kedi chase: only its
goal cell differs.

Stall fronts are drawn as one long awning per run of stalls facing a lane,
rather than a striped cap on every wall cell, which is what makes the lanes
readable at 12 pixels per cell.
