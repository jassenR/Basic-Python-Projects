warehouse=[]
print("Choose whether to Add a product , Modify the status of the product, Remove the product or Exit")
while True:
    if len(warehouse)==0:
        pass
    else:
        total=0
        for a in warehouse:
            if a["Quan"]<=5:
                print(f"{a['Name']} , is low on stocks with only  {a['Quan']} left")
            else:
                total +=a['Price'] * a['Quan']
                print(f"{total} total inventory value")
                pass
    choice=input("Add , Modify , Remove ,Stock,View Exit\n").lower()
    if choice == "add":
        storage={
            "Name":input("Enter product name : "),
            "Quan":int(input("Quantity : ")),
            "Price":int(input("Price : ")) }
        if storage["Quan"] <= 0:
            print("Numbers cannot be negative")
            break
        elif storage["Price"]<0:
            print("Numbers cannot be negative")
            break
        else:
            pass
        check = False
        for a in warehouse:
            if a["Name"]==storage["Name"]:
                check = True
                print("Already Exist")
                break
            elif a["Quan"]<0:
                print("Numbers cannot be negative")
        if not check:
            print(f"{storage['Name']}, {storage['Quan']}, {storage['Price']}")
            warehouse.append(storage)
    elif choice == "modify":
        name=input("Enter product name : ")
        check = False
        for i in warehouse:
            if i["Name"] == name:
                check = True
                nname=input("Enter new product name : ")
                dupli = False
                for a in warehouse:
                    if a["Name"]==nname:
                        dupli = True
                        break
                if dupli:
                    print("Already Exist")
                else:
                    i["Name"] = nname
                nprice=int(input("new Price : "))
                if nprice <0:
                    print("Numbers cannot be negative")
                    break
                else:
                    i["Price"] = nprice
                    break
        if not check:
                print("Not Found")
    elif choice == "stock":
        name=input("Enter product name : ")
        check = False
        for i in warehouse:
            if i["Name"] == name:
                check = True
                print(i["Quan"])
                question=int(input("Stocking up select 1 , Stocking down select 2"))
                if question==1:
                    a=int(input("How many ? : "))
                    if a <0:
                        print("Cannot Stock down")
                    else:
                        i["Quan"] +=a
                elif question==2:
                    a=int(input("How many ? : "))
                    if a <0:
                        print("Cannot number is negative")
                    elif i["Quan"]-a < 0:
                        print("Number cannot be negative")
                    else:
                        i["Quan"] -=a

                    break
                else:
                    print("Invalid")
        if not check:
                print("Not Found")
    elif choice == "remove":
        name=input("Enter product name : ")
        check = False
        for i in warehouse:
            if i["Name"] == name:
                check = True
                warehouse.remove(i)
                print(f"Successfully Removed {i['Name']}")
                break
        if not check:
            print("Not Found")
    elif choice == "view":
        if len(warehouse)==0:
            print("Inventory Empty ")
        else:
            print("Inventory")
            for a in warehouse:
                print(f"{a['Name']}, {a['Quan']}, {a['Price']}")

    elif choice == "exit":
        break
    else:
        print("Invalid Choice")
