data = input()

n = len(data)
half_n = n // 2
print(half_n)

sum_half_a = sum(map(int, data[:half_n]))
sum_half_b = sum(map(int, data[half_n:]))

if sum_half_a == sum_half_b:
    print("LUCKY")
else:
    print("READY")