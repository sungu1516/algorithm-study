import sys
sys.stdin = open("input.txt", "r")
# 필요함수 정의
def get_code(): # N, M 값을 참조하여 암호코드 정보를 입력받고, 암호코드에 해당하는 부분을 리턴
    for row in arrs:
        for i in range(M - 1, -1, -1):  # 코드 한 줄을 탐색하며, 뒤에서부터 1을 찾는다.
            if row[i] == '1':
                return row[i - 55:i + 1]  # 암호코드의 길이는 56칸이므로, 적절한 길이만큼 슬라이싱하여 변수에 저장해둔다.

def get_ans():
    # 홀수자리, 짝수자리 합 구하기
    odd_sum = 0
    even_sum = 0
    for i in range(7):
        if i % 2:  # 짝수 자리
            even_sum += decimal[i]
        else:
            odd_sum += decimal[i]

    # 검증코드 확인
    val_code = decimal[-1]
    if (odd_sum * 3 + even_sum + val_code) % 10 == 0:
        return sum(decimal)
    else:
        return 0

decode = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
          '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9} # 2진수를 10진수로 변환하기 위한 딕셔너리

T = int(input())
for tc in range(1, T + 1):
    # 입력받기
    N, M = map(int, input().split()) # 배열의 세로 크기, 가로크기
    #  암호코드 정보가 표함된 배열을 만든다.
    arrs = [input() for _ in range(N)]
    code = get_code() # 함수를 이용해 필요한 부분만큼 가져옴

    # 2진수 -> 10진수 변환하여 배열에 담기
    decimal = []
    for i in range(0, 56, 7):
        decimal.append(decode.get(code[i:i+7]))

    # 함수 이용해 결과 얻기
    ans = get_ans()

    print('#{} {}'.format(tc, ans))