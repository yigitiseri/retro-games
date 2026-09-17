# OKÇU

A sunset range: an archer on the left in Lincoln green, balloons rising on the
right, and a crosswind between the two.

## Play

Open `index.html` in any browser. No build step and no dependencies: the two
fonts are served from this repository, so the page makes no third-party requests
at all (and falls back to system fonts if the files are missing).

## Controls

| Action | Desktop | Phone |
| --- | --- | --- |
| Aim and draw | Up / Down for angle, Left / Right for power | **Drag anywhere and pull back** — direction sets the angle, distance sets the power |
| Loose | Space | Release the drag, or the LOOSE button |
| Pause | P | PAUSE button |
| Restart | R | RESTART button |

Dragging works anywhere on the glass, so your thumb never covers the archer or
the shot.

## Arrows are the whole game

You start with **six**. Every shot spends one.

- **Pop a balloon and you get that arrow back**, up to a quiver of twelve.
  You see it happen: a small gold arrow lifts off the burst and drifts home to
  the bow, so a three-balloon line sends three of them back at once.
- **An arrow does not stop at the first balloon.** It runs on through everything
  in its line, losing a little speed with each one it punches through, until it
  reaches the grass or leaves the screen.
- **Miss and the arrow sticks in the grass.** It is gone.
- **Run dry — with nothing still in the air — and the day is over.**

So accuracy is not a score multiplier here, it is your ammunition. A cold streak
ends the run on its own, without anything ever hitting you.

## Scoring

- A balloon is worth **10 points plus 5 for every 12 pixels of height** it had
  when you hit it. Letting one climb is worth more than popping it off the grass.
- **Each balloon further down the same arrow's path is worth more**: the first
  scores face value, the second double, the third triple. Lining a row up is the
  big play — and it hands back an arrow for every one of them.
- Some balloons rise in **pairs on one string**. Hit either balloon and you get
  just that one. Hit the **knot** below them and both burst at **double** value
  — the greedy shot, and a much smaller target.
  A knot only exists to hold two balloons together, so the moment the pair is
  down to one the string is cut: the knot flutters away and the survivor
  carries on as an ordinary single balloon. Nothing is ever left hanging in
  the sky with nothing on it.
- Balloons that escape off the top cost you nothing but the arrow you did not
  get back.

## Wind

A crosswind pushes every arrow in flight, changes slowly, and is shown twice:
the **pennant** on the pole leans and streams with it, and the HUD gives you the
number. The grass leans too. Read the pennant before a long shot.

## Notes on the code

The aim preview is a short arc of dots that fades out rather than a full
trajectory line — it shows the shape of the shot without solving it for you, and
it is integrated with the same gravity and wind the arrow will actually use.

The bow rotates around its grip to the aim angle and the string draws back in
proportion to power, so the archer's pose is the read-out. The archer himself is
a 12×21 character map with a warm rim light applied to the last lit pixel of each
row — the sun is off to his right, and that edge is what separates him from the
dark hills behind.
