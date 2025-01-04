# Financial Dashboard

A comprehensive Streamlit-based financial analytics dashboard for visualizing and analyzing sales, revenue, and profit data across different regions and product categories.

![Capture](https://github.com/user-attachments/assets/39ef2b4c-1a45-401a-b6d7-02a00c24ddf6)


## 📊 Features

- **Item-wise Sales Analysis**: Bar chart visualization showing sales distribution across different product categories including Baby Food, Beverages, Cereal, Clothes, Cosmetics, and more
- **Regional Sales Distribution**: Interactive donut chart displaying sales distribution across regions:
  - Sub-Saharan Africa (27.4%)
  - Europe (25.4%)
  - Middle East and North Africa (13.9%)
  - Asia (13.4%)
  - Other regions including Central America, Australia, and North America
  - 
 ![Capture01](https://github.com/user-attachments/assets/5c8b8e6f-674c-44ac-8a51-e77087cd245f)

![Capture03](https://github.com/user-attachments/assets/675891d2-4dc2-44b3-acda-f301a395490b)



- **Time Series Analysis**:
  - Monthly and yearly profit trends (2010-2017)
  - Interactive date range selection
  - Detailed profit metrics visualization
 
  ![Capture04](https://github.com/user-attachments/assets/0f196d72-777f-4ab8-b955-50322e1fd734)

- **Hierarchical Sales Visualization**: TreeMap representation of sales data organized by:
  - Regions
  - Countries
  - Product categories
 
    ![Capture05](https://github.com/user-attachments/assets/121eb109-39ef-4dd6-9469-c4c81236f285)
    
    ![Capture06](https://github.com/user-attachments/assets/76d6db2b-36b0-4caa-a731-9bafe78d50b4)


- **Financial Metrics Dashboard**:
  - Total Sales: 5,053,988 units
  - Total Revenue: 1,327,321,840 LKR
  - Total Cost: 936,119,229 LKR
  - Total Profit: 391,202,612 LKR (29% profit margin)

- **Additional Features**:
  - File upload functionality (CSV, TXT, XLSX, XLS)
  - Date range filtering
  - Downloadable data in CSV and PDF formats
  - Responsive design with dark mode interface

## 🚀 Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/financial-dashboard.git
cd financial-dashboard
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📦 Requirements

```text
streamlit>=1.20.0
pandas>=1.4.0
plotly>=5.10.0
numpy>=1.22.0
```

## 🏃‍♂️ Running the Dashboard

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

## 📁 Data Format

The dashboard accepts data files in the following formats:
- CSV
- TXT
- XLSX
- XLS

Maximum file size: 200MB

Expected data columns:
- time_period
- region
- country
- item_type
- units_sold
- total_profit
- total_revenue
- total_cost

## 🔍 Usage

1. **Data Upload**:
   - Use the file upload section to import your data
   - Supported formats: CSV, TXT, XLSX, XLS
   - Maximum file size: 200MB

2. **Filtering Options**:
   - Region selection
   - Country selection
   - Item type selection
   - Date range selection

3. **Visualization Options**:
   - Bar charts for item-wise analysis
   - Donut chart for regional distribution
   - Time series graph for profit trends
   - TreeMap for hierarchical sales view
   - Tabular data view

4. **Data Export**:
   - Download as CSV
   - Download as PDF
   - View raw data tables

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

