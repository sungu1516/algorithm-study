def solution(numbers):
    
    # 첫째 자리 숫자를 뒤에 더해주기 (for 정렬)
    numbers_str = list(map(lambda x: str(x) * 3, numbers))
    
    
    # 정렬
    result = sorted(numbers_str, reverse=True)
    
    # 정렬 결과의 원소들에서 끝 자리만 제거하기
    result = list(map(lambda x: x[:len(x)//3], result))

    
    # join - 0 처리를 위해 int로 형변환 후 다시 str로 형변환
    answer = str(int(''.join(result)))
    
    
    return answer