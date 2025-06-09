import streamlit as st

# Set page configuration
st.set_page_config(page_title="Smart Parking System", layout="centered")

# Title of the app
st.title(" Smart Parking System")

# Brief description
st.markdown("""
Welcome to the Smart Parking System!

This system is designed to improve urban parking experiences using a combination of **Computer Vision**, **IoT**, and **Navigation Technologies**. Key features include:

- 📸 Real-time detection of available parking spots using camera feeds.
- 📊 Prediction of parking availability based on historical data.
- 🧭 Indoor navigation using BLE beacons to guide users to vacant spots.
- 🌐 Integrated with mapping APIs for route and ETA prediction before arrival.

Explore the future of smart parking – efficient, automated, and user-friendly.
""")
