def solution(s):
    # 필요한 자료구조 정의
    open = {'(': 1, '[': 2, '{': 3}
    close = {')': 1, ']': 2, '}': 3}

    # 회전 시 가능한 올바른 문자열 개수
    cnt = 0

    # 올바른 괄호 문자열을 확인하기 위한 함수 정의
    def is_correct(s):
        # 사전 검증 - 만약 닫는 괄호로 시작하거나 여는 괄호로 끝나는 경우
        if s[0] in close or s[-1] in open:
            return False

        stack = []

        for i in range(len(s)):
            # 여는 괄호인 경우 stack에 담기
            if s[i] in open:
                stack.append(s[i])

            # 닫힌 괄호인 경우
            else:
                # 만약 stack이 빈 경우
                if not stack:
                    return False
                else:
                    # 직전에 담긴 괄호와 현재 괄호를 비교
                    if open[stack[-1]] == close[s[i]]:
                        stack.pop()
                    else:
                        return False

        # for문 종료 후
        if not stack:
            return True
        else:
            return False

    # 정해진 길이만큼 회전하며 올바른 문자열인지 확인한다.
    for i in range(len(s)):
        # 올바른 괄호 여부 확인
        if is_correct(s):
            cnt += 1

        # 왼쪽으로 문자열 회전
        s = s[1:] + s[0]

    return cnt


