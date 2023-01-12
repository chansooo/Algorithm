def solution(N, number):
    if N == number:
        return 1
    
    set_list = []
    
    for count in range(1, 9):
        partial_set = {int(str(N) * count)}
        for i in range(len(set_list)):
            set1 = set_list[i]
            set2 = set_list[-i-1]
            for num1 in set1:
                for num2 in set2:
                    partial_set.add(num1 - num2)
                    partial_set.add(num2 - num1)
                    partial_set.add(num1 * num2)
                    partial_set.add(num1 + num2)
                    if num2 != 0:
                        partial_set.add(num1 // num2) 
                    if num1 != 0:
                        partial_set.add(num2 // num1)
        if number in partial_set:
            return count
        set_list.append(partial_set)
    return -1