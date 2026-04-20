import streamlit as st
from assets import (
    ICON_FISH, ICON_CARDS, ICON_CHAMPAGNE, ICON_RAFT, ICON_PLANE,
)
from styles import CSS

st.set_page_config(
    page_title="Sarah & Willy's 30th Birthday Bash",
    page_icon="🏔️",
    layout="centered",
)


def render_hero():
    st.markdown("""
    <div class="hero-block">
      <svg class="hero-mountains" viewBox="0 0 820 110" xmlns="http://www.w3.org/2000/svg">
        <polygon points="0,110 0,65 90,22 185,70 285,5 400,58 510,10 620,62 710,26 820,48 820,110" fill="#0f1f0f"/>
        <polygon points="0,110 0,80 70,50 155,84 250,32 365,74 470,28 580,68 670,40 780,62 820,52 820,110" fill="#162a16"/>
        <polygon points="0,110 0,96 50,80 120,98 200,72 305,94 410,68 520,92 620,76 720,94 820,80 820,110" fill="#1a2e1a"/>
        <circle cx="410" cy="28" r="9" fill="#f0e8c8" opacity="0.85"/>
        <circle cx="438" cy="16" r="3" fill="#f0e8c8" opacity="0.45"/>
        <circle cx="384" cy="35" r="2" fill="#f0e8c8" opacity="0.35"/>
      </svg>
      <div class="hero-content">
        <div class="eyebrow">Jackson Hole, Wyoming</div>
        <div class="hero-title">Sarah &amp; Willy's<br><em>30th Birthday Bash</em></div>
        <div class="gold-line"></div>
        <div class="hero-sub">August 5 &#8211; 9, 2026</div>
        <div class="pill-row">
          <span class="pill">Cookout</span>
          <span class="pill">Ski Valley Dinner</span>
          <span class="pill">River Float</span>
          <span class="pill">Fly Fishing</span>
          <span class="pill">Choose Your Own Adventure</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


def render_days():
    st.markdown('<div class="body-wrap">', unsafe_allow_html=True)

    # Wednesday (content left, icon right)
    st.markdown(f"""
    <div class="day-row">
      <div class="content-left">
        <div class="day-name">Wednesday, August 5</div>
        <div class="event-row">
          <span class="event-desc">Texas shuttle departs <strong>Meacham (KFTW)</strong> mid-morning; coastal friends arrive on their own schedule. Casual cookout at the Kleinheinz house &#8212; burgers, hot dogs, s'mores, and a campfire.</span>
        </div>
      </div>
      <div class="icon-col">
        {ICON_CHAMPAGNE}
        <div class="icon-label">House cookout</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Thursday (icon left, content right)
    st.markdown(f"""
    <div class="day-row">
      <div class="icon-col">
        {ICON_CARDS}
        <div class="icon-label">Ski valley dinner</div>
      </div>
      <div class="content-right">
        <div class="day-name">Thursday, August 6</div>
        <div class="event-row">
          <span class="event-desc">A relaxing day &#8212; golf or a casual hike. Dinner in the ski valley, then drinks at the <strong>Mangey Moose</strong>.</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Friday (content left, icon right)
    st.markdown(f"""
    <div class="day-row">
      <div class="content-left">
        <div class="day-name">Friday, August 7</div>
        <div class="event-row">
          <span class="event-desc"><strong>River float</strong> with drinks and snacks; off the water by mid-afternoon. Outdoor seated dinner at the Kleinheinz house &#8212; festive and boozy.</span>
        </div>
      </div>
      <div class="icon-col">
        {ICON_RAFT}
        <div class="icon-label">River float</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Saturday (icon left, content right)
    st.markdown(f"""
    <div class="day-row">
      <div class="icon-col">
        {ICON_FISH}
        <div class="icon-label">Adventure day</div>
      </div>
      <div class="content-right">
        <div class="day-name">Saturday, August 8</div>
        <div class="event-row">
          <span class="event-desc">Pick your pace: a casual hike, fly fishing on the Snake, or a pool day. Dinner in town to celebrate.</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Sunday (content left, icon right)
    st.markdown(f"""
    <div class="day-row">
      <div class="content-left">
        <div class="day-name">Sunday, August 9</div>
        <div class="event-row">
          <span class="event-desc">Texas shuttle departs mid-morning, arriving Fort Worth mid-afternoon. Coastal friends depart on their own schedule.</span>
        </div>
      </div>
      <div class="icon-col">
        {ICON_PLANE}
        <div class="icon-label">Homeward bound</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer-block">
      <div class="gold-line"></div>
      <p style="margin-top:1rem;">Questions? Reach out to Sarah or Willy directly.</p>
      <p class="footer-sig">With love &amp; anticipation &#8212; Sarah &amp; Willy</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    st.markdown(CSS, unsafe_allow_html=True)
    render_hero()
    render_days()
    render_footer()


if __name__ == "__main__":
    main()
