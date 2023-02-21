# 20291 파일 정리

# T = int(input())
# ex_list = []
# for t in range(0, T):
#     name, extension = input().split('.')
#     ex_list.append(extension)
# ex_set = set(ex_list)
# ex_names = list(ex_set)
# sorted_ex_names = sorted(ex_names)
# for name in sorted_ex_names:
#     print(f"{name} {ex_list.count(name)}")
    
T = int(input())
ex_count = {}
for t in range(T):
    name, extension = input().split('.')
    if extension in ex_count:
        ex_count[extension] += 1
    else:
        ex_count[extension] = 1

sorted_ex_names = sorted(ex_count.keys())
for name in sorted_ex_names:
    print(f"{name} {ex_count[name]}")
