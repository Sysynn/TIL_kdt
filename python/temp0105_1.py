import random
num = list(range(1, 45, 1))
print(random.sample(num, 6))

students = ['민욱', '홍엽', '현석', '정은']
print(students)
random.shuffle(students)
print(random.shuffle)

today = datetime.date(2023, 1, 5)
print(today)
print(type(today))
print(today.year)
print(today.day)