#9498 시험 성적

number = int(input())

if 0 <= number <= 100:
    if 90 <= number <= 100:
        print("A")
    elif 80 <= number <= 89:
        print("B") 
    elif 70 <= number <= 79:
        print("C")
    elif 60 <= number <= 69:
        print("D")
    else:
        print("F")
        