# 입력값 받기
n = int(input())    # 스위치 개수
status = list(map(int, input().split()))    # 스위치 상태 배열
m = int(input())    # 학생 수
student = [list(map(int, input().split())) for _ in range(m)]   # 학생 성별 & 받은 숫자 배열

# 편리한 숫자 비교를 위해 status 배열 처리
status.insert(0, 9)

# student 배열 순회
for stu in student:
    sex = stu[0]    # 성별
    number = stu[1] # 학생이 받은 숫자

    # 남자인 경우
    if sex == 1:
        for i in range(number, len(status)):
            if i % number == 0:
                # number의 배수인 경우 - 비트연산으로 상태값 변경
                status[i] = status[i] ^ 1
    else:
        # 여자인 경우
        # status[number] 상태값 변경
        status[number] = status[number] ^ 1
        # 대칭 숫자 비교 & 상태값 변경 처리
        left = number - 1   # 대칭 왼쪽 인덱스
        right = number + 1  # 대칭 오른쪽 인덱스
        while left > 0 and right < n + 1 and status[left] == status[right]:
            # 상태값 변경
            status[left] = status[left] ^ 1
            status[right] = status[right] ^ 1
            # 인덱스 대칭 이동
            left -= 1
            right += 1

for i in range(1, len(status)):
    if i % 20 == 0:
        print(status[i], end='\n')
    else:
        print(status[i], end=' ')