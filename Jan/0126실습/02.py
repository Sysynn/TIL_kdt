#2720 세탁소 사장 동혁
T = int(input())
changes = [25, 10, 5, 1]

for t in range(T):
    coins = []
    change = int(input())
    for i in changes:
        coin = change // i
        coins.append(coin)
        change = change % i
    print(*coins)