# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.


# [제약 사항]

# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 풀이
# 입력된 문자열의 마디 길이를 반환하는 함수 정의
def len_madi(strings):
    madi = ''
    # 반복문을 통해 strings[0:x] 와 strings[x:2x] 비교
    for idx, chr in enumerate(strings):
        # 비교하는 같은 길이의 부분 문자열이 동일한 경우
        if strings[0:idx+1] == strings[idx+1:2*(idx+1)]:
            # 기존의 madi 모다 길이가 길고, 문자열의 길이가 10 이하인 경우
            if (len(madi) < len(strings[0:idx+1])) and (len(strings[0:idx+1])<=8):
                madi = strings[0:idx+1]

    # madi 문자열의 길이 리턴
    return len(madi)

# 입력받기
result = ''
number = int(input())
for i in range(number):
    input_strings = input()
    result += f'#{i + 1} {len_madi(input_strings)}' + '\n'

print(result)
