def solution(s):
    answer = []
    max_ = len(s)//2
    # s를  1 ~ 문자열 절반 길이 단위로 확인하자
    if len(s) == 1:
        return 1
    for i in range(1, max_+1):
        result = ""
        temp = ''
        block_count = 0 #블록 몇개째인지 확인
        same_count =1 # 같은 문자열 몇개 나왔는지 확인
        while block_count <= len(s):
            # k~k+i를 묶어서 확인하자
            if len(temp) != 0:
                #이전 문자열과 같을 때
                if temp == s[block_count:block_count+i]:
                    same_count += 1
                #이전 문자열과 다를 때 
                else:
                    #temp에 저장된 문자열과 횟수 넣어주기
                    if same_count == 1:
                        result += str(temp)
                    else:
                        result += str(same_count) 
                        result += str(temp)
                    same_count =1
                if block_count + 2*i > len(s):
                    result +=(s[block_count+i:])
            temp = s[block_count:block_count+i]
            block_count += i
        answer.append(result)
    
    return len(min(answer, key = len))