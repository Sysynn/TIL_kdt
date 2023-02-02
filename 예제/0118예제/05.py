#2941 크로아티아 알파벳



word = input()
cro_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
new_word = []
for i in cro_word:
    if i in word:
        word = word.replace(i, "X")
new_word.append(word)    
        
print(len(*new_word))






