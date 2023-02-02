#10101 삼각형 외우기

A = int(input())
B = int(input())
C = int(input())

if A + B + C != 180:
    print("Error")
elif A == B == C and A + B + C == 180:
    print("Equilateral")
elif A == B or A == C or B == C and A + B + C == 180:
    print("Isosceles")
elif A != B != C and A + B + C == 180:
    print("Scalene")
    