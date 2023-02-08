
N, M = list(map(int,input().split()))
scores = list(map(int,input().split()))
sorted_scores = sorted(scores)

print(sorted_scores[N - M])