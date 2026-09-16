# KUŞ

Flappy, on a neon-night cabinet: a violet city skyline with lit windows, mint
pipes, a moon, and a bird that only ever falls.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

One button, which is the whole point.

| Action | Desktop | Phone |
| --- | --- | --- |
| Flap | Space / Up / W / Enter | Tap the screen, or the FLAP button |
| Pause | P | PAUSE button |
| Restart | R | RESTART button, or tap after a crash |

## Rules

- Each pipe you pass is a point. Touch a pipe or the ground and the run is over
  — there is no second life.
- **The gap tightens as you go.** It starts at 78 pixels and loses 2 every five
  points, down to a floor of 58. The HUD's GAP readout shows the current
  width, so you can see the squeeze coming.
- The city scrolls faster on the same schedule, from 64 up to 96 px/s.
- The hitbox is two pixels smaller than the bird on every side — near misses
  are misses.
- Best score is kept in `localStorage` on the device that set it.

## Notes on the drawing

Everything is drawn at 180 internal pixels wide with `image-rendering: pixelated`
over the top, so the whole scene is chunky by construction rather than by
filter. The bird is an 11×9 character map (`BIRD_ROWS`) with the wing drawn
separately on top so it can beat without needing three copies of the sprite,
and its tilt snaps to 15° steps so it stays blocky as it rotates.
