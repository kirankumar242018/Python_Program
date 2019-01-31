from OOPS_Utility.Inventory_Information import stock_Account_Shares

s1 = stock_Account_Shares()


class Stock_Account:
    try:
        # p = Accounts()
        s1.view_shares()
        print("\n1.Admin login.\n2.User login.\n3.Exit ")
        choice = int(input("\nEnter choice:->"))

        if choice == 1:
            print("\nwelcome Admin")
            print("\n1.To add Company\n2.Exit")
            j = int(input("Enter choice:-> "))

            if j == 1:
                s1.add_new_company()
                s1.view_shares()
            elif j == 2:
                exit(0)
            else:
                print("you have entered wrong input..")
        elif choice == 2:
            print("Welcome User,Hello..")
            s1.check_validity()
        elif choice == 3:
            exit(0)
        else:
            print("Invalid choice....")
    except ValueError:
        print("please enter valid input for choices...\n")
    except RuntimeError:
        print("oops something went wrong......")
