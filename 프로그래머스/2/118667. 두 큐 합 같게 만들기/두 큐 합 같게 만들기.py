from collections import deque

def solution(queue1, queue2):
    # queue1 = [1]
    # queue2 = [3]
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    target = (sum(queue1) + sum(queue2)) // 2
    max_loop = len(queue1)* 3
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    loop_count = 0
    
    q1_sum = sum(queue1)
    
    while q1_sum != target:
        loop_count += 1
        # print(queue1)
        # print(queue2)
        # print()
        if loop_count >= max_loop:
            return -1
        # 넘칠 때는 pop
        if q1_sum > target:
            num = queue1.popleft()
            queue2.append(num)
            q1_sum -= num
        else:
            num = queue2.popleft()
            queue1.append(num)
            q1_sum += num
    
    return loop_count