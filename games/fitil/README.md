# FİTİL

A blueprint of a room, and three charges. Bomberman where a single bomb is worth
almost nothing.

## Play

Open `index.html` in any browser. No build step and no dependencies: the two
fonts are served from this repository, so the page makes no third-party requests
at all (and falls back to system fonts if the files are missing).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Move | Arrows or WASD | The direction pad |
| Drop a bomb | Space | DROP BOMB |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## The chain is the game

You carry **three bombs from the very start**, because chaining is not a reward
you unlock — it is the whole point.

- A bomb that goes off alone pays its base value.
- **A bomb caught in another bomb's fire detonates instantly**, and the payout is
  multiplied by the **square** of how many went at once. Two bombs pay four times.
  Three pay nine.
- So you stop clearing the room and start **arming** it: laying charges you have
  no intention of setting off yet, and racing your own first fuse.
- **Every bomb burns for the same time from the moment it is dropped**, which
  makes a chain a schedule rather than a trick. The first one you place is the
  one that decides when everything happens.

## What else is in the room

- **Soft brick** breaks and stops the fire at the first one it meets; **hard
  block** does neither. So every blast reshapes where the next one can reach.
- **Fire does not care whose bomb it was.** The bigger the chain you build, the
  less floor you have left to stand on.
- Two kinds of company: one wanders, one comes for you when you get within about
  seven cells. Both are slower than you are — measured, not assumed — so being
  caught is a mistake rather than bad luck.
- Clear the floor of them and the next one is denser.

## Fairness

Some invariants are covered by tests rather than by hope:

- Dropping a bomb and simply walking away in a straight line **always** clears the
  blast, with about four cells to spare.
- Every chaser is slower than the runner, on every floor.
- Coming back after a death gives you a real moment of grace, so you cannot be
  killed the instant you reappear in a room that is still burning.
- Lives cannot go below zero, and the third death ends the run then and there.

## Notes on the code

The chain is a breadth-first cascade: a detonating bomb collects its blast cells,
anything standing in them dies, and any bomb found there is pulled into the same
queue. The multiplier falls out of the queue length, so the mechanic is the data
structure rather than a special case bolted on.

The room is drawn as a plan rather than a picture — cyan grid, outlined blocks,
white fire. Soft brick gets a filled body so it can never be mistaken for a hard
block at a glance, which is the one real risk of drawing everything in outline.
