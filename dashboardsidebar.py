import streamlit as st
import pandas as pd
import json
import requests
from streamlit_lottie import st_lottie

class Sidebar:
    def __init__(self, df):
        self.df = df

    def load_lottieurl(self, url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    def filter_data(self):
        st.sidebar.header("Choose your filter")
        lottie_hello = self.load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_w51pcehl.json")

        with st.sidebar:
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low",
                height=None,
                width=None,
                key=None,
            )

        # Date picker
        col1, col2 = st.columns(2)
        self.df["Order Date"] = pd.to_datetime(self.df["Order Date"])

        # Getting min and max date
        startDate = pd.to_datetime(self.df["Order Date"]).min()
        endDate = pd.to_datetime(self.df["Order Date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))
        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        # Filtering the data frame based on the selected date range
        df_filtered_by_date = self.df[(self.df["Order Date"] >= date1) & (self.df["Order Date"] <= date2)].copy()

        # Sidebar filter pane
        region = st.sidebar.multiselect("Pick your Region", df_filtered_by_date["Region"].unique())
        country = st.sidebar.multiselect("Pick your Country", df_filtered_by_date[df_filtered_by_date["Region"].isin(region)]["Country"].unique())
        item_type = st.sidebar.multiselect("Pick your Item Type", df_filtered_by_date[df_filtered_by_date["Country"].isin(country)]["Item Type"].unique())

        if region:
            df_filtered_by_date = df_filtered_by_date[df_filtered_by_date["Region"].isin(region)]
        if country:
            df_filtered_by_date = df_filtered_by_date[df_filtered_by_date["Country"].isin(country)]
        if item_type:
            df_filtered_by_date = df_filtered_by_date[df_filtered_by_date["Item Type"].isin(item_type)]

        lottie_hello = self.load_lottieurl("https://lottie.host/0eb98c91-1cb6-4cc7-9da5-a624fb5247d5/Mz7KAGDcBw.json")

        with st.sidebar:
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low",
                height=None,
                width=None,
                key=None,
            )

        return df_filtered_by_date

