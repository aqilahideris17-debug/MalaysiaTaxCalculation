from IA_834164_functions import register_user, check_user_exists, get_registered_ic, verify_user, calculate_tax, save_to_csv, file_read_from_csv

def main():
    print("Hello! Welcome to Malaysia Tax Input Program System!")

    print()
    
    while True:  
        print("1. Login")
        print("2. Register New User")
        print("3. Exit System \n")

        choice = input("Select an option (1/2/3) : ").strip()

        #---------------------------------------------------Register New User ---------------------------------------------------------
        if choice == '2':
            print("\n--- User Registration ---")
            user_id = input("Enter a new User ID : ").strip()
            ic_number = input("Enter your 12-digit IC number : ").strip()

            if len(ic_number) != 12 or not ic_number.isdigit():
                print("Invalid IC number! Please enter exactly 12 digits")
                continue

            print()

            if check_user_exists(user_id):
                print("User ID already registered! Please choose 1. Login instead")
            else:
                register_user(user_id, ic_number)

        #--------------------------------------------------Login Existing User--------------------------------------------------------
        elif choice == '1':
            print("\n--- User Login ---")
            user_id = input("Enter your User ID : ").strip()

            if not check_user_exists(user_id):
                print("\n USER NOT FOUND! PLEASE REGISTER FIRST! \n")
                continue

            ic_number = get_registered_ic(user_id)
            password = input("Enter your password (last 4 digits of your IC): ").strip()

            if verify_user(ic_number, password):
                print("\nLogin successful!\n")

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
                    "User ID" : user_id,
                    "IC Number" : ic_number,
                    "Annual Income" : income,
                    "Tax Relief" : tax_relief,
                    "Tax Payable" : tax
                }

                save_to_csv(data)

                print()

                print("All saved Records Tax :")

                records = file_read_from_csv()
                if records is not None:
                    print(records)
                else:
                    print("Sorry! No records were found!")

                print()

                cont = input("Do you want to continue using the system? (Y/N) : ").strip().lower()
                if cont != 'y':
                    print("\n Thank you for using the Malaysia Tax Input Program System. Goodbye!")
                    break
            else:
                print("Invalid password! Please check and try again.\n")

                print()

        #------------------------------------------------------------Exit System --------------------------------------------------
        elif choice == '3':
            print("Thank you for using the Malaysia Tax Input Program System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()

