#10101 삼각형 외우기

A = int(input())
B = int(input())
C = int(input())

if A == B == C == 60:
    print("Equilateral")
elif A + B + C == 180:
    if A == B or B == C or C == A:
        print("Isosceles")    
    else:
        print("Scalene")
else:
    print("Error")
    