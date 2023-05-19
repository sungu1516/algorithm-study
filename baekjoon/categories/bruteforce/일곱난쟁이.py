# 입력값 받기
heightArr = [int(input()) for _ in range(9)]

# 함수 정의
def getAns(inputArr):
    for i in range(len(inputArr) - 1):
        for j in range(i + 1, len(inputArr)):
            if sum(inputArr) - inputArr[i] - inputArr[j] == 100:
                return i, j

# main
# 정렬
heightArr.sort()
idx1, idx2 = getAns(heightArr)

for i in range(len(heightArr)):
    if i == idx1 or i == idx2:
        continue
    print(heightArr[i])

