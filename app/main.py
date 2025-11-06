import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="SeeAlong", page_icon="🗺️")

st.title("🗺️ Welcome to SeeAlong!")
st.subheader("Discover and review the most scenic routes.")

# Create base map centered at San Francisco
m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)

# Display map inside Streamlit
st_data = st_folium(m, width=700, height=450)

st.info("This is your base map view. Phase 2 will add route search and reviews!")
