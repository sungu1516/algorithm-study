# test case 횟수 입력
cnt = int(input())

for _ in range(cnt):
    number = int(input())

    # 특정 n값을 넣으면, 파스칼 삼각형의 n번째 줄을 리스트 형태로 반환하는 재귀함수 정의
    def pascal_triangle_line(n):
        if n < 3:
            # n의 값이 2 이하라면, [1] * n 을 리턴
            return [1] * n
        else:
            # n의 값이 3 이상이라면
            # 결과 리스트에 1을 담아 초기화
            result = [1]
            # n-1을 인자로 넣어 함수를 재호출 (즉, 변수엔 n-1번 줄의 숫자들을 담은 리스트가 담긴다.)
            prior_triangle_line = pascal_triangle_line(n-1)

            # 반복문을 활용하여, 이전 리스트의 값을 두 개씩 묶어 차례대로 더해 결과 리스트에 추가하고, 마지막 값을 1로 추가한다.
            for idx, elem in enumerate(prior_triangle_line):
                if idx < len(prior_triangle_line) - 1:
                    result.append(elem + prior_triangle_line[idx + 1])
                else:
                    # 인덱스가 마지막에 도달 시
                    result.append(1)
            
            return result

            # 위의 반복문은 아래의 list comprehesion 으로도 가능
            # return [1] + [(val + prior_triangle[idx+1] if idx < len(prior_triangle) -1 else 1) for idx, val in enumerate(prior_triangle)]

    # test case 의 번호 출력
    print(f'#{_ + 1}')
    # pascal triangle 출력
    for i in range(1, number + 1):
        print(*pascal_triangle_line(i))