import streamlit as st
import random

# --- Page Setup ---
st.set_page_config(page_title="Kozhikode Family Trip", page_icon="🧳", layout="centered")

# --- Title ---
st.title("Chakkalakkal Family Trip")
st.markdown("Discover beautiful family destinations around Kozhikode and Chakkalakkal. Click below to get a suggestion!")

# --- Destination List ---
destinations = [
    {
        "name": "Kozhikode Beach",
        "tagline": "Sunset views, street food & kids’ fun zone",
        "image": "https://source.unsplash.com/featured/?kozhikode,beach"
    },
    {
        "name": "Beypore Port & Beach",
        "tagline": "Historic port, boating and beach strolls",
        "image": "https://source.unsplash.com/featured/?beypore,port"
    },
    {
        "name": "Mananchira Square",
        "tagline": "A beautiful urban park near the city center",
        "image": "https://source.unsplash.com/featured/?mananchira,kozhikode"
    },
    {
        "name": "Sarovaram Bio Park",
        "tagline": "Family-friendly boating and green park",
        "image": "https://source.unsplash.com/featured/?sarovaram,kozhikode"
    },
    {
        "name": "Kadalundi Bird Sanctuary",
        "tagline": "Birdwatching and peaceful backwaters",
        "image": "https://source.unsplash.com/featured/?kadalundi,birds"
    },
    {
        "name": "Thusharagiri Waterfalls",
        "tagline": "Cool falls and mini trekking trails",
        "image": "https://source.unsplash.com/featured/?thusharagiri,waterfalls"
    },
    {
        "name": "Kakkayam Dam",
        "tagline": "Scenic dam with nature trails and waterfalls",
        "image": "https://source.unsplash.com/featured/?kakkayam,kozhikode"
    },
    {
        "name": "Peruvannamuzhi Dam & Eco Park",
        "tagline": "Eco-tourism spot with boating and garden",
        "image": "https://source.unsplash.com/featured/?peruvannamuzhi,dam"
    },
    {
        "name": "Mishkal Mosque",
        "tagline": "One of the oldest mosques with timber architecture",
        "image": "https://source.unsplash.com/featured/?mishkal,mosque"
    },
    {
        "name": "Regional Science Centre & Planetarium",
        "tagline": "Fun learning for kids with shows and exhibits",
        "image": "https://source.unsplash.com/featured/?science,planetarium"
    },
    {
        "name": "Kirtads Museum",
        "tagline": "Tribal life and heritage museum",
        "image": "https://source.unsplash.com/featured/?kirtads,museum"
    },
    {
        "name": "Vellari Mala",
        "tagline": "Hidden hill spot for nature lovers and trekking",
        "image": "https://source.unsplash.com/featured/?vellarimala,kozhikode"
    }
]

# --- Suggestion Button ---
if st.button("🎒 Suggest a Kozhikode Trip"):
    pick = random.choice(destinations)
    st.success(f"🏞️ **{pick['name']}** – {pick['tagline']}")
    st.image(pick["image"], use_column_width=True)

# --- Footer ---
st.markdown("---")
st.caption("© 2025 Chakkalakkal NFamily Trip – Kozhikode Edition")
