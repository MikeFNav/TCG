# TCG

This Pygame game is built for browsers with Pygbag and deployed to GitHub Pages.

## Run locally

Install Pygame and run the game:

```powershell
python -m pip install pygame
python main.py
```

## Deploy

The GitHub Actions workflow builds the browser version and deploys it to GitHub
Pages whenever changes are pushed to `main` or `master`. It can also be started
manually from the repository's Actions tab.

In the repository settings, set **Pages** → **Build and deployment** → **Source**
to **GitHub Actions**. The first successful workflow run publishes the game.
