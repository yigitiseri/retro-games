# YILAN

A single-file retro arcade snake game — green-phosphor CRT look, scanlines, amber
pellets, and rising speed as you eat.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Steer | Arrow keys / WASD | Swipe the screen, or the on-screen D-pad |
| Start / resume | Space or Enter | Tap the screen |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## Rules

- Eat the amber pellet to score `10 + current speed level` and grow three cells.
- Walls and your own tail are fatal.
- The board is 21 columns wide; the number of rows is set by your screen, so a
  tall phone gets a taller board.
- Speed steps up every 4 pellets, from 150 ms per move down to 68 ms.
- The high score is kept in `localStorage` on the device that set it.
