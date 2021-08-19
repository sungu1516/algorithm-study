import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 필요함수 정의 - 재귀함수 활용
def pascal(n):
    if n < 2: # 종료 조건
        return [1] * n
    else:
        result = []
        prior = pascal(n-1) # 이전 줄의 내용을 저장
        for i in range(0, len(prior) - 1):
            result.append(prior[i] + prior[i+1]) # 모든 요소를 돌며 더해주고, 결과를 result 에 담는다.
        return [1] + result + [1]

T = int(input())

for _ in range(1, T + 1):
    N = int(input()) + 1
    
    # 출력
    print('#{}'.format(_), end='')
    for i in range(N):
        print(*pascal(i))
