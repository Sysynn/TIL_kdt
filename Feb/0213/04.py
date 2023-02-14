# 1302 베스트셀러

N = int(input())
title_dic = {}
for i in range(0, N):
    title = input()
    if title not in title_dic:
        title_dic[title] = 1
    else:
        title_dic[title] += 1

max_value = max(title_dic.values())
titles = [k for k, v in title_dic.items() if v == max_value]
titles.sort()
print(titles[0])