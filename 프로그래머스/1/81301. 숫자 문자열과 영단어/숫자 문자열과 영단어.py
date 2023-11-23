def solution(s):
    english_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    temp = ''
    # 이렇게 temp만들어두고 append해야할 때는 어떤 자료형?
    for i in s:
        if i.isdigit():
            answer += i
        elif i.isalpha():
            temp += i
            if temp in english_list:
                answer += str(english_list.index(temp))
                temp = ''
            
            
    return int(answer)