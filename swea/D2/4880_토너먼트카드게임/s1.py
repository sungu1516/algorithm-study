import sys
sys.stdin = open('input.txt', "r")

# 가위바위보 함수 정의 - 학생의 번호를 받아, 이긴 학생의 번호를 리턴
def fight(a, b):
    if cards[a][1] - cards[b][1] == -2 or cards[a][1] - cards[b][1] == 1:
        return a
    elif cards[a][1] == cards[b][1]: # 만약 두 카드가 동일하다면
        return a if a < b else b # 번호가 낮은 학생의 번호를 리턴
    else:
        return b

# 재귀함수 정의
def grouping(group):
    if len(group) == 1: # 부전승
        return group[0][0]

    elif len(group) == 2:
        return fight(group[0][0], group[1][0]) # 해당 숫자 카드를 가진 학생번호를 넣어준다.

    else: # 만약 길이가 3 이상이라면
        if len(group) % 2: # 홀수일 경우
            group1 = group[:len(group) // 2 + 1]
            group2 = group[len(group) // 2 + 1:]
        else: # 짝수일 경우
            group1 = group[:len(group) // 2]
            group2 = group[len(group) // 2:]

        return fight(grouping(group1), grouping(group2)) # 두 그룹으로 나눈 후, 재귀함수 호출(종료조건에 닿을 때까지 반복)

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 인원수
    cards = list(enumerate(list(map(int, input().split())))) # (인덱스, 카드번호) 가 저장된 배열
    print('#{} {}'.format(tc, grouping(cards) + 1))
