# 입력값 받기
import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 자료구조 - HashMap
file_map = {}

# 확장자(key), 개수(value) 정보를 map에 추가
for _ in range(n):
    fnm = input().rstrip()
    ext = fnm[fnm.index('.') + 1:]
    file_map[ext] = file_map.get(ext, 0) + 1

# map을 key값으로 오름차순 정렬
file_map = sorted(file_map.items())

for file in file_map:
    print(file[0], file[1])