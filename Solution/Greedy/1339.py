N=int(input())

# 입력할 단어 변수 선언
words = []

# 입력받기
for _ in range(N):
  words.append(input())

# 딕셔너리 초기화
dict = {}


for word in words:
  square_root = len(word) - 1
  for c in word:
    if c in dict: # 값이 있는경우 더해준다.
      dict[c] += pow(10, square_root)
    else: # 없는경우 그대로 넣어준다.
      dict[c] = pow(10, square_root)
    square_root -= 1 

dict = sorted(dict.values(), reverse=True)


result,m = 0,9

# 값 계산
for value in dict:
  result += value * m
  m -= 1

print(result)


# from collections import defaultdict, deque
# N = int(input())
# words = []
# max_len = 0
# match = defaultdict(int)
# stack = [0,1,2,3,4,5,6,7,8,9]
# result = []
# for _ in range(N):
#     a = input()
#     words.append(a)
#     max_len = max(max_len, len(a))

# for i in range(len(words)):
#     while len(words[i]) < max_len:
#         a = deque(words[i])
#         a.appendleft('0')
#         words[i] = ''.join(a)
#         print(words[i])
        
# temp = 0
# for i in range(max_len):
#     temp = temp * 10
#     for word in words:
#         if word[i] == '0':
#             continue
#         if word[i] in match:
#             #result.append(dict[word[i]])
#             temp += int(match[word[i]])
#         # 아직 매치되지 않은 알파벳이라면
#         else: 
#             # 매치시켜주기
#             match[word[i]] = stack.pop()
#             temp += int(match[word[i]])
    
# print(temp)
# # 각 단어의 길이를 받아서 해당 길이에 가장 큰 자릿수에 해당하는 수에 제일 큰 수를 넣자
