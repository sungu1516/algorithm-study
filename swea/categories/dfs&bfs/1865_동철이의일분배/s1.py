import sys
sys.stdin = open('input.txt')

def dfs(person, probability):   # person = 직원 번호로, 행 번호를 의미
    global max_probability

    # 가지치기
    if probability <= max_probability:  # 현재 성공 확률에서 더 커질 수 없으므로
        return

    if person == N:   # 마지막 사람이 일 선택 시
        if probability > max_probability:
            max_probability = probability

    for i in range(N):  # 한행씩 내려간다.
        if not solved[i]:   # 아직 해결하지 못한 문제일 경우
            solved[i] = 1
            dfs(person + 1, probability * arr[person][i])
            solved[i] = 0

T = int(input())
for tc in range(1, T+1):
   N = int(input())
   arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]   # 입력받을 때 확률로 변환
   max_probability = 0  # 최대값
   solved = [0] * N    # 해결한 일의 번호를 기록

   dfs(0, 1)    # 시작 행과 초기 확률을 넣어준다.

   print('#{} {:.6f}'.format(tc, max_probability*100))