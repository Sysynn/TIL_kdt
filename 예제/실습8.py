first = input("첫 번째 숫자를 입력해주세요 > ")
second = input("두 번째 숫자를 입력해주세요 > ")
third = input("세 번째 숫자를 입력해주세요 > ")
forth = input("네 번째 숫자를 입력해주세요 > ")
fifth = input("다섯 번째 숫자를 입력해주세요 > ")
list_variable = []
list_variable.append(int(first))
list_variable.extend([int(second), int(third), int(forth), int(fifth)])
print(list_variable)
