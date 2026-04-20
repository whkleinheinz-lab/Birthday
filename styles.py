CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

/* Force light color scheme regardless of user's system preference */
:root { color-scheme: light only; }
html, body { color-scheme: light only; background-color: #fdfcf8 !important; }
html, body, [class*="css"] { font-family: 'Cormorant Garamond', Georgia, serif; }
.main .block-container { padding: 0 !important; max-width: 820px !important; }

/* --- Hide Streamlit chrome so the invitation looks standalone --- */
#MainMenu, #MainMenu * { visibility: hidden !important; display: none !important; }
header, header * { visibility: hidden !important; display: none !important; height: 0 !important; }
footer, footer * { visibility: hidden !important; display: none !important; height: 0 !important; }
[data-testid="stHeader"],
[data-testid="stHeader"] * { display: none !important; visibility: hidden !important; height: 0 !important; }
[data-testid="stToolbar"],
[data-testid="stToolbar"] * { display: none !important; visibility: hidden !important; }
[data-testid="stToolbarActions"] { display: none !important; visibility: hidden !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }
[data-testid="stAppDeployButton"],
[data-testid="stAppDeployButton"] * { display: none !important; visibility: hidden !important; }
[data-testid="stActionButton"] { display: none !important; }
[data-testid="manage-app-button"] { display: none !important; }
[data-testid="stBaseButton-headerNoPadding"] { display: none !important; }
[data-testid="stBaseButton-header"] { display: none !important; }
[data-testid="stMainMenu"] { display: none !important; }
.stDeployButton,
.stDeployButton * { display: none !important; visibility: hidden !important; }
.stActionButton { display: none !important; }
.viewerBadge_container__r5tak,
.viewerBadge_link__qRIco,
.viewerBadge_text__1JaDK,
[class*="viewerBadge"] { display: none !important; visibility: hidden !important; }
a[href*="streamlit.io"] { display: none !important; }
a[href*="github.com/streamlit"] { display: none !important; }
a[href*="share.streamlit.io"] { display: none !important; }
button[kind="header"] { display: none !important; }
button[kind="headerNoPadding"] { display: none !important; }
[data-testid="stAppViewContainer"] > .main { padding-top: 0 !important; }
[data-testid="stAppViewBlockContainer"] { padding-top: 0 !important; }
.stAppViewContainer .main .block-container { padding-top: 0 !important; }
div[data-testid="stAppViewContainer"] > section > div:first-child { padding-top: 0 !important; }

.hero-block {
    background: #1a2e1a; padding: 3.5rem 2rem 2.5rem;
    text-align: center; border-bottom: 3px solid #b8a97a;
    position: relative; overflow: hidden;
}
.hero-mountains { position: absolute; bottom: 0; left: 0; width: 100%; z-index: 1; }
.hero-content { position: relative; z-index: 2; }
.eyebrow {
    font-family: 'Cormorant Garamond', serif; font-size: 0.72rem;
    letter-spacing: 5px; text-transform: uppercase; color: #b8a97a; margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Playfair Display', 'Cormorant Garamond', serif; font-size: 3.4rem;
    font-weight: 500; color: #fdfcf8; line-height: 1.15; margin-bottom: 0.5rem;
    letter-spacing: 0.5px;
}
.hero-title em { font-style: italic; font-weight: 400; color: #b8a97a; }
.gold-line { width: 80px; height: 1px; background: #b8a97a; margin: 1rem auto; }
.hero-sub {
    font-family: 'Cormorant Garamond', serif; font-size: 1.1rem;
    font-weight: 300; color: #c8c0a8; letter-spacing: 2px;
}
.pill-row { display: flex; justify-content: center; flex-wrap: wrap; gap: 1.2rem; margin-top: 1.2rem; }
.pill {
    font-family: 'Cormorant Garamond', serif; font-size: 0.68rem;
    letter-spacing: 3px; text-transform: uppercase; color: #b8a97a;
}

.illus-band { background: #f0ebe0; }
.illus-band-inner { display: flex; align-items: stretch; }
.illus-band-copy { width: 38%; padding: 1.5rem 1.5rem 1rem; }
.illus-band-copy.right { text-align: right; }
.illus-band-art { width: 62%; }
.illus-eyebrow { font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase; color: #8b7a5a; margin-bottom: .4rem; }
.illus-title { font-size: 1.45rem; font-weight: 300; color: #1a2e1a; line-height: 1.2; margin-bottom: .4rem; }
.illus-title em { font-style: italic; color: #5a7a3a; }
.illus-desc { font-size: 0.85rem; color: #4a3a2a; line-height: 1.65; }
.illus-link {
    font-size: 0.78rem; color: #5a7a3a; border-bottom: 0.5px solid #5a7a3a;
    text-decoration: none; display: inline-block; margin-top: .4rem;
}

.adventure-band { background: #f0ebe0; border-top: 0.5px solid #e0d8c8; }
.adventure-header { text-align: center; padding: 1.5rem 2rem .75rem; }
.adventure-eyebrow { font-size: 0.65rem; letter-spacing: 4px; text-transform: uppercase; color: #8b7a5a; margin-bottom: .35rem; }
.adventure-title { font-size: 1.75rem; font-weight: 300; font-style: italic; color: #1a2e1a; }

.body-wrap { background: #fdfcf8; padding: 2rem 2.5rem; }
.day-row { display: flex; gap: 0; margin-bottom: 2.5rem; align-items: flex-start; }
.content-left { flex: 1; border-right: 1px solid #c8b882; padding-right: 1.5rem; }
.content-right { flex: 1; border-left: 1px solid #c8b882; padding-left: 1.5rem; }
.icon-col { width: 90px; flex-shrink: 0; display: flex; flex-direction: column; align-items: center; padding-top: .25rem; }
.day-name { font-family: 'Playfair Display', 'Cormorant Garamond', serif; font-size: 1.45rem; font-weight: 500; color: #1a2e1a; margin-bottom: .8rem; letter-spacing: 0.3px; }
.event-row { display: flex; gap: 1rem; margin-bottom: .55rem; align-items: baseline; }
.event-time { font-size: 0.72rem; letter-spacing: 1px; color: #8b7a5a; min-width: 68px; flex-shrink: 0; }
.event-desc { font-size: 0.92rem; color: #2c2c2a; line-height: 1.7; }
.event-desc strong { font-weight: 500; color: #1a2e1a; }
.event-desc a { color: #5a7a3a; text-decoration: none; border-bottom: 0.5px solid #5a7a3a; }
.icon-label { font-size: 0.58rem; letter-spacing: 2px; text-transform: uppercase; color: #b8a97a; margin-top: .5rem; text-align: center; }

.childcare-note { background: #f8f2e4; border-top: 1px solid #e0d8c8; padding: 1.25rem 2.5rem; text-align: center; }
.childcare-note p { font-size: 0.88rem; font-style: italic; color: #6a5a3a; letter-spacing: .5px; line-height: 1.7; }

.rsvp-eyebrow { font-size: 0.65rem; letter-spacing: 4px; text-transform: uppercase; color: #8b7a5a; margin-bottom: .3rem; }
.rsvp-title { font-size: 1.4rem; font-weight: 300; font-style: italic; color: #1a2e1a; margin-bottom: .5rem; }

.footer-block { background: #fdfcf8; text-align: center; padding: 2rem; border-top: 1px solid #e8e0cc; }
.footer-block p { font-size: 0.88rem; color: #8b7a5a; letter-spacing: 1px; margin-bottom: .4rem; }
.footer-sig { font-style: italic; color: #b8a97a !important; font-size: 1rem !important; }

/* ---------- Mobile (<= 640px) ---------- */
@media (max-width: 640px) {
    /* Hero: smaller title, tighter padding, pills stay centered */
    .hero-block { padding: 2.4rem 1rem 1.75rem; }
    .hero-title { font-size: 2.1rem; line-height: 1.2; }
    .hero-sub { font-size: 0.9rem; letter-spacing: 1.5px; }
    .eyebrow { font-size: 0.6rem; letter-spacing: 3px; margin-bottom: 0.7rem; }
    .pill-row { gap: 0.5rem 0.9rem; margin-top: 0.9rem; }
    .pill { font-size: 0.55rem; letter-spacing: 2px; }

    /* Illustration bands stack vertically: art on top, copy below, full-width, centered */
    .illus-band-inner { flex-direction: column !important; }
    .illus-band-art { width: 100%; order: -1; }
    .illus-band-copy,
    .illus-band-copy.right { width: 100%; padding: 1.25rem 1.25rem 1.5rem; text-align: center !important; }
    .illus-eyebrow { text-align: center; }
    .illus-title { font-size: 1.4rem; text-align: center; }
    .illus-desc { font-size: 0.92rem; text-align: center; }
    .illus-link { display: inline-block; margin-top: .6rem; }

    /* Adventure band header */
    .adventure-header { padding: 1.2rem 1.25rem 0.6rem; }
    .adventure-title { font-size: 1.4rem; }
    .adventure-eyebrow { font-size: 0.6rem; letter-spacing: 3px; }

    /* Day-by-day: stack icon above content; drop center divider; center day name */
    .body-wrap { padding: 1.5rem 1.15rem; }
    .day-row { flex-direction: column !important; gap: 0.4rem; margin-bottom: 2rem; }
    .content-left, .content-right { border: none !important; padding: 0 !important; width: 100%; }
    .icon-col { width: 100%; flex-direction: row; justify-content: center; gap: 0.6rem; padding-top: 0; margin-bottom: 0.5rem; order: -1; align-items: center; }
    .icon-col svg { width: 40px !important; height: 40px !important; }
    .icon-label { margin-top: 0; font-size: 0.55rem; }
    .day-name { font-size: 1.35rem; margin-bottom: 0.6rem; text-align: center; }
    .event-row { gap: 0.6rem; margin-bottom: 0.7rem; }
    .event-time { min-width: 54px; font-size: 0.66rem; }
    .event-desc { font-size: 0.88rem; line-height: 1.6; }

    /* Childcare + RSVP + footer */
    .childcare-note { padding: 1rem 1.15rem; }
    .childcare-note p { font-size: 0.85rem; }
    .rsvp-title { font-size: 1.25rem; }
    .footer-block { padding: 1.5rem 1.15rem; }
}
</style>
"""
