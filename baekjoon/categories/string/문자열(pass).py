# 입력값
a, b = input().split()

# 두 문자열의 차이를 구하는 함수
# def get_diff(str1, str2):
#     cnt = 0
#     for i in range(len(str1)):
#         if str1[i] != str2[i]:
#             cnt += 1
#
#     return cnt

# main
a_len = len(a)
b_len = len(b)
min_val = b_len # 최소값 초기화

# 인덱스를 증가시키며 문자열 비교
for i in range(b_len - a_len + 1):
    val = 0
    for j in range(a_len):
        if a[j] != b[j+i]:
            val += 1

    if val < min_val:
        min_val = val

print(min_val)