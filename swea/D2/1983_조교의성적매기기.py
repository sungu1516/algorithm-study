# test case 수 입력받기
cnt = int(input())

for i in range(cnt):
    # 학생 수, 번호, 점수를 입력받아서 총점 계산 후 리스트 저장
    n, k = map(int, input().split())

    # 정렬하기 전의 학생들의 총 점수를 담은 리스트
    before_sorted = []

    for _ in range(n):
        scores = map(int, input().split())
        # lambda 함수를 이용하여 총점 계산 후 변수에 저장
        # map 객체의 요소들을 인자로 넣기 위해 * (unpack) 이용
        final_score = (lambda x, y, z: x*0.35 + y*0.45 + z*0.2)(*scores)
        before_sorted.append(final_score)

    # 정렬하기 전 k번째 학생의 총점을 저장해둔다.
    k_final_score = before_sorted[k-1]

    # 학생들의 총점이 담겨있는 리스트를 정렬
    after_sorted = sorted(before_sorted, reverse=True)

    # 위에서 입력받은 학생 수(n)를 이용하여 총점을 딕셔너리 안에 넣기
    # 정렬한 총점들을 학생 수에 따른 기준에 맞게 딕셔너리에 넣어주기
    point = n // 10

    grades = {
        'A+': after_sorted[:point],
        'A0': after_sorted[point:2*point],
        'A-': after_sorted[2*point:3*point],
        'B+': after_sorted[3*point:4*point],
        'B0': after_sorted[4*point:5*point],
        'B-': after_sorted[5*point:6*point],
        'C+': after_sorted[6*point:7*point],
        'C0': after_sorted[7*point:8*point],
        'C-': after_sorted[8*point:9*point],
        'D0': after_sorted[9*point:]
    }

    for grade in grades:
        if k_final_score in grades[grade]:
            print(f'#{i+1} {grade}')