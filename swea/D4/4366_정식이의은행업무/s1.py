import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    bin_num = list(map(int, input()))   # 2진수를 arr 로
    ter_num = list(map(int, input()))   # 3진수를 arr 로

    for i in range(len(bin_num)):
        bin_num[i] = bin_num[i] ^ 1  # 2진수 한 자리를 반전
        # 3진수 숫자를 변환
        for j in range(len(ter_num)):
            tmp = ter_num[j]
            for k in range(3):  # 3진수 한 자리 변환
                if k != tmp:
                    ter_num[j] = k

                bin_to_dec = int(''.join(map(str, bin_num)), base=2)
                ter_to_dec = int(''.join(map(str, ter_num)), base=3)

                if bin_to_dec == ter_to_dec:
                    print('#{} {}'.format(tc, bin_to_dec))  # 만약 한 자리씩 변환한 결과를 모두 확인하여, 동일한 경우가 있다면 10진수로 출력
                    break
            ter_num[j] = tmp  # 3진수 한 자리 원상복구
        bin_num[i] = bin_num[i] ^ 1  # 2진수 한 자리를 원상복구




