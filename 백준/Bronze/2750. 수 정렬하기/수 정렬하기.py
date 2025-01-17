n = int(input())
array=[]
for i in range(n):
    array.append(int(input()))
array.sort()
for char in array:
    print(char)