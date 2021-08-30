import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())        # 수강생의 수 N, 과제를 제출한 사람의 수 K
    students = list(map(int, input().split()))      # 과제를 제출한 수강생들의 번호

    submit = [0] * (N+1)        # 수강생의 번호를 인덱스로, 제출 여부를 값으로 갖는 배열

    # 과제를 제출한 수강생들을 표시해준다.
    for student in students:
        submit[student] = 1

    # 미제출자들의 번호를 오름차순으로 출력
    print('#{}'.format(tc), end = ' ')
    for i in range(1, N+1):
        if not submit[i]:
            print(i, end=' ')
    print()