# KUŞ

One button, a Famicom afternoon, and a line of birds behind you that is getting
longer and harder to fly.

## Play

Open `index.html` in any browser. No build step and no dependencies: the two
fonts are served from this repository, so the page makes no third-party requests
at all (and falls back to system fonts if the files are missing).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Flap | Space / Up / W / Enter | Tap the screen, or the FLAP button |
| Pause | P | PAUSE button |
| Restart | R | RESTART button, or tap after a crash |

## The flock

You start alone. **Every tree you clear, another bird falls in behind you**, up
to fifteen.

The flock is not a recording of your path. It is a chain: each bird chases the
one in front of it, so the lag compounds down the line. Fly a smooth, centred
line and the whole skein follows you through. Take a gap steeply, late, or off
centre and the tail cuts the corner you turned — and the corner is where the
crown is.

- **Tail clips a tree: you lose that bird.** Feathers, a jolt, and the line
  closes up. The rest get a moment's grace so one branch cannot shred the whole
  flock.
- **Your head clips a tree, or the ground: that is the run.**
- The gap is a constant 78 pixels. Nothing narrows on a timer — the difficulty
  is the flock you built.
- The wood does come at you a little faster as you clear trees, from 64 to
  96 px/s.
- The HUD reads **FLOCK** (birds including you), **BEST** (the biggest flock you
  have ever held) and **GAPS** (trees cleared this run).

Played well, the run settles into a push and pull: you gather birds until the
tail starts costing you them, and you hold at whatever length your flying is
good enough for.

## Notes on the drawing

Everything is drawn at 180 internal pixels wide with `image-rendering: pixelated`
over the top, so the scene is chunky by construction rather than by filter.

Each obstacle is a whole tree — a trunk running off the frame, side limbs with
clumps of leaves, and a lumpy crown ending exactly at the gap edge with a bright
rim along that edge. Crown shapes come from a per-tree seed through a fixed
wobble function, so every tree differs but none flicker. Backdrop pines are a
deliberately darker green so they can never be mistaken for an obstacle.

The bird is an 11×9 character map (`BIRD_ROWS`) with the wing drawn separately
on top so it can beat without three copies of the sprite; its tilt snaps to 15°
steps to stay blocky while rotating. Followers use the same sprite one shade
back, each beating slightly behind the bird in front, which is what makes the
line ripple rather than move as a block.
