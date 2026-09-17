# BLOK

Falling wool on a loom. Complete a row and it is woven into the carpet beside
you — and the carpet is what you are actually playing for.

## Play

Open `index.html` in any browser. No build step, no dependencies (the two fonts
load from Google Fonts; the game works with system fallbacks offline).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Move | Left / Right (hold to repeat) | ◀ and ▶, press and hold |
| Rotate | Up or X | ↻ button |
| Hard drop | Space | DROP button |
| Soft drop | Down | — |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

## The carpet is the point

Clearing rows quickly is not the skill here. **Clearing rows that are patterned
is.**

- Every cleared row is **woven onto the kilim**, the strip beside the loom, in
  the exact colours you gave it. The carpet is a record of the run.
- A row that **mirrors around its centre** is a motif, and pays many times what a
  mixed row pays. In testing, a symmetric row scored **1485 against a mixed row's
  50** — nearly thirty times as much.
- A row in a single dye is a **solid band**, worth more still.
- So every piece is two decisions at once: where it fits, and what colour it puts
  there. Dropping now is safe; holding out for the pattern is worth far more.

Five dyes, all from real kilim work: madder red, indigo, saffron, walnut and
undyed cream.

## Scoring

Row value is multiplied by how well the row mirrors itself, counted as matched
pairs either side of the centre. The MOTIFS counter in the HUD tracks how many
patterned rows you have woven, which is the number worth comparing between runs —
ROWS alone only says how long you survived.

## Notes on the code

The playfield is deliberately shorter than the traditional twenty rows so that
the loom, the carpet and the controls all fit one phone screen without scrolling.
The internal canvas height is decided first and the displayed box is derived from
it, so the buffer and the CSS box can never disagree and stretch the picture.
