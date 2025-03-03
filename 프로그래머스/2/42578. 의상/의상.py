def solution(clothes):
    
    closet = {}
    for n, k in clothes:
        if k in closet.keys():
            closet[k] += [n]
        else:
            closet[k] = [n]
    
    answer = 1
    for _, value in closet.items():
        answer *= (len(value) + 1)
        

    return (answer -1)