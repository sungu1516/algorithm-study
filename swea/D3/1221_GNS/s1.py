import sys
sys.stdin = open('input.txt')

T = int(input())

numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(1, T + 1):
    M, N = input().split()
    N = int(N)

    arr = input().split()

    sorted_arr = []

    for i in range(len(numbers)):
        for j in range(len(arr)):
            if numbers[i] == arr[j]:
                sorted_arr.append(arr[j])

    print(M)
    print(*sorted_arr)
