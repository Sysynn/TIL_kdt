#2754 학점 계산

score = input()
list = ["D", "C", "B", "A"]

if score[0] == 'F':
    print(0.0)
else:
    result = list.index(score[0]) + 1
    if score[1] == "+":
        result += 0.3
    elif score[1] == "-":
        result -= 0.3
    print("{:.1f}".format(float(result)))
    

# # 딕셔너리 

# grade_dict = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}

# score = input()
# if score not in grade_dict:
#     print("Invalid score")
# else:
#     result = grade_dict[score]
#     print("{:.1f}".format(result))