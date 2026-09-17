# GÖKTAŞI

A salvage tug in a drifting rock field. Asteroids with the guns taken out.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Turn | Left / Right | ◀ and ▶, press and hold |
| Thrust | Up or Space | THRUST, press and hold |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## You cannot destroy anything

There is no fire button. A rock is never removed from the field — it is only
**moved**. Everything follows from that:

- **The collector ring** drifts across the field. Push a rock through it to bank
  it. Each wave asks for more than the last.
- **Gentle wins.** Hit a rock above a speed threshold and it **shatters** into
  smaller pieces, each worth less than the whole and much harder to herd. A slow,
  planned push banks a rock intact for far more than its fragments will ever pay.
  This is the exact inverse of the game it comes from: patience outscores
  aggression.
- **Nothing stops.** There is no friction on you or on the rocks, and every edge
  wraps. A rock you shoved badly does not go away — it comes back around later in
  the wave, still carrying the speed you gave it.
- **Your hull takes three hard hits.** Gentle contact is free. Ram something and
  you pay for it twice: the rock shatters and your hull cracks.

## Scoring

A rock is worth its size. Bank a large one whole and it pays several times what
the same rock pays after you have broken it into three. The wave counter in the
HUD is a quota, not a timer — the pressure comes from the field getting more
crowded, not from a clock.

## Notes on the code

The collision is an impulse along the contact normal, with the closing speed
deciding both the transfer and whether the rock survives it, so the shatter
threshold is a real physical quantity rather than a special case. Rock outlines
are generated once per rock as a set of per-vertex radius multipliers, then drawn
at whole pixels so they stay crisp at the low internal resolution.
