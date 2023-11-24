def solution(cap, n, deliveries, pickups):
    move_count = 0

    deliver_pointer = n - 1
    pickup_pointer = n - 1
    
    while deliver_pointer >= 0 or pickup_pointer >= 0:
        deliver_cap = 0
        pickup_cap = 0
        cost = 0

        # 배달 포인터 업데이트
        while deliver_pointer >= 0 and deliveries[deliver_pointer] == 0:
            deliver_pointer -= 1

        # 픽업 포인터 업데이트
        while pickup_pointer >= 0 and pickups[pickup_pointer] == 0:
            pickup_pointer -= 1

        if deliver_pointer >= 0 or pickup_pointer >= 0:
            cost = (max(deliver_pointer, pickup_pointer) + 1) * 2
            move_count += cost

        # 배달 처리
        while deliver_cap < cap and deliver_pointer >= 0:
            if deliveries[deliver_pointer] + deliver_cap <= cap:
                deliver_cap += deliveries[deliver_pointer]
                deliveries[deliver_pointer] = 0
                deliver_pointer -= 1
            else:
                remaining = cap - deliver_cap
                deliveries[deliver_pointer] -= remaining
                deliver_cap += remaining

        # 픽업 처리
        while pickup_cap < cap and pickup_pointer >= 0:
            if pickups[pickup_pointer] + pickup_cap <= cap:
                pickup_cap += pickups[pickup_pointer]
                pickups[pickup_pointer] = 0
                pickup_pointer -= 1
            else:
                remaining = cap - pickup_cap
                pickups[pickup_pointer] -= remaining
                pickup_cap += remaining

    return move_count

# # 테스트
# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))  # 16
# print(solution(5, 5, [2, 0, 1, 0, 0],
