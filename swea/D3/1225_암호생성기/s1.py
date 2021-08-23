import sys
sys.stdin = open('input.txt')
T = 10
for _ in range(1, T+1):
    tc = input() # 테스트 케이스의 번호
    data = list(map(int, input().split())) # 암호 데이터

    i = 0 # 암호 연산에 사용될 변수
    while data[-1] > 0: # 만약 0이 되는 경우가 나온다면 반복문 종료
        temp = data.pop(0) - (i+1) # 첫 번째 숫자를 배열에서 꺼내 연산
        if temp < 0: # 만약 연산의 결과가 0보다 작다면
            temp = 0
        data.append(temp) # 연산결과를 다시 배열의 마지막 자리에 넣어준다.
        i = (i + 1) % 5

    print('#{}'.format(tc), *data)