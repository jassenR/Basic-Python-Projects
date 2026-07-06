

while True:
    print("Press 1 for Addition , 2 for Subtraction, 3 for Multiplication, 4 for Division, 5 for Exit")
    Operation = int(input())
    if Operation == 1:
        a=int(input("Enter number: "))
        b=int(input("Enter another number: "))
        c=a+b
        print(c)
    if Operation == 2:
        a=int(input("Enter number: "))
        b=int(input("Enter another number: "))
        c=a-b
        print(c)
    if Operation == 3:
        a=int(input("Enter number: "))
        b=int(input("Enter another number: "))
        c=a*b
        print(c)
    if Operation == 4:
        a=int(input("Enter number: "))
        b=int(input("Enter another number: "))
        c=a/b
        print(c)
    if Operation == 5:
        break