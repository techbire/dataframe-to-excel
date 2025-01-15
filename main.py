import streamlit as st
import pandas as pd

# Function to process and display the Excel file
def process_file(file):
    df = pd.read_excel(file)

    result = ""
    for _, row in df.iterrows():
        for col in df.columns:
            value = row[col]
            
            # Apply bold for DSA Topics
            if 'DSA Topic' in col:
                value = f"**{value}**"
            
            # Apply italics for Subtopics/Tasks
            if 'Subtopics/Tasks' in col:
                value = f"*{value}*"
            
            # Display the column and value
            result += f"{col}: {value}\n"
        result += "\n"
    
    return result

# Streamlit UI
st.title("Excel Upload and Convert to Text")

# File uploader widget
uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx")

# If file is uploaded, process and display the result
if uploaded_file is not None:
    result_text = process_file(uploaded_file)
    st.text(result_text)
else:
    st.info("Please upload an Excel file.")
