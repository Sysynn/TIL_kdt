#9093   단어 뒤집기

T = int(input())
for _ in range(T):
    sentence = input().split()
    reversed_sentence = [word[::-1] for word in sentence]
    print(" ".join(reversed_sentence))