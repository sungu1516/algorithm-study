def solution(record):
    # 1. record 순회하며 hash에 최신 닉네임을 저장하는 함수
    def set_name(sentence):
        # 만약 방을 나가는 경우가 아니라면
        if sentence[0] != 'Leave':
            hash[sentence[1]] = sentence[2]

    # 2. 출력 결과를 담아 리턴하는 함수
    def get_result(sentences):
        result = []
        for sentence in sentences:
            if sentence[0] == 'Enter':
                content = hash[sentence[1]] + "님이 들어왔습니다."
                result.append(content)

            elif sentence[0] == 'Leave':
                content = hash[sentence[1]] + "님이 나갔습니다."
                result.append(content)

        return result

    # 2차원 배열로 변환
    record = [list(elem.split()) for elem in record]

    # 아이디 - 닉네임 (최종)
    hash = dict()

    # 닉네임 업데이트
    for a_record in record:
        set_name(a_record)

    return get_result(record)