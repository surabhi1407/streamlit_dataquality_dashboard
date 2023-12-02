import streamlit as st
from streamlit_dashboard import dashboard_main
from streamlit_logboard import logboard_main
import datetime

st.set_page_config(
        page_title="Data Quality Monitor",
        page_icon="✔️",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def intro():
    st.title('Data Quality Monitoring')
    st.markdown("---")
    st.markdown(
        """
        ### 
        > This application tracks and monitors data integrity issues in ingested Data                  
        """)


if __name__ == "__main__":
    # main page
    tab1, tab2, tab3= st.tabs(["Intro","DQ Dashboard", "DQ Logboard"])
    with tab1:
        intro()
    with tab2:
        dashboard_main()
    with tab3:
        logboard_main()
