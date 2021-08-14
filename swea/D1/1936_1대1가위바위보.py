A, B = map(int, input().split())
A += 1

if (A - B) % 3:
    result = 'A'
else:
    result = 'B'

print(result)