decimal_num = int(input())
bin_num_reverse = ""
bin_num = ""

while decimal_num:
    bin_num_reverse += str(decimal_num % 2)
    decimal_num //= 2

for i in range(len(bin_num_reverse)-1, -1, -1):
    bin_num += bin_num_reverse[i]

print(int(bin_num))