import math

# global
def solution(fees, records):

    # 시간 계산 함수 - 문자열 그대로 넣으면 됨
    def cal_time(time_in, time_out):
        time_in_hour, time_in_minute = map(int, time_in.split(':'))
        time_out_hour, time_out_minute = map(int, time_out.split(':'))

        minute_diff = time_out_minute - time_in_minute  # 분 차
        if minute_diff < 0:
            time_out_hour -= 1
            minute_diff += 60

        hour_diff = time_out_hour - time_in_hour
        return hour_diff * 60 + minute_diff

    # records 를 읽어 입출차량 관리하는 함수
    def decode(record):

        time, id, command = record.split()
        # 입차의 경우
        if command == 'IN':
            parking_lot[id] = time

        # 출차
        else:
            if id not in fees_dict:
                fees_dict[id] = cal_time(parking_lot[id], time)
            else:
                fees_dict[id] += cal_time(parking_lot[id], time)
            # 시간 계산이 끝나면 parking lot 에서 차량 제거
            del parking_lot[id]


    def cal_fee(minute):    # 총 주차 시간을 넣으면, 주차 요금을 리턴
        default_time = fees[0]
        default_fee = fees[1]
        unit_time = fees[2]
        unit_fee = fees[3]

        if minute <= default_time:
            return default_fee
        else:
            return default_fee + math.ceil((minute - default_time)/unit_time) * unit_fee


    parking_lot = {}  # 입차한 차량의 목록이 들어있는 딕셔너리. key = 차량번호, value = 입차 시간
    fees_dict = {}  # 차량의 총 주자시간이 누적되는 딕셔너리. key = 차량번호, value = 누적 시간(분)

    for r in records:
        decode(r)

    if parking_lot:  # 남아있는 차량이 있다면, 출차처리 후 시간 계산
        for id in parking_lot:
            if id not in fees_dict:
                fees_dict[id] = cal_time(parking_lot[id], "23:59")
            else:
                fees_dict[id] += cal_time(parking_lot[id], "23:59")

    fees_dict = sorted(fees_dict.items())
    ans = []
    for a_tuple in fees_dict:
        ans.append(cal_fee(a_tuple[1]))
    return ans

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

