# 📊 Streamlit Dashboard Project

A dynamic and interactive dashboard built with Streamlit for visualizing and analyzing sales data.



---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Key Functions and Components](#key-functions-and-components)
- [Libraries Used](#libraries-used)
- [Installation and Usage](#installation-and-usage)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 📁 **File upload** for CSV, TXT, XLSX, and XLS files
- 🔍 **Dynamic data filtering** (date range, region, country, item type)
- 📊 **Multiple chart types**:
  - Bar charts for item-wise sales
  - Pie charts for region-wise sales
  - Time series analysis for profit
  - Treemap for hierarchical sales view
- 📑 **Summary tables** with styling
- 📈 **Progress bar** for target achievement
- 📥 **Downloadable reports** (CSV and PDF)
- 🕒 **Current time display**

---

## Project Structure

```bash
streamlit-dashboard/
├── main.py                # Main file for the Streamlit app
├── utils.py               # Utility functions (e.g., PDF export)
├── dashboardfile_upload.py # Handles file uploads
├── dashboardsidebar.py    # Handles the sidebar UI and filtering
├── dashboardmain_charts.py # Creates and displays the main charts
└── requirements.txt       # Lists the required packages
```

---

## How It Works

  - User uploads a file or the app loads a default CSV.
-   Sidebar allows data filtering.
  - **Main area displays various charts and analyses**:
      -  Top analysis (sales, revenue, cost, profit)
      -  Item-wise sales bar chart
      -  Region-wise sales pie chart
      -    Time series profit analysis
      -   Hierarchical sales treemap
      -  Summary tables
