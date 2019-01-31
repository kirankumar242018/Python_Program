import json

from OOPS_Utility.Inventory_Information import stock_Linked_list


class stock_linkedList:
    try:
        with open("Stock.json","r") as content:
            new_file = content.read()
            content.close()
            item = json.loads(new_file)
            l1 = stock_Linked_list(item)
            l1.add_companyShares()
    except Exception as e:
        print(e)