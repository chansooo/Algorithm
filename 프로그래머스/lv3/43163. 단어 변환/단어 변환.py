from collections import deque
# 단어가 들어왔을 떄 변환 가능한 단어 배열 return
def next_words(target, words):
    ret = []
    for word in words:
        count = 0
        if word == target:
            continue
        for i in range(len(target)):
            if target[i] != word[i]:
                count += 1
        if count == 1:
            ret.append(word)
    return ret

def solution(begin, target, words):
    count = 0
    if target not in words:
        return 0
    q = deque()
    q.append([begin])
    while q:
        count += 1
        next_word_list = []
        available_words = list(q.popleft())
        for available_word in available_words:
            next_word_list += next_words(available_word, words)
        if target in next_word_list:
            return count
        if len(next_word_list) != 0:
            q.append(next_word_list)
    return 0