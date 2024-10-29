import streamlit as st
import pandas as pd
import pickle
from functions import get_complaint_info  # Import from the new module

# Load the DataFrame
try:
    df = pd.read_csv("Final_AB_Complaint_Classification_Restaurant.csv")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Load the dictionary from the pickle file
try:
    with open('complaint_functions3.pkl', 'rb') as f:
        functions_dict = pickle.load(f)
except Exception as e:
    st.error(f"Error loading functions: {e}")
    st.stop()

# Access the specific function
get_complaint_info = functions_dict.get('get_complaint_info')

# Streamlit application title
st.title("Complaint Counts Dashboard")

# Input for days
days = st.number_input("Enter the number of days:", min_value=1, value=30)

# Submit button
if st.button("Get Complaint Info"):
    if days <= 0:
        st.error("Please enter a positive number of days.")
    else:
        with st.spinner("Fetching complaint information..."):
            result = get_complaint_info(df, days)  # Call the function with the DataFrame and days

        # Display total complaints
        st.write("Total Complaints:", result['total_complaints'])

        # Display category counts
        st.write("Category Counts:")
        categories = result['categories'].split(', ')
        counts = result['counts'].split(', ')

        for category, count in zip(categories, counts):
            st.write(f"{category}: {count}")

        # Display detailed reviews information
        st.write("Reviews Information:")
        reviews_df = result['reviews']

        reviews_df.columns = ['Review', 'Category', 'Severity', 'Urgency', 'Is Repeated']
        st.dataframe(reviews_df.reset_index(drop=True))   # Hide index column in the DataFrame display
