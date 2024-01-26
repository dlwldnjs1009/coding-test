def solution(enroll, referral, seller, amount):
    profit_dict = {name: 0 for name in enroll}
    referral_dict = dict(zip(enroll, referral))

    for s, amt in zip(seller, amount):
        profit = amt * 100
        current = s

        while current != "-":
            # 10% 계산 (1원 미만 절사)
            profit_to_parent = profit // 10
            if profit_to_parent < 1:
                profit_dict[current] += profit
                break

            profit_dict[current] += profit - profit_to_parent
            profit = profit_to_parent
            current = referral_dict[current]

    answer = [profit_dict[name] for name in enroll]
    return answer
