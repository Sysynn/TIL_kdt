# 1269 대칭 차집합


A, B = list(map(int,input().split()))
num_a = list(map(int,input().split()))
num_b = list(map(int,input().split()))
set_a = set(list(num_a))
set_b = set(list(num_b))

ab = set_a - set_b
ba = set_b - set_a

AB = list(ab)
BA = list(ba)

result = len(AB) + len(BA)

print(result)    