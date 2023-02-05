number1 = int(input('첫 번째 정수를 입력하세요 >'))
number2 = int(input('두 번째 정수를 입력하세요 >'))

if number1 < number2:
    for element in range(number1 + 1, number2):
        print(element)

elif number1 > number2:
    for element in range(number2 + 1, number1):
        print(element)

else:
    print(False)