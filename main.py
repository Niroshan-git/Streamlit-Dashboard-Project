import streamlit as st
from dashboardfile_upload import FileUpload
from dashboardsidebar import Sidebar
from dashboardmain_charts import MainCharts


def main():
    file_upload = FileUpload()
    file_upload.load_data()



    if file_upload.df is not None:
        sidebar = Sidebar(file_upload.df)
        filtered_df = sidebar.filter_data()

        main_charts = MainCharts(filtered_df)
        main_charts.main_menu()
        main_charts.top_Analysis()
        main_charts.plot_item_sales()
        main_charts.plot_region_sales()
        main_charts.plot_time_series()
        main_charts.plot_treemap()
        main_charts.display_summary_table()


if __name__ == "__main__":
    main()
