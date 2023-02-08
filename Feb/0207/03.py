# 1063 킹
import string

k, rock, dis = input().split() #킹, 돌, 움직이는 회수를 입력받는다
x = k[0] # 처음 킹의 x 좌표
y = k[1] # 처음 킹의 y 좌표
r_x = rock[0] # 처음 돌의 x 좌표
r_y = rock[1] # 처음 돌의 y 좌표

upper = [i for i in string.ascii_uppercase] # 알파벳 대문자 리스트
x_no = upper.index(x) + 1 # 현재 킹의 x 좌표
y_no = int(y) # 현재 킹의 y 좌표
x_rock = upper.index(r_x) + 1 # 현재 돌의 좌표
y_rock = int(r_y) # 현재 돌의 좌표



for d in range(0, int(dis)):
    move = input()
    if 1 <= x_no <= 8 and 1 <= x_rock <= 8:
        if 1 <= y_no <= 8 and 1 <= y_rock <= 8:
            if "R" in move:
                x_no += 1
                if x_no == x_rock and y_no == y_rock:
                    x_rock += 1
            if "L" in move:
                x_no -= 1
                if x_no == x_rock and y_no == y_rock:
                    x_rock -= 1
            if "T" in move:
                y_no += 1
                if x_no == x_rock and y_no == y_rock:
                    y_rock += 1
            if "B" in move:
                y_no -= 1
                if x_no == x_rock and y_no == y_rock:
                    y_rock -= 1
    print(x_no, y_no)
    print(upper[x_no - 1] + str(y_no))
    print(upper[x_rock - 1] + str(y_rock))



# print(new_K)
# print(r_x + str(r_y))
