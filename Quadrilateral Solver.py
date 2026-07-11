import math

print("Welcome this is a solver that can calculate a quadrilateral perimeter and semi perimeter as well as area\n")
print("Input exactly 4 numbers otherwise it will throw an error\n")
a,b,c,d=map(float,input("Enter the 4 sides of the quadrilateral\n").split())
if a+b+c<=d or a+b+d<=c or c+b+d<=a or a + c + d <= b:
    print("Not a valid quadrilateral ")
else:
    print("Confirmed quadrilateral, Now computing.....")
    result=a+b+c+d
    sresult=result/2
    print(f"{result:.2f} this is the perimeter\n {sresult:.2f} this is the semi perimeter")
    A, B, C, D = map(int, input("Now in order to compute the area you need to input the 4 angles of the quadrilateral\n").split())
    if sum([A, B, C, D]) ==360:
        print("Valid Quadrilateral, Determining kind.....")
        if A==90 and A==B==C==D and a==b==c==d:
            print("It's a Square")
        elif a==b==c==d and not A==90 and A==B==C==D:
            print("It's a Rhombus")
        elif A == 90 and A == B == C == D and a == c and b == d and A==C and B==D:
            print("It's a rectangle")
        elif A != 90 and  a == c and b == d and A==C and B==D:
            print("It's a parallelogram")
        else:
            print(" a general quadrilateral ")
    else:
        print("Not a valid quadrilateral — angles must sum to 360°")
    sa=sresult-a
    sb = sresult - b
    sc = sresult - c
    sd = sresult - d
    final = math.sqrt(sa * sb * sc * sd)
    print(f"The area of the quadrilateral is {final:.2f} area units\n")


    math.isclose(A, 90, abs_tol=0.5)
    math.isclose(B, 90, abs_tol=0.5)
    math.isclose(C, 90, abs_tol=0.5)
    math.isclose(D, 90, abs_tol=0.5)