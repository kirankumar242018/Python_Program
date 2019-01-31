import json


from OOPS_Utility.Inventory_Information import Test_Oops
t1 = Test_Oops()


class Inventory_Management:
    try:
        with open("Inventory_Data1.json", "r") as file:
            # print(json.loads(file.read())) # loads deserializes as string
            # print(json.load(file)          # load deserializes as fp (file pointer)
            jason_File = file.read()
            file.close()

            item = json.loads(jason_File)

            t1.inventory_information(item)
    except RuntimeError:
        print("oops something went wrong..\n")
