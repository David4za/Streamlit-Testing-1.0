import pandas as pd
import streamlit as st

st.title("Motor Selection App")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type="xlsm")

if uploaded_file:
    # Read the uploaded file
    motor_df = pd.read_excel(uploaded_file, sheet_name="Motor Type")
    gearbox_df = pd.read_excel(uploaded_file, sheet_name="Gearboxes")
    remark_table_df = pd.read_excel(uploaded_file, sheet_name="Remarks")
    
    # Select motor
    motor_types = motor_df['Motor Type'].unique()
    selected_motor = st.selectbox("Select Motor", motor_types)
    st.write(f"You selected: {selected_motor}")
