# 뒤집힌 덧셈

def rev(X):
    a = int(str(X)[::-1])
    return(a)

X, Y = list(map(int,input().split()))

res = rev(rev(X)+rev(Y))
print(res)