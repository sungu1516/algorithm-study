import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 화덕의 크기, 피자의 개수
    all_pizza = list(map(int, input().split())) # 모든 피자의 치즈양  가 담긴 배열
    que = []  # 화덕으로 쓸 que 만들기 - 원형큐 활용

    # pizza 마다 번호를 붙이자
    numbered_pizza = [] # 피자마다 번호를 붙여 넣을 배열
    idx = 1
    for pizza in all_pizza:
        inner = [idx, pizza]
        numbered_pizza.append(inner)
        idx += 1

    # 화덕에 피자 넣어주기 - 일단 화덕 크기만큼만 넣자
    for _ in range(N):
        que.append(numbered_pizza.pop(0))

    # # 피자 돌려가며 확인 후 치즈가 덜 녹았다면 다시 넣어주고, 녹았다면 뺴주고 새로운 피자 추가
    while len(que) > 1: # 화덕에 피자 하나가 남을 때까지
        t = que.pop(0) # 피자하나를 꺼내 확인한다.
        t[1] //= 2 # 녹은 치즈

        if t[1] == 0: # 만약 치즈가 다 녹았다면
            if numbered_pizza: # 남은 피자가 있다면
                que.append(numbered_pizza.pop(0)) # que 에 넣기
        # 치즈가 남은 경우
        else:
            que.append(t) # 녹은 치즈를 반영하여 다시 que 에 넣어준다.

    ans = que[0][0]    # 피자번호

    print('#{} {}'.format(tc, ans))

