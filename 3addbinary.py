a = "1"
b = "101"

num_a = int(a, 2)
num_b = int(b, 2)

sum_num = num_a + num_b
result = bin(sum_num)[2:]

print(result)