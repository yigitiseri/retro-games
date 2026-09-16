# YARIŞ

A single-file pseudo-3D road racer in the Atari *Enduro* tradition — amber-CRT
cabinet, a road that bends toward a moving horizon, and a full day/night cycle
that doubles as your clock.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Accelerate | Up / W | Hold GAS |
| Brake | Down / S | Hold BRAKE |
| Steer | Left / Right, A / D | ◀ ▶ buttons |
| Start / resume | Space or Enter | Tap the screen |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## Rules

- Each day you must pass a quota of cars — `10 + day × 3` — before nightfall.
  The amber strip across the top of the screen is the day running out.
- Miss the quota when the day ends and the run is over. Meet it and the quota
  turns green, the day rolls over, and the next one asks for more.
- Crashing into traffic costs you nearly all your speed, but never the run.
- Two wheels on the grass caps you at roughly 76 mph.
- The sky cycles dawn → day → dusk → night, and visibility closes in with it:
  at night the road fades out a few car lengths ahead.

## How the road is drawn

There is no 3D engine here. Each screen row below the horizon is one `fillRect`,
its depth taken as `z = 1 / s` where `s` is the row's distance down the screen.
Road width scales with `s`, the curve offset scales with `z`, and the stripes
come from `floor((travel + z) / segment) & 1` — the same trick the 1983 cabinets
used, at 320 internal pixels wide with `image-rendering: pixelated` on top.
