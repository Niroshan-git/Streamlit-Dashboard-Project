import time
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
from utils import dataframe_to_pdf
from streamlit_option_menu import option_menu

class MainCharts:
    def __init__(self, filtered_df):
        self.filtered_df = filtered_df

    def progress_bar(self):
        st.markdown("""
                <style>
                    .stProgress > div > div > div > div {
                        background-image: linear-gradient(to right, #99ff99, #FFF00);
                    }
                </style>
            """, unsafe_allow_html=True)
        target = 80000000
        current = self.filtered_df["Total Profit"].sum()
        percent = round((current/target*100))
        mybar = st.progress(0)

        if percent > 100:
            st.subheader("Target Done!")
        else:
            st.write("You have ", percent,"% ", "of", (format(target, 'd')), "LKR")
            for percent_complete in range(percent):
                time.sleep(0.1)
                mybar.progress(percent_complete + 1, text= "Target Profit Percentage")

    def tabular(self):
        with st.expander("Tabular"):
            showData = st.multiselect('Filter: ',self.filtered_df.columns,default=[])
            st.write(self.filtered_df[showData])

    def main_menu(self):

        col1, col2 = st.columns([5,1])
        with col2:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Progress"],
                icons=["house", "eye"],
                menu_icon="cast",
                default_index=0
            )
        with col1:
            if selected == "Home":
                st.subheader(f"Page: {selected}")
                self.tabular()
            elif selected == "Progress":
                st.subheader(f"Page: {selected}")
                self.progress_bar()




    def top_Analysis(self):
        # Compute the top analysis
        total_sales = (self.filtered_df["Units Sold"]).sum()
        total_revenue = (self.filtered_df["Total Revenue"].sum())
        total_cost = (self.filtered_df["Total Cost"].sum())
        total_profit = (self.filtered_df["Total Profit"].sum())
        profit_percentage = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

        columns =st.columns(4, gap='large')

        with columns[0]:
            st.info('Total Sales', icon=":material/shopping_bag:")
            st.metric(label="Sum LKR", value=f"{total_sales:,.0f}")

        with columns[1]:
            st.info('Total Revenue',icon=":material/paid:")
            st.metric(label="Sum LKR", value=f"{total_revenue:,.0f}"
                     )

        with columns[2]:
            st.info('Total Cost',icon=":material/credit_card:")
            st.metric(label="Sum LKR", value=f"{total_cost:,.0f}")

        with columns[3]:
            st.info('Total Profit', icon=":material/payments:")
            st.metric(label="Sum LKR", value=f"{total_profit:,.0f}")
            placeholder = st.empty()

            for i in range(int(profit_percentage) + 1):
                time.sleep(0.05)  # Adjust the sleep time to control the speed of the animation

                if i > 0:
                    placeholder.metric(label="Profit Percentage", value=f"{i}%", delta="Going up")
                else:
                    placeholder.metric(label="Profit Percentage", value=f"{i}%", delta="Going down ")

    def plot_item_sales(self):

        item_type_df = self.filtered_df.groupby(by=["Item Type"], as_index=False)["Units Sold"].sum()
        st.subheader("Item wise Sale")
        fig = px.bar(item_type_df, x="Item Type", y="Units Sold", text=[f'{x:,}' for x in item_type_df["Units Sold"]],
                             template="seaborn")
        st.plotly_chart(fig, use_container_width=True)
        csv = item_type_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Item Wise Sale.csv", mime="text/csv",
                                   help='Click here to download the data as a csv file')


    def plot_region_sales(self):

        st.subheader("Region wise Sale")
        fig = px.pie(self.filtered_df, values="Units Sold", names="Region", hole=0.5)
        fig.update_traces(text=self.filtered_df["Region"], textposition="outside")
        st.plotly_chart(fig, use_container_width=True)




        col1, col2 = st.columns(2)
        with col1:
            region = self.filtered_df.groupby(by=["Region"], as_index=False)["Units Sold"].sum()
            csv = region.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data as CSV", data=csv, file_name="Region.csv", mime="text/csv",
                                   help='Click here to download the data as a csv file')

        with col2:
            pdf_file = dataframe_to_pdf(region)
            with open(pdf_file, "rb") as f:
                pdf_data = f.read()
            st.download_button("Download Data as PDF", data=pdf_data, file_name="Region.pdf", mime="application/pdf",
                               help='Click here to download the data as a PDF file')

    def plot_time_series(self):
        self.filtered_df["month"] = self.filtered_df["Order Date"].dt.to_period("M")
        self.filtered_df["year"] = self.filtered_df["Order Date"].dt.to_period("Y")
        st.subheader('Time Series Profit Analysis')

        selection = st.radio('Choose Month wise or Year wise', ('Month-Wise', 'Year-Wise'))
        self.filtered_df["time_period"] = self.filtered_df[selection.split('-')[0].lower()]

        linechart = pd.DataFrame(self.filtered_df.groupby(self.filtered_df["time_period"].dt.strftime("%Y-%m"))["Total Profit"].sum()).reset_index()
        linechart.columns = ["time_period", "Total Profit"]

        fig2 = px.line(linechart, x="time_period", y="Total Profit", labels={"Total Profit": "Total Profit"}, height=500,
                       width=1000, template="gridon")
        st.plotly_chart(fig2, use_container_width=True)

        with st.expander("View Data of the TimeSeries:"):
            st.write(linechart.T.style.background_gradient(cmap="Blues"))
            csv = linechart.to_csv(index=False).encode("utf-8")
            st.download_button('Download Data', data=csv, file_name="TimeSeries.csv", mime='text/csv')

    def plot_treemap(self):
        st.subheader("Hierarchical view of Sales using TreeMap")
        fig3 = px.treemap(self.filtered_df, path=["Region", "Country", "Item Type"], values="Units Sold", hover_data=["Units Sold"],
                          color="Region")
        fig3.update_layout(width=800, height=650)
        st.plotly_chart(fig3, use_container_width=True)

    def display_summary_table(self):
        st.subheader(":point_right: Month wise Sales Summary")
        with st.expander("Summary_Table"):
            df_sample = self.filtered_df[["Region", "Units Sold", "Country", "Total Profit"]].head(7)
            fig = ff.create_table(df_sample, colorscale="Cividis")
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("Month wise Total Profit Table")
            self.filtered_df["month"] = self.filtered_df["Order Date"].dt.month_name()
            sales_category_Year = pd.pivot_table(data=self.filtered_df, values="Total Profit", index=["Country"], columns="month")
            st.write(sales_category_Year.style.background_gradient(cmap="Blues"))
