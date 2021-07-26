# 1. 숫자의 의미

def get_secret_word(num_list):
    result = ''
    for num in num_list:
        result += chr(num)
    return result

print(get_secret_word([83, 115, 65, 102, 89]))