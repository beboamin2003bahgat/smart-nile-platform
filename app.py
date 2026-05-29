import streamlit as st
import pandas as pd

st.title("Smart Nile Platform")

data = {
    "Device": [
        "FortiGate Firewall",
        "Cisco Switch",
        "Dell Server"
    ],
    "Vendor": [
        "Fortinet",
        "Cisco",
        "Dell"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df)