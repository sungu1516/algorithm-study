import sys
sys.stdin = open('input.txt')
T = 10
for _ in range(1, T+1):
    tc = input() # 테스트 케이스의 번호
    data = list(map(int, input().split())) # 암호 데이터
    k = 0 # 연산에 사용될 숫자

    # 첫 번째 요소 빼서 연산 후 뒤에 추가
    while data[-1] > 0:  # 마지막 연산 결과가 0이하면 종료
        rmv = data.pop(0)   # 제거할 첫 번째 데이터
        add = rmv-(k+1)  # 다시 더해줄 데이터 연산
        if add < 0:
            add = 0
        data.append(add)
        k = (k+1) % 5

    print('#{}'.format(tc), *data)
