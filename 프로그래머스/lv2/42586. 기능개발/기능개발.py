from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = [[ceil((100 - progresses[0]) / speeds[0]), 0]]
    
    for progress, speed in zip(progresses, speeds):
        duration = ceil((100 - progress) / speed)
        if answer[-1][0] < duration:
            answer.append([duration, 0])
        answer[-1][1] += 1
    return [count for _, count in answer]