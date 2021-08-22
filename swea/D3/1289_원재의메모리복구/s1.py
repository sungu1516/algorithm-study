import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    bin_nums = input()
    stack = ['0']
    cnt = 0

    for bin_num in bin_nums:  # 스택에 쌓아가며 각 자리수를 비교
        if stack.pop() != bin_num:
            cnt += 1
        stack.append(bin_num)

    print('#{} {}'.format(tc, cnt))
