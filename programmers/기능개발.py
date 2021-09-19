from math import ceil

def solution(progresses, speeds):
    # 작업진도, 작업 속도를 이용하여 각 작업 진도 별 잔여 작업 일수 배열 생성
    remains = []
    for i in range(len(progresses)):
        remains.append(ceil((100 - progresses[i]) / speeds[i]))

    # stack 활용하여 각 배포일 별 배포 가능 기능 개수 구하기
    stack = []
    answer = []
    for remain in remains:
        if stack:   # stack 안에 원소가 존재하는 경우
            # stack 안의 top 원소와 비교를 한다.
            # 만약 top 원소보다 다음 숫자가 더 클 경우
            if stack[-1] < remain:
                # stack 의 크기를 계산하여 ans 에 추가해주고
                answer.append(len(stack))
                # stack 을 비운 후 remain 을 저장
                stack = [remain]
            else:
                stack.append(remain)    # 내림차순 or 같은 숫자인 경우는 스택에 누적

        else:   # stack 이 빈 경우
            stack.append(remain)

    if stack:   # 반복문 종료 후 stack 안에 원소가 남아있는 경우
        answer.append(len(stack))

    return answer


print(solution([93, 30, 55], [1, 30, 5]))