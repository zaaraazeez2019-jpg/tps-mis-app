import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("TPS_Transactions").sheet1

# Item database
items = {
    "JBL Black Headphones": {"code": "H001", "price": 5000},
    "Samsung Galaxy S24 Black 256GB Mobile Phone": {"code": "M002", "price": 350000},
    "Mac Book Air 2024 16GB RAM Rose Gold Laptop": {"code": "L003", "price":280000},
    "Logitech Wireless Keyboard & Mouse Black": {"code": "A004", "price": 8000}
}

# App Title
st.title("TPS Data Entry System")

# Inputs
employee = st.text_input("Employee Name")
item = st.selectbox("Select Item", list(items.keys()))
quantity = st.number_input("Quantity", min_value=1)

# Pricing
unit_price = items[item]["price"]
total_price = unit_price * quantity

st.write("Unit Price:", unit_price)
st.write("Total Price:", total_price)

# Submit Transaction
if st.button("Submit"):
    transaction_id = len(sheet.get_all_values())
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sheet.append_row([
        transaction_id,
        time_now,
        items[item]["code"],
        item,
        quantity,
        unit_price,
        total_price,
        employee
    ])

    st.success("Transaction saved!")
