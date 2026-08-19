def addition (a,b):
    return a+b
def subtraction (a,b):
    return a-b
def multiplication (a,b):
    return a*b
def division (a,b):
    return a/b
def operator(a,b,):
    c = int(input("Enter your operator"))
    if c == 1:
        result = addition(a,b)
    elif c == 2:
        result = subtraction(a, b)
    elif c == 3:
        result = multiplication(a, b)
    elif c == 4:
        result = division(a, b)
    return result
def main ():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = operator(a,b)
    print(result)
if __name__ == "__main__":
    main()