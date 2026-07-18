print("This is a Student Record System choose below\n")
records =[]
if "a" in records:
    print(records )
while True:
    choice=input("Add, Search, Delete, Modify, Check, Exit\n").lower()
    if choice=="add":
        record = {
        "name":input("Enter Name"),
        "scores":input("Enter 3 quiz Scores").split(), }
        if len(record["scores"]) !=3:
            print("Input Invalid or not 3 quiz scores"),
            continue
        try:
                q1,q2,q3=map(int,record["scores"])
                record["scores"] = [q1, q2, q3]
                records.append(record)
        except ValueError:
            print("Wrong input please Enter 3 scores or numbers")

    elif choice=="search":
        name=input("Enter Name")
        for A in records:
            if A["name"]==name:
                print(A["name"],A["scores"])
            else:
                print("Not Found")

    elif choice=="delete":
        name=input("Enter Name")
        for A in records:
            if A["name"]==name:
                records.remove(A)
                break
            else:
                print("Not Found")
    elif choice=="modify":
        name=input("Enter Name")
        for A in records:
            if A["name"]==name:
                name=input("Enter Name")
                A["name"]=name
                A["scores"]=input("Enter 3 quiz Scores").split()
                q1, q2, q3 = map(int, A["scores"])
                A["scores"] = [q1, q2, q3]
            else:
                print("Not Found")
    elif choice=="check":
        print(records)
    elif choice=="exit":
        break
    else:
        print("Enter Valid Choice")