from OOPS_Utility.Inventory_Information import Test_Regex

t1 = Test_Regex()


class Regular_Expression:
    try:

        print("enter your  full_name............\n")
        full_name = str(input())

        while full_name.isdigit() is True or full_name.isidentifier() is True:
            print("enter your proper full_name that should not contain any numeric or special characters............\n")
            print("enter your  full_name............\n")
            full_name = str(input())

        print()

        print("enter your contact_no...........\n")
        contact_no = input()
        while contact_no.isalpha() is True or len(contact_no) > 12 or len(contact_no) < 12:
            print("enter valid input contact_no should not contain any characters and format should be like "
                  "111-111-1111 its  length should be 12..\n")
            print("enter your  contact numbers............\n")
            contact_no = str(input())

        t1.regular_expression(full_name, contact_no)

    except ValueError:
        print("enter valid input.............\n")

    except RuntimeError:
        print("oops something went wron.......\n")
