def solution(today, terms, privacies):
    answer = []

    # terms to dict
    terms_dict = {}
    for term in terms:
        term_pair = term.split()
        terms_dict[term_pair[0]] = int(term_pair[1]) * 28

    # 날짜 표준화
    # 1. today 표준화
    to_year, to_month, to_date = map(int, today.split('.'))
    today_std = to_year * 12 * 28 + to_month * 28 + to_date

    # 2. 각 개인정보 파기일자 표준화
    idx = 1
    for privacy in privacies:
        # 2-1. 각 개인정보별 파기일자 구하기
        indi_day, indi_term = privacy.split()
        indi_year, indi_month, indi_date = map(int, indi_day.split('.'))
        expire_std = indi_year * 12 * 28 + indi_month * 28 + indi_date + terms_dict[indi_term]

        # 2-2. 파기일자와 현재 날짜 비교하기
        if (today_std >= expire_std):
            answer.append(idx)
        idx += 1

    return answer