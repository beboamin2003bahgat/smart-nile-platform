import streamlit as st
import pandas as pd

st.title("Smart Nile Platform")

uploaded_file = st.file_uploader(
    "Upload Devices CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("devices.csv")

search = st.text_input("Search Device")

if search:
    df = df[df["Device"].str.contains(search, case=False)]

st.dataframe(df)

selected_device = st.selectbox(
    "Select Device",
    df["Device"]
)

device_info = df[df["Device"] == selected_device]

st.subheader("Device Details")
st.write(device_info)