number = list(map(int, input()))



def min_holhol(n_list):
    count =0
    for n in n_list:
        if n % 2 == 1:
            count += 1 
    
    
    if len(n_list) == 1:
        return count
    elif len(n_list) == 2:
        temp = n_list[0] + n_list[1]     
        temp = list(map(int, str(temp)))
        return count + min_holhol(temp)
    else:
        # 0 <= i < j < len(n_list)
        stack = []
        for i in range(1,len(n_list)):
            for j in range(i+1, len(n_list)):
                a = n_list[:i]
                b = n_list[i:j]
                c = n_list[j:]
                a = int("".join(map(str, a)))
                b = int("".join(map(str, b)))
                c = int("".join(map(str, c)))
                temp = a + b + c
                temp = list(map(int, str(temp)))
                temp_val = min_holhol(temp)
                stack.append(temp_val)
        return min(stack) + count
    
def max_holhol(n_list):
    count =0
    for n in n_list:
        if n % 2 == 1:
            count += 1 
    
    
    if len(n_list) == 1:
        return count
    elif len(n_list) == 2:
        temp = n_list[0] + n_list[1]
        temp = list(map(int, str(temp)))

        return count + max_holhol(temp)
    else:
        # 0 <= i < j < len(n_list)
        stack = []
        for i in range(1,len(n_list)):
            for j in range(i+1, len(n_list)):
                a = n_list[:i]
                b = n_list[i:j]
                c = n_list[j:]
                a = int("".join(map(str, a)))
                b = int("".join(map(str, b)))
                c = int("".join(map(str, c)))
                temp = a + b + c
                temp = list(map(int, str(temp)))
                temp_val = max_holhol(temp)
                stack.append(temp_val)
        return max(stack) + count
         
result1 = min_holhol(number)
result2 = max_holhol(number)
       
print(result1, result2)