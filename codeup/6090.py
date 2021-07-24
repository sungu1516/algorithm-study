# 6090 : [기초-종합] 수 나열하기3

a, m, d, n = map(int, input().split())

# 재귀함수로 해결해보기
def seq(number):
    if number == 1:
        return a
    return seq(number-1) * m + d

print(seq(n))