str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
dict = {"A" : 4, "B": 3, "C": 2, "D": 1}

score_list = list(map(lambda x: dict[x], str))

total = 0

for score in score_list:
    total += score

print(total)
