# Retro Games

Five arcade cabinets, each a single self-contained HTML file. No build step, no
dependencies, no framework — open any `index.html` in a browser and it runs.
All three are built for a phone first: touch controls, a screen that fills the
space it is given, and a keyboard fallback on desktop.

| Game | | Play |
| --- | --- | --- |
| [**YILAN**](games/yilan/) | Snake, on a green-phosphor CRT. Swipe or use the D-pad; the board grows rows to fit your screen. | [`games/yilan/index.html`](games/yilan/index.html) |
| [**YARIŞ**](games/yaris/) | An *Enduro*-style road racer. Pass your quota of cars before nightfall, then keep driving in the dark. | [`games/yaris/index.html`](games/yaris/index.html) |
| [**ROKET**](games/roket/) | A lander, but a supply run: hop pad to pad on fuel you only earn by delivering. | [`games/roket/index.html`](games/roket/index.html) |
| [**KUŞ**](games/kus/) | Flappy in a Famicom wood. One button, and a gap between two tree crowns. | [`games/kus/index.html`](games/kus/index.html) |
| [**TUĞLA**](games/tugla/) | Breakout, with a ball that heats up away from your bat and burns two bricks deep. | [`games/tugla/index.html`](games/tugla/index.html) |

`index.html` at the root is the arcade menu: the three cabinets side by side,
each with a live attract-mode preview of the game running in miniature. It is
what GitHub Pages serves, so the Pages URL opens straight into the arcade.

Each game has its own README covering controls, rules, and how it is drawn.

## Running them

Open `index.html` directly, or serve the folder:

```sh
python3 -m http.server 8000
# then visit http://localhost:8000/
```

## Publishing

Settings → Pages → Deploy from a branch → `main` / root. The menu is then at
`https://<user>.github.io/retro-games/` and each cabinet a link away, with no
sign-in and nothing to install.

## Repository layout

```
index.html       the arcade menu
games/
  yilan/   index.html  README.md
  yaris/   index.html  README.md
  roket/   index.html  README.md
  kus/     index.html  README.md
  tugla/   index.html  README.md
```
