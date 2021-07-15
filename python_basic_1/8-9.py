a, b = input().split(",")
a, b = a.strip(), b.strip()

def get_long(str1, str2):
    if len(str1) > len(str2):
        return str1
    else:
        return str2

long_str = get_long(a, b)
print(long_str)