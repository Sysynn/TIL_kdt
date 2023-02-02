# number = int(input())
# num_list = []
# for i in range(0, number):
#     num = int(input())
#     if num == 0:
#         num_list.pop()
#     else:
#         num_list.append(num)

# print(sum(num_list))

#2161 카드1

N = 7
queue = [i for i in range(1, N + 1)]
# queue = list(range(1, N + 1))
discard_cards = []  #버린 카드를 관리할 빈 리스트 생성
# 1장 남을 때 까지 반복 => while
while len(queue) > 1: # 한장 남을 때까지
    #우선, 제일 위에 있는 카드를 바닥에 버린다.
    #queue 에서 제일 위 : pop(0)
    discard_cards.append(queue.pop(0)) # 버리기
    #그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    queue.append(queue.pop(0))
    print(discard_cards, queue)