import math

def solution(progresses, speeds):
    # 결과값을 담을 배열
    result = []
    
    stack = []
    
    # remains 배열 완성 (배포 가능 날짜를 담는다.)
    remains = []
    for i in range(len(progresses)):
        remain = math.ceil((100 - progresses[i])/speeds[i])
        remains.append(remain)
    
    
    # stack을 이용하여 배포 일자 별 가능 개수 세기
    while remains:
        curr = remains.pop(0)
        
        # stack이 비어있을 때
        if not stack:
            stack.append(curr)
        else:
            if stack[0] >= curr:
                stack.append(curr)
            else:
                # 만약 잔여 일수가 더 많이 남은 경우라면
                # 우선 현재 stack 의 길이를 결과 배열에 누적
                result.append(len(stack))
                
                # stack 최신화
                stack = [curr]
    
    # stack에 남아있는 원소 처리
    result.append(len(stack))
    
    return result