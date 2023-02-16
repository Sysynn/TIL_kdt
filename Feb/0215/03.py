# 1259 팰린드롬수

while True:
    S = int(input())
    if S == 0:
        break
    else:
        leng = len(str(S))
        if leng % 2 == 0:
            a = str(S)[0:leng//2]
            b = str(S)[leng:leng//2-1:-1]
            if a == b:
                print("yes")
            else:
                print("no")
        else:
            c = leng // 2 + 1
            d = str(S)[0:c-1]
            e = str(S)[leng:c-1:-1]
            if d == e:
                print("yes")
            else:
                print("no")


