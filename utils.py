import json
import requests
from fpdf import FPDF

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", size=12)
        self.cell(200, 10, txt="Region wise Sale", ln=True, align='C')
        self.ln(10)

    def table(self, data):
        self.set_font("Arial", size=12)
        # Column headers
        self.cell(100, 10, txt="Region", border=1)
        self.cell(100, 10, txt="Units Sold", border=1)
        self.ln()
        # Data rows
        for i in range(len(data)):
            row = data.iloc[i]
            self.cell(100, 10, txt=row['Region'], border=1)
            self.cell(100, 10, txt=str(row['Units Sold']), border=1)
            self.ln()

def dataframe_to_pdf(df, file_name="data.pdf"):
    pdf = PDF()
    pdf.add_page()
    pdf.table(df)
    pdf.output(file_name)
    return file_name
