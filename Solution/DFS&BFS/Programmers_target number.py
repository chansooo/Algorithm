def solution(numbers, target):
    answer = 0
    numbers_len = len(numbers)
    #해당 노드를 뺄건지 더할건지 확인
    def dfs(index, result):
        if numbers_len == index:
            if result == target:
                nonlocal answer
                answer +=1
        else: 
            dfs(index+1, result + numbers[index])
            dfs(index+1, result - numbers[index])
    dfs(0,0)    
    return answer
