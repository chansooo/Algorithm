
def solution(triangle):
#     answer = 0
#     dp = [0] * (len(triangle) + 1)
    
#     answer = dfs(triangle, 0, 0, dp)
#     print(answer)
    for index, triangle_row in enumerate(triangle):
        triangle_row.append(0)
        new = [0] + triangle_row
        triangle[index] = new
        
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            left, right = 0, 0
            if len(triangle[i-1]) > j - 1:
                left = triangle[i-1][j-1]
            if len(triangle[i-1]) > j:
                right = triangle[i-1][j]
            triangle[i][j] += max(left, right)

    return max(triangle[len(triangle)-1])