from IA_834164_functions import verify_user, calculate_tax, save_to_csv, file_read_from_csv

def main():
    print("Hello! Welcome to Malaysia Tax Input Program System!")

    print()
    
    while True:  
        #-------------------------------------------------------Login Loop------------------------------------------------------------
        while True:
            ic_number = input("Enter your IC number : ")

            if len(ic_number) != 12 or not ic_number.isdigit():  #Check IC length and digits only, make sure 12 digits
                print("Invalid IC Number! Please enter a valid 12 digit IC number!")
                continue

            print()

            password = input("Enter your last 4 digits of your IC as password : ")

            if verify_user(ic_number, password):  #Verify user's IC and check if password matches the last 4 digits.
                print("\n Login successful! \n")
                break
            else:
                print("Invalid credentials! Please check and try again!")

        #----------------------------------------------------After successful login--------------------------------------------------
        while True:
            try:
                income = float(input("Enter your annual income (RM) : "))
                break
            except ValueError:
                print("Please make sure you enter a valid number for income!")

        print()

        while True:
            try:
                tax_relief = float(input("Enter your tax relief amount (RM) : "))
                break
            except ValueError:
                print("Please make sure you enter a valid number for tax relief!")

        print()
        
        tax = calculate_tax(income, tax_relief)
        print(f"Your calculated tax payable is : RM {tax:.2f}")

        data = {
            "IC Number" : ic_number,
            "Annual Income" : income,
            "Tax Relief" : tax_relief,
            "Tax Payable" : tax
        }

        save_to_csv(data)

        print()

        print("All saved Tax Records:")

        records = file_read_from_csv()
        if records is not None:
            print(records)
        else:
            print("Sorry! No records were found!")

        #-------------------------------------------------Ask user to proceed or exit--------------------------------------------
        print()

        cont = input("Do you want to continue using the system? (Y/N) : ").strip().lower()

        if cont != 'y':
            print("\n Thank you for using the Malaysia Tax Input Program System. Goodbye!")
            break  #exits system

if __name__ == "__main__":
    main()
