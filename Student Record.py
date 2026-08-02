print("This is a Student Record System choose below\n")
records = []
try:
    with open("Record.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                name = parts[0]
                scores = list(map(int, parts[1:4]))
                records.append({"name": name, "scores": scores})
except FileNotFoundError:
    pass
while True:
    choice = input("Add, Search, Delete, Modify, Check, Exit\n").lower()
    if choice == "add":
        record = {
            "name": input("Enter Name: "),
            "scores": input("Enter 3 quiz Scores: ").split(),   }
        if len(record["scores"]) != 3:
            print("Input Invalid or not 3 quiz scores")
            continue
        try:
            q1, q2, q3 = map(int, record["scores"])
            record["scores"] = [q1, q2, q3]
            records.append(record)
            with open("Record.txt", "a") as file:
                file.write(f"{record['name']} {q1} {q2} {q3}\n")
        except ValueError:
            print("Wrong input please Enter 3 scores or numbers")
    elif choice == "search":
        name = input("Enter Name: ")
        found = False
        for A in records:
            if A["name"] == name:
                print(A["name"], A["scores"])
                found = True
                break
        if not found:
            print("Not Found")
    elif choice == "delete":
        name = input("Enter Name: ")
        found = False
        for A in records:
            if A["name"] == name:
                records.remove(A)
                found = True
                break
        if found:
            with open("Record.txt", "w") as file:
                for A in records:
                    file.write(f"{A['name']} {A['scores'][0]} {A['scores'][1]} {A['scores'][2]}\n")
        else:
            print("Not Found")
    elif choice == "modify":
        name = input("Enter Name: ")
        found = False
        for A in records:
            if A["name"] == name:
                new_name = input("Enter New Name: ")
                A["name"] = new_name
                new_scores = input("Enter 3 quiz Scores: ").split()
                try:
                    q1, q2, q3 = map(int, new_scores)
                    A["scores"] = [q1, q2, q3]
                    found = True
                except ValueError:
                    print("Wrong input please Enter 3 scores or numbers")
                break
        if found:
            with open("Record.txt", "w") as file:
                for A in records:
                    file.write(f"{A['name']} {A['scores'][0]} {A['scores'][1]} {A['scores'][2]}\n")
        else:
            print("Not Found")
    elif choice == "check":
        print(records)
    elif choice == "exit":
        break
    else:
        print("Enter Valid Choice")