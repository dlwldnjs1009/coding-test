n = int(input())
coordinate = list(map(int, input().split()))
new_coordinate = sorted(set(coordinate))
dictionary = {new_coordinate[i]: i for i in range(len(new_coordinate))}

for i in coordinate:
    print(dictionary[i], end=' ')


