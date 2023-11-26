import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Load the CSV data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    # Convert check run date to datetime
    data['Check Run Date'] = pd.to_datetime(data['Check Run Date'])
    return data

# Function to calculate DQ scores
def calculate_dq_scores(data):
    # Here you would calculate the overall DQ score and scores per category based on your criteria
    # For simplicity, we are using dummy calculations
    overall_dq_score = np.random.randint(90, 100)
    category_scores = {
        'Completeness': np.random.randint(50, 100),
        'Timeliness': np.random.randint(50, 100),
        'Validity': np.random.randint(50, 100),
        'Accuracy': np.random.randint(50, 100),
        'Consistency': np.random.randint(50, 100),
        'Uniqueness': np.random.randint(50, 100)
    }
    return overall_dq_score, category_scores

# Path to your CSV file
file_path = './data/data_quality_checks_results.csv'  # Replace with the path to your CSV file

# Load data
df = load_data(file_path)

# Calculate DQ scores
overall_dq_score, category_scores = calculate_dq_scores(df)

# Dashboard Title
st.title('Data Quality Dashboard')

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Overall DQ Score", overall_dq_score)
col2.metric("Total Rows Processed", df['Rows Scanned'].sum())
col3.metric("Failed Rows", df['Rows Failed'].sum())

with st.container():
    st.divider()
    c1, c2, c3, c4 = st.columns(4)
    with c1, st.container(), st.expander(label=':ballot_box_with_check:', expanded=True):
        st.metric("Overall DQ Score", overall_dq_score)

    with c2, st.container(), st.expander(label=':ballot_box_with_check:', expanded=True):
        st.metric("Checks Run", df['Rows Scanned'].sum())

    with c3, st.container(), st.expander(label=':ballot_box_with_check:', expanded=True):
        st.metric("Checks Failed", df['Rows Failed'].sum())

# Category scores
cols = st.columns(5)
for i, (category, score) in enumerate(category_scores.items()):
    cols[i].progress(score)
    cols[i].write(category)

# Historical DQ Score Trend
st.subheader("Overall DQ Score - Last 12 Months")
df['month'] = df['Check Run Date'].dt.to_period('M')
monthly_scores = df.groupby('month').apply(lambda x: np.random.randint(50, 100)) # Replace with real calculation
st.line_chart(monthly_scores)
