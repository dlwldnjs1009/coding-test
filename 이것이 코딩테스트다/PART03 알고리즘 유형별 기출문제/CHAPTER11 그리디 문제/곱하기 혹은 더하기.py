b=input()
array=[]
for i in b:
    array.append(i)

result = 1

for i in array:
    if int(i) == 0:
        continue
    result *= int(i)

print(result)

# 저자의 코드
# data = input()
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= i or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)
