# PING PONG

The oldest arcade game, and the only cabinet here you can hand to someone sitting
opposite you.

## Play

Open `index.html` in any browser. No build step and no dependencies: the two
fonts are served from this repository, so the page makes no third-party requests
at all.

## Controls

| Action | Phone | Desktop |
| --- | --- | --- |
| Move your bat | **Drag anywhere in your half of the court** | Cyan: `A` / `D` · Pink: `←` / `→` |
| Start, pause, resume | Tap the court | Space, or `P` to pause |
| One or two players | The 1 PLAYER / 2 PLAYERS button | — |
| Restart | RESTART button | `R` |

Two thumbs work at the same time and independently: a finger in the top half owns
the cyan bat, a finger in the bottom half owns the pink one, and they can cross
past each other. Hold the phone flat between you.

## The pot

This is the one thing that is not Pong.

In the original, a twenty-shot rally is worth exactly what a missed serve is
worth, so there is no reason to want the rally to continue. Here:

- **Every return raises the pot**, and the ball speeds up with it.
- **Whoever wins the point takes the whole pot.**

So both of you want the rally to keep going, and both of you are getting more
frightened as it does. It turns a reflex test into a game of nerve between two
people — the tension is across the phone, not against the machine.

The growth is not linear. Measured from the running game:

```
return   1    2    3    4    5    6    7    8    9   10   11   12
pot     15   20   30   40   50   65   80   95  115  135  155  180
```

A twelve-shot rally is worth eighteen times a point won off the serve.

## The bat

Hitting with the **middle** sends the ball straight back — safe, and it keeps the
rally alive for someone else to inherit. Hitting with the **end** throws it out at
a sharp angle: measured, a flat hit returns with 0 sideways speed and an edge hit
with 76. The dangerous shot is how you end a rally you are frightened of, and it
is also how you miss.

First to 300 takes the match.

## Alone

If nobody else is there, a machine takes the far bat. It tracks the ball well but
not perfectly, and it has a deliberate wobble, so it can be beaten.

## Notes on the code

The court itself is the control surface. Pointer events are tracked per
`pointerId` and assigned to a half on touch-down, which is what lets two thumbs
work at once without either stealing the other's bat — a single-pointer approach
would have made the two-player mode impossible on a phone.

The ball takes the colour of whoever touched it last, so at a glance you can see
whose mistake is on its way.
