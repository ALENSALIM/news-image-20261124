# The World in One Picture — Tuesday 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/ALENSALIM/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/ALENSALIM/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A newspaper front page summing up the world news of Tuesday 24 November
2026 in a single 1024×1024 image (under 1 MiB), drawn entirely with
Python and Pillow from simple flat-colour shapes. No photos, no
downloaded images.

## Stories covered

- **Lead — NATO sends AWACS to Poland:** after three Russian cruise
  missiles came down in Poland on Friday, NATO agreed on Monday to send an
  AWACS early-warning aircraft to Poland.
- **Korea scrambles jets as Russian planes near island:** South Korea
  scrambled fighter jets on Tuesday after several Russian military planes
  entered its air defence zone near Ulleung Island.
- **Three killed in Gaza strike:** an Israeli airstrike killed at least
  three Palestinians on Tuesday near a police outpost in Khan Younis.
- **India and Nepal open new rail link:** the prime ministers flagged off
  the Saryu-Kamala Express on Tuesday, linking Ayodhya with Janakpur Dham.
- **Chess crown on the line in Geneva:** the youngest World Chess
  Championship match in history begins today; D Gukesh defends his title
  against Javokhir Sindarov over 14 games.
- **UN agrees talks on killer robots:** two years of negotiations on rules
  for lethal autonomous weapons, but no binding pact.
- **US sanctions Iran shadow banking:** new sanctions on Monday on dozens
  of people and entities linked to Iran's shadow banking networks.
- **In brief:** ESA's BepiColombo probe safe around Mercury; India and New
  Zealand drew the first Test in Wellington; Oxfam on lasting contamination
  in Gaza; Germany and Ukraine sign a deal on Kyiv's Delta battlefield
  system; Thailand protesters march on a Bangkok oil refinery.

## How to run

```sh
python3 main.py
```

This writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`),
creating the directory if needed, and prints the byte count and SHA-256
hash of the copy. It also checks the copy against the bundled image by
size and hash. Python 3, standard library only; no network access.

To regenerate the image from scratch, run `python3 ../draw.py` from this
directory (Pillow required; the script lives one level up, in the
workspace root, and writes `entry.png` here). Running it twice produces
a byte-identical file.

## Files

- `main.py` — copies the bundled image to the output directory.
- `entry.png` — the front page (1024×1024 PNG).
- `README.md` — this file.
- `LICENSE` — MIT licence.
- `.makefun/owner.json` — bounty owner wallet.

## Licence

MIT — see `LICENSE`.
