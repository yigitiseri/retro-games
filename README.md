# Retro Games

Three arcade cabinets, each a single self-contained HTML file. No build step, no
dependencies, no framework — open any `index.html` in a browser and it runs.
All three are built for a phone first: touch controls, a screen that fills the
space it is given, and a keyboard fallback on desktop.

| Game | | Play |
| --- | --- | --- |
| [**YILAN**](games/yilan/) | Snake, on a green-phosphor CRT. Swipe or use the D-pad; the board grows rows to fit your screen. | [`games/yilan/index.html`](games/yilan/index.html) |
| [**YARIŞ**](games/yaris/) | An *Enduro*-style road racer. Pass your quota of cars before nightfall, then keep driving in the dark. | [`games/yaris/index.html`](games/yaris/index.html) |
| [**ROKET**](games/roket/) | A lander, but a supply run: hop pad to pad on fuel you only earn by delivering. | [`games/roket/index.html`](games/roket/index.html) |

Each game has its own README covering controls, rules, and how it is drawn.

## Running them

Open the file directly, or serve the folder:

```sh
python3 -m http.server 8000
# then visit http://localhost:8000/games/yilan/
```

## Repository layout

```
games/
  yilan/   index.html  README.md
  yaris/   index.html  README.md
  roket/   index.html  README.md
```
