text = '.F.F....F'

#['.', 'F', '.', ..., 'F']
list(text)

# 8 * 8
import pprint
matrix = []
for _ in range(8):
    #text = '.F.F....F'
    
    matrix.append(list(text))
pprint.pprint(matrix)

# 1 - 2 list comprehension
matrix = [list(input()) for _ in range(8)]

# 2. 3X3
# line = '1 2 3'
# [1, 2, 3]으로 바꿔야함. 
matrix = [list(map(int, input()) for _ in range(3))]
          
matrix = []



    
