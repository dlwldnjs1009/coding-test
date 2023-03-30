data = list(input())
data.sort()
result = []
sum = 0
for i in data:
    if i.isalpha():
        result.append(i)
    else:
        sum += int(i)
if sum != 0:
    result.append(str(sum))
a = ''.join(result)
print(a)