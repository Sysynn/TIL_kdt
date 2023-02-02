# 유학 금지

word = input()

no_word = "CAMBRIDGE"
new_word = []

for x in word:
    if x not in no_word:
        new_word.append(x)

print("".join(new_word))