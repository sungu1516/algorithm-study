def solution(info, query):
    # 문자열 처리 > 리스트로 만들기
    parsed_info = [x.split() for x in info]
    parsed_query = [x.split() for x in query]
    for q in parsed_query:
        while 'and' in q:
            q.remove('and')
    
    # parsing 된 query 를 순회하며 result 에 결과 더하기
    result = []
    for qry in parsed_query:
        cnt = 0
        # 하나의 query 문으로 모든 info 를 확인한다.
        for inf in parsed_info:
            able = True
            # 모든 항목이 일치하는지 확인한다.
            for i in range(4):
                if qry[i] != inf[i] and qry[i] != '-':
                    able = False
                    break
            # 모든 항목이 일치하고, 점수가 조건에 맞는 경우
            if not able: continue 
            
            if int(qry[4]) <= int(inf[4]):
                cnt += 1
                
        result.append(cnt)

    return result
    