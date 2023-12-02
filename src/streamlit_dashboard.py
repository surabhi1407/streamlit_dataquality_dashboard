import streamlit as st
import pandas as pd
import numpy as np
import datetime

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
file_path = './data/data_quality_checks_results.csv'

def dashboard_main():
    # Load data
    df = load_data(file_path)

    # Dashboard Title
    st.title('Data Quality Metric Monitoring Dashboard')

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    date_range_tuple = st.date_input(
        "Select date range to see the Data Quality Metric",
        value=(last_week, datetime.date.today()),
        min_value=datetime.date(2022, 12, 1),
        max_value=datetime.date.today(),
        format="MM.DD.YYYY",
    )

    if date_range_tuple:
        if len(date_range_tuple) == 1:
            start_date = end_date = date_range_tuple[0]
        else:
            start_date = date_range_tuple[0]
            end_date = date_range_tuple[1]

    if start_date > end_date:
        st.error('Error: End date must fall after start date.')

    # Filter the DataFrame based on the selected date range
    filtered_df = df[
        (df['Check Run Date'] >= pd.to_datetime(start_date)) & (df['Check Run Date'] <= pd.to_datetime(end_date))]

    # Create a 'month' column
    filtered_df['month'] = filtered_df['Check Run Date'].dt.to_period('M')

    # Calculate DQ scores
    overall_dq_score, category_scores = calculate_dq_scores(filtered_df)

    # Metrics
    with st.container():
        st.divider()
        c1, c2, c3 = st.columns(3)
        with c1, st.container(), st.expander(label=':ballot_box_with_check:', expanded=True):
            st.metric("Overall DQ Score", overall_dq_score)

        with c2, st.container(), st.expander(label=':ballot_box_with_check:', expanded=True):
            st.metric("Rows Scanned", df['Rows Scanned'].sum())

        with c3, st.container(), st.expander(label=':ballot_box_with_check:', expanded=True):
            st.metric("Rows Failed", df['Rows Failed'].sum())

    # Determine the number of categories
    num_categories = len(category_scores)
    st.divider()
    # Create columns dynamically based on the number of categories
    cols = st.columns(num_categories)

    # Iterate over category scores and create a widget for each
    for i, (category, score) in enumerate(category_scores.items()):
        with cols[i % num_categories], st.container(), st.expander(label=':ballot_box_with_check:', expanded=True):
            cols[i % num_categories].progress(score)
            cols[i % num_categories].write(category)

    st.divider()


    # Historical DQ Score Trend
    st.subheader("DQ Score Trend")
    filtered_df['month'] = filtered_df['Check Run Date'].dt.to_period('M')
    monthly_scores = filtered_df.groupby('month').apply(lambda x: np.random.randint(50, 100)) # Replace with real calculation
    st.line_chart(monthly_scores)

