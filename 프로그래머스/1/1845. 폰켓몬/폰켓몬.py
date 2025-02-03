def solution(nums):
    answer = 0;
    pick = len(nums) // 2
    dict = {}

    for num in nums:
        dict[num] = True

    # 사전의 길이가 pick보다 크거나 같으면 그냥 pick 출력
    if len(dict) >= pick:
        answer = pick
    # 사전의 길이가 pick보다 작다면 
    else:
        answer = len(dict)

    return answer;