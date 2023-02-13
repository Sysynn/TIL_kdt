# 1065 한수

# def cal(num):
#     for i in range(len(num)):


# cal(876)
# 36

a = 231
b = []
for i in range(0, len(str(a)) - 1):
    n = int(str(a)[i]) + int(str(a)[i + 1])
    b.append(n)
    
print(b)