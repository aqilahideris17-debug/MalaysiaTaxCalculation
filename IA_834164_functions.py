
import pandas as pd
import os
import csv

#--------------------------------------------------------Registration Function-------------------------------------------------------
def register_user(user_id, ic_number, filename = "Registered_Users.csv"): #Register new user by saving ID and IC number to a CSV file
    df = pd.DataFrame([[user_id, ic_number]], columns=["User ID", "IC Number"])
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)
    print("Registration successful! You can now log in.")

def check_user_exists(user_id, filename = "Registered_Users.csv"): #Check if a user ID already exists in the registration file
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        return user_id in df["User ID"].values
    return False

def get_registered_ic(user_id, filename = "Registered_Users.csv"): #Retrieve the IC number of a registered user by their ID
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        user_row = df.loc[df["User ID"] == user_id]
        if not user_row.empty:
            return str(user_row.iloc[0]["IC Number"])
    return None

#---------------------------------------------------------System Function------------------------------------------------------------
def verify_user(ic_number, password): #Verify user's and check IC number 12 digits, last 4 digits for password
    return len(ic_number) == 12 and password == ic_number[-4:]

def calculate_tax(income, tax_relief): #Calculate tax payable based on Malaysian tax rates for current year (2024)
    taxable_income = income - tax_relief

    tax_brackets = (5000, 20000, 35000, 50000)

    if taxable_income <= tax_brackets[0]:
        return 0
    elif taxable_income <= tax_brackets[1]:
        tax = taxable_income * 0.01
    elif taxable_income <= tax_brackets[2]:
        tax = 150 + (taxable_income - 20000) * 0.03
    elif taxable_income <= tax_brackets[3]:
        tax = 600 + (taxable_income - 35000) * 0.06
    else:
        tax = 1500 + (taxable_income - 50000) * 0.11
    return round (tax, 2)

#--------------------------------------------------------Record File Function--------------------------------------------------------
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

