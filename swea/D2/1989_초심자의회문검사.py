# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.


# [제약 사항]

# 각 단어의 길이는 3 이상 10 이하이다.


## 풀이 

# 필요한 함수 정의
def is_palindrome(word):
    if len(word) < 2:
        # 종료조건 설정
        return 1
    else:
        if word[0] == word[-1]:
            # 만약 문자의 양 끝이 같다면 재귀함수 호출 (입력값 주의)
            return is_palindrome(word[1:-1])
        else:
            # 한 번이라도 틀린 경우가 나온다면
            return 0

# 입력값 받기
cnt = int(input())

for i in range(cnt):
    word = input()

    print(f'#{i+1} {is_palindrome(word)}')