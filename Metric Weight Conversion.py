print("This is a Weight Conversion from Imperial to Metric Weight.")
print("Which converts Imperial Weights to Metric Weights \n")
print("Type Exit to Exit")
print("Lbs to Kg, oz to grams, Stones to Kg, Ton to Kg")
while True:
    a=input("What are you Trying to Convert?\n").lower().strip()
    if a in ("pound", "pounds"):
        b=int(input("Input the pounds\n"))
        c= b*0.45359237
        print(f"{c:.2f} Kg\n")
    elif a in ("ounce","ounces"):
        b=int(input("Input the ounces\n"))
        c= b*28.3495
        print(f"{c:.2f} grams\n")
    elif a == ("stones","stone"):
        b=int(input("Input the Stones\n"))
        c= b*6.35029
        print(f"{c:.2f} Kg\n")
    elif a == ("tons","ton"):
        b=int(input("Input the Tons\n"))
        c= b*907.185
        print(f"{c:.2f} Kg\n")
    elif a == "exit":
        print("Thank you for using the converter!")
        break
    else:
        print("Invalid Input try again\n")
