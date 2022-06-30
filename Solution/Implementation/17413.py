# from collections import deque


# S = input()
# length = len(S)
# flag = False
# result = deque()
# temp = deque()
# for i in range(length):
#     temp.append(S[i])
#     if S[i] == '<':
#         flag = True
#         continue
#     if S[i] == '>':
#         flag = False
#         result.append(temp)
#         temp.clear()
#         continue
#     if flag == False and S[i] == ' ':
#         temp.pop()
#         for _ in range(len(temp)):
#             result.append(temp.pop())
#         result.append(' ')  
        
# [::-1]
# print(*result)


def solution():
    answer = []
    str = input()

    temp = []
    not_temp = []
    flag = False

    print(str.split("<"))

    # for s in range(len(str)-1):
    #     if str[s] == "<":
    #         flag = True
            
    #     elif str[s] == ">":
    #         flag = False
            
    #     if flag == True:
    #         temp.append(str[s+1])
    #     else:
    #         pass
        
        
    #     if str[s] == ">":
    #         not_temp.append(str[s+1])
            
    
    # temp = "".join(temp)
    # print(temp.split(">"))
    
    
    # for s in str:
    #     if s[0] == '<':
    #         answer.append(s)
    #     else:
    #         answer.append(s[::-1])
    
    # print(answer)

solution()
    
