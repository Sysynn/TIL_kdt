# 5576 콘테스트

W = []
for w in range(0,10):
    score = int(input())
    W.append(score)

K = []
for k in range(0,10):
    score = int(input())
    K.append(score)

sorted_W = sorted(W)
sorted_K = sorted(K)

top_W = sorted_W[7:10]
top_K = sorted_K[7:10]

print(sum(top_W), sum(top_K))