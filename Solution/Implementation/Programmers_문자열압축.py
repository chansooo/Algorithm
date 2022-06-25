def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2+1): # 1부터 길이최대까지 압축 시뮬레이션 진행
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼 잘라서 저장
        count =1        
        # step만큼 증가시키면서 이전 문자열과 비교
        for j in range(step, len(s), step):
            #이전과 동일하면 count증가
            if prev == s[j:j+step]:
                count += 1
            #동일하지 않을 경우
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count =1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer