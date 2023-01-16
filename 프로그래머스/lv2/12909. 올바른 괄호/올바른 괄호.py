from collections import deque
def solution(s):
    answer = True
    s = deque(s)
    stack = []
    
    while s:
        cur = s.popleft()
        if stack and stack[-1] == '(' and cur == ')':
            stack.pop()
        else:
            stack.append(cur)
    

    return False if stack else True