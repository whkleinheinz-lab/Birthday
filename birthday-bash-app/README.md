# Sarah & Willy's 30th Birthday Bash — Streamlit Website

A wedding-invitation-styled website for the birthday weekend in Jackson Hole.

## Files

- `birthday_bash_app.py` — the main Streamlit app (run this)
- `assets.py` — all SVG illustrations and icons
- `styles.py` — CSS styling

All three files must sit in the same folder.

## Run locally

```bash
pip install streamlit
streamlit run birthday_bash_app.py
```

Opens at http://localhost:8501

## Deploy to Streamlit Community Cloud (free)

1. Create a new GitHub repository.
2. Upload all three `.py` files to the repo root.
3. Create a `requirements.txt` file in the repo with one line:
   ```
   streamlit
   ```
4. Go to https://share.streamlit.io and sign in with GitHub.
5. Click "New app" → select your repo → set the main file to `birthday_bash_app.py`.
6. Click Deploy. You'll get a shareable public URL.

## Editing content

- Event text and copy → edit the `render_days()` function in `birthday_bash_app.py`
- Illustrations → edit the SVG strings in `assets.py`
- Colors, fonts, spacing → edit `styles.py`
