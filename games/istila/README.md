# İSTİLA

A city at dusk, and a swarm coming down on it. The invaders stand on one
another, so the shape of the formation is the puzzle.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Move | Left / Right | ◀ and ▶, press and hold |
| Fire | Space or Up (hold to keep firing) | FIRE, press and hold |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## The swarm is a structure

This is the whole game, and it is the one thing the original never did.

- **Shoot the bottom of a stack and everything above it drops a row.** Fast
  progress: one shot clears a space and shuffles the whole column down.
- **But the one that lands is now the lowest — and only the lowest invader in a
  column can shoot at you.** Collapsing a stack does not just bring them closer,
  it hands them a gun. The greedy shot arms the enemy.
- **Thread a shot up through a gap and you take one off the top.** Nothing moves,
  nothing gets armed, and the top tiers are worth the most. Slower, safer, richer.
- **The swarm slides left and right**, so the gaps you can shoot through open and
  close. Aiming is not enough; you have to wait for the lane.

So every trigger pull is the same question: do I want this cleared, or do I want
it *safe*?

## Scoring

Value rises with height — the top tier is worth 35, the middle 20, the bottom 10,
multiplied up as the waves go on. That is deliberate: the invader that is hardest
to reach, and safest to remove, is the one that pays. Clearing a wave brings a
denser lattice with fewer gaps to thread.

## The rooftops

There is no winning, only holding. Let any column reach the skyline and the run
ends. Three ships, and a hit costs you one.

## Notes on the code

Bombs are spawned only from the lowest live invader in each column, recomputed
every frame, which is what makes the collapse mechanic bite. Player shots travel
upward and are tested against the lowest rows first, so a shot naturally meets
the bottom of a stack unless you have found a genuine gap — the mechanic falls
out of the collision order rather than being special-cased.

The invaders are drawn twice, once in near-black offset by a pixel and once in
their tier colour, because this palette puts orange sprites over a bright orange
horizon as they descend. The hitbox on your ship is deliberately smaller than the
sprite, so a shave past the wing is a near miss rather than a death.
