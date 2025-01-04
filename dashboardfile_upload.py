import streamlit as st
import pandas as pd
from time import strftime, time
import uuid

class FileUpload:
    def __init__(self):
        self.df = None
        self.setup_page()

    def setup_page(self):
        st.set_page_config(page_title="Test", page_icon=":bar_chart:", layout="wide")
        st.title(" :bar_chart: Financial Dashboard")
        st.markdown('<style>div.block-container{padding-top:2.5rem;}</style>', unsafe_allow_html=True)

        if "show_time" not in st.session_state:
            st.session_state.show_time = False
            st.session_state.last_click_time = 0

        self.button_click()
        self.display_clock()


    def display_clock(self):
        clock_placeholder = st.empty()
        current_time = strftime('%H:%M %p')

        # Check if the current time should be displayed
        if st.session_state.show_time:
            elapsed_time = time() - st.session_state.last_click_time
            if elapsed_time > 60:
                st.session_state.show_time = False
            else:
                clock_placeholder.markdown(
                    f"<h1 style='display: inline; float: right;'>{current_time}</h1>",
                    unsafe_allow_html=True
                )

    
    def button_click(self):
        if st.button("Check the current time"):
            st.session_state.show_time = True
            st.session_state.last_click_time = time()

    def load_data(self):
        unique_key = str(uuid.uuid4())
        file = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"],key=unique_key)
        if file is not None:
            self.df = pd.read_csv(file, encoding="ISO-8859-1")
        else:
            self.df = pd.read_csv("Test.csv", encoding="ISO-8859-1")

