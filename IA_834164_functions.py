
import pandas as pd
import os

def verify_user(ic_number, password): #Verify user's and check IC number 12 digits, last 4 digits for password
    return len(ic_number) == 12 and password == ic_number[-4:]

def calculate_tax(income, tax_relief): #Calculate tax payable based on Malaysian tax rates for current year (2024)
    taxable_income = income - tax_relief

    if taxable_income <= 5000:
        return 0
    elif taxable_income <= 20000:
        tax = taxable_income * 0.01
    elif taxable_income <= 35000:
        tax = 150 + (taxable_income - 20000) * 0.03
    elif taxable_income <= 50000:
        tax = 600 + (taxable_income - 35000) * 0.06
    else:
        tax = 1500 + (taxable_income - 50000) * 0.11
    return round (tax, 2)

def save_to_csv(data, filename = "Record_Tax.csv"):  #Append new data or create a new csv if not exists
    df = pd.DataFrame([data])
    if os.path.exists(filename):
        df.to_csv(filename, mode = 'a' , header = False, index = False)
    else:
        df.to_csv(filename, index = False)

def file_read_from_csv(filename = "Record_Tax.csv"): #Read data from existing file
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return None