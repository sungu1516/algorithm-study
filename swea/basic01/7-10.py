# 빈도수 저장 리스트 만들기
frequency = [0]*10

# 입력숫자의 자리수별 저장 리스트 만들기
list = []
num = int(input())

while num:
    list.append(num % 10)
    num //= 10

for i in list:
    frequency[i] += 1

# 결과 출력
result = ""
for i in range(0, 10):
   result += str(i) + " "
print(result[0:len(result)-1])
result = ""
for fre in frequency:
    result += str(fre) + " "
print(result[0:len(result) - 1])