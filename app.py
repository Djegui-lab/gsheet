# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1lVEnNDRIjw-9TC6MipteJ0RvA1e9Ve7p-IE4TGYVXIo/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet=427152267)
st.dataframe(data)


