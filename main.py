import streamlit as st
import pydeck as pdk
import pandas as pd
import streamlit.components.v1 as components

st.title("Mapping Self Driving Labs")

st.markdown("""
## Outline
1. [What are Self-Driving Labs](#section-1)
2. [Self-Driving Labs Map](#section-2)
3. [Add yourself to the map!](#section-3)
""")

st.markdown("<a name='section-1'></a>", unsafe_allow_html=True)
st.header("What are Self-Driving Lab?")
st.image("robot_arm.jpg")
with open('what_are_SDL.md', 'r') as file:
  content = file.read()

st.markdown(content)

st.markdown("<a name='section-2'></a>", unsafe_allow_html=True)
st.header("Self-Driving Labs Map")

# Sample data: Latitude and Longitude of a few cities
data = pd.DataFrame({
    'lat': [42.3505, 53.4048, 35.7851],
    'lon': [-71.1054, -2.9653, -78.6813],
    'institution': [
        'Boston University', 'University of Liverpool',
        'North Carolina State University'
    ],
    'robot': [
        'UR5e, Universal Robotics', 'KUKA Mobile Robot, Mobile Platform',
        'custom microfluidic reactor'
    ]
})

# Create a layer for pydeck
layer = pdk.Layer(
    'ScatterplotLayer',
    data,
    get_position='[lon, lat]',
    get_radius=200000,  # Setting the pin size
    get_fill_color=[0, 50, 250, 150],  # Setting the pin color
    pickable=True)

# Render the map
view_state = pdk.ViewState(latitude=data.lat.mean(),
                           longitude=data.lon.mean(),
                           zoom=1,
                           pitch=0)

r = pdk.Deck(layers=[layer],
             initial_view_state=view_state,
             tooltip={"text": "{institution}\n equipment: {robot}"},
             map_style='mapbox://styles/mapbox/light-v10')

st.pydeck_chart(r)

st.markdown("<a name='section-3'></a>", unsafe_allow_html=True)
st.header("Add yourself to the Self-Driving Lab Map!")
st.markdown(
    "If you are building a self-driving lab, you can add yourself to the map by filling [out this form](https://docs.google.com/forms/d/e/1FAIpQLSfTFRaNnbOE4327bT56Q45B4o_wHGMCLDQ2yf1kz-HjYDluZA/viewform?embedded=true)."
)

st.markdown(
    "This page was created by [Charles Yang](http://charlesyang.io). All views presented here are my own. \n Feedback, ideas, or questions are welcome and can be sent to [me via email](mailto:contact@charlesyang.io)"
)

st.session_state.run_once = True
