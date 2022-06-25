
score = input()
score_len = len(score)
left_score = []
right_score = []
for i in range(score_len//2):
    left_score.append(score[i])
    temp = score_len//2
    right_score.append(score[temp + i])

left_sum =0
right_sum =0
for i in range(score_len//2):
    left_sum += int(left_score[i])
    right_sum += int(right_score[i])
    
# print(left_sum)
# print(right_sum)

if left_sum == right_sum:
    print("LUCKY")
else: 
    print("READY")