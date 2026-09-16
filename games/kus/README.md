# KUŞ

One button, a Famicom afternoon, and a bird that only ever falls. You thread the
gap between a tree crown hanging from above and one growing up from the forest
floor.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Flap | Space / Up / W / Enter | Tap the screen, or the FLAP button |
| Pause | P | PAUSE button |
| Restart | R | RESTART button, or tap after a crash |

## Rules

- Each tree you pass is a point. Touch a tree or the ground and the run is over
  — there is no second life.
- **The wood closes in.** The gap starts at 78 pixels and loses 2 every five
  points, down to a floor of 58, while the scroll speed climbs from 64 to
  96 px/s. The HUD's GAP readout shows the current width.
- The hitbox is two pixels smaller than the bird on every side — near misses
  are misses.
- Best score is kept in `localStorage` on the device that set it.

## The look

A Famicom daylight palette: one cyan sky, three greens, one brown, drawn at 180
internal pixels wide with `image-rendering: pixelated` over the top, so the
scene is chunky by construction rather than by filter.

Each obstacle is a whole tree — a trunk running off the frame, side limbs with
clumps of leaves, and a lumpy crown that ends exactly at the edge of the gap,
with a bright rim along that edge so the line you have to miss is the crispest
thing on screen. Backdrop pines are drawn in a deliberately darker green so
they can never be mistaken for something you can hit. Crown edges come from a
per-tree seed through a fixed wobble function, so every tree is a different
shape but none of them flicker.

The bird is an 11×9 character map (`BIRD_ROWS`) with the wing drawn separately
on top so it can beat without needing three copies of the sprite, and its tilt
snaps to 15° steps so it stays blocky as it rotates.
