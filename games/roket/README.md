# ROKET

A single-file lander with an ice-blue vector-monitor look. It borrows the flight
model of the 1979 cabinets — gravity, rotation, a thirsty main engine — but the
game around it is a supply run rather than a single descent.

## Play

Open `index.html` in any browser. No build step and no dependencies: the two
fonts are served from this repository, so the page makes no third-party requests
at all (and falls back to system fonts if the files are missing).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Main engine | Up / W / Space | Hold BURN |
| Rotate | Left / Right, A / D | ↺ ↻ buttons |
| Start / resume | Enter | Tap the screen |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## How it differs from the original

- **It does not end when you land.** The surface is five landing shelves spread
  across a map wider than the screen. One is lit: set down there and it counts
  as a delivery, then a different pad lights up and you take off again.
- **Every delivery refuels you.** Touching down on the lit pad fills the tank
  back to 100%, so fuel is the budget for one hop rather than for the whole run.
  The only way to lose is the ground: crash, or put down on an unlit pad with
  nothing left to take off again with.
- **The map scrolls.** The camera tracks the ship, and an arrow at the screen
  edge points to the lit pad with the distance to it.
- **Wind.** A lateral drift, re-rolled after every delivery, that you have to
  trim against on the way down.
- **Wrong pads are safe.** Landing on an unlit shelf costs you nothing but the
  fuel it took to get there.

## Landing limits

| Reading | Must be under |
| --- | --- |
| V-SPD | 42 |
| H-SPD | 25 |
| Tilt | 14° |

The V-SPD and H-SPD readouts turn green when you are inside the limits, so the
HUD tells you whether the landing will take before you touch down.
