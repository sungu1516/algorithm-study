def solution(phone_book):
    '''
    Review
    문제를 잘못이해했다.. 접두가 일치하는 경우에 대해서만 고려해야 하는데, 위치를 고려하지 않고 풀었다.
    처음엔 이중 for문으로 구현했더니, 정확성은 통과했지만 효율성 중 2개의 케이스를 통과하지 못했다.
    '''
    
    '''
    Approach
    우선 배열을 숫자의 길이를 기준으로 정렬한다.
    이후, 앞의 숫자부터 차례대로 비교하며 접두어인 경우를 확인한다.
    길이를 기준으로 짧은 숫자들이 앞에 위치하게 되므로, 뒤에 있는 숫자들에 대해서만 비교하면 된다.
    '''
    
    phone_book = sorted(phone_book)
    answer = True
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    
    return answer