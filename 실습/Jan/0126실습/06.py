# 9012 괄호
T = input()
for t in T:
    ps = input()
    pss = list(ps)
    
    for p in ps:
        if '(' in ps:
            if p == ')':
                pss.remove('(')
                pss.remove(p)
    if pss == []:
        print("YES")
    else:
        print("NO")

#미완성