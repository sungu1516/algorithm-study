def get_div_cnt(number):
    share = number // 2
    div_cnt = 0
    for i in range(1, share + 1):
        if number % i == 0:
            div_cnt += 1

    return div_cnt + 1


def solution(left, right):
    answer = 0

    # for: left to right
    for integer in range(left, right + 1):
        # integer 의 약수의 개수 구하기
        cnt = get_div_cnt(integer)

        # cnt 홀짝 판단
        if cnt % 2 == 0:
            answer += integer
        else:
            answer -= integer

    return answer
