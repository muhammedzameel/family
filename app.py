# app.py
import random
import streamlit as st

# ---------------- Page setup ---------------- #
st.set_page_config(
    page_title="Chakkalakkal NFamily Trip",
    page_icon="🎒",
    layout="centered",
)

# ---------------- Data ---------------- #
DESTINATIONS = [
    {
        "name": "Wayanad",
        "tagline": "Waterfalls and wildlife",
        "image": "https://source.unsplash.com/featured/?wayanad",
    },
    {
        "name": "Munnar",
        "tagline": "Tea gardens and cool climate",
        "image": "https://source.unsplash.com/featured/?munnar,tea",
    },
    {
        "name": "Alappuzha",
        "tagline": "Houseboat and backwaters",
        "image": "https://source.unsplash.com/featured/?alappuzha,backwater",
    },
    {
        "name": "Coorg",
        "tagline": "Coffee plantations and hills",
        "image": "https://source.unsplash.com/featured/?coorg,coffee",
    },
    {
        "name": "Ooty",
        "tagline": "Lake and botanical gardens",
        "image": "https://source.unsplash.com/featured/?ooty",
    },
    {
        "name": "Mysore",
        "tagline": "Palace and zoo",
        "image": "https://source.unsplash.com/featured/?mysore,palace",
    },
    {
        "name": "Kodaikanal",
        "tagline": "Pine forest and boating",
        "image": "https://source.unsplash.com/featured/?kodaikanal",
    },
    {
        "name": "Thekkady",
        "tagline": "Periyar wildlife and boating",
        "image": "https://source.unsplash.com/featured/?thekkady,wildlife",
    },
    {
        "name": "Goa",
        "tagline": "Clean beaches and forts",
        "image": "https://source.unsplash.com/featured/?goa,beach",
    },
    {
        "name": "Pondicherry",
        "tagline": "French‑style town and peaceful vibes",
        "image": "https://source.unsplash.com/featured/?pondicherry,beach",
    },
]

# ---------------- UI ---------------- #
st.title("Chakkalakkal NFamily Trip")
st.markdown(
    "Plan your next **family getaway**. Click **Suggest a Trip** "
    "and let us pick a destination for you!"
)

if st.button("🎒 Suggest a Trip"):
    dest = random.choice(DESTINATIONS)
    st.success(f"🏖️ **{dest['name']}** – {dest['tagline']}")
    st.image(dest["image"], use_column_width=True)

st.markdown("---")
st.caption("© 2025 Chakkalakkal NFamily Trip")
