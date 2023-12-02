import streamlit as st
import datetime

def logboard_main():

    st.title('Data Quality Check Logboard')
    form_container = st.empty()
    df_container = st.empty()
    info_container = st.empty()
    df_key_counter = 1

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    with form_container:
        date_range_tuple = form_container.date_input(
            "Select date range to see log",
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
