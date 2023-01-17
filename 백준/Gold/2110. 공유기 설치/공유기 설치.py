    
    
house_num, share_num = map(int, input().split())
house_location = [int(input()) for _ in range(house_num)]
house_location.sort()

min_ = 1
max_ = house_location[-1]
while min_ <= max_:
    mid = (min_ + max_) // 2
    
    cur = house_location[0]
    count = 1
    
    for i in range(1, len(house_location)):
        if house_location[i] >= cur + mid:
            count += 1
            cur = house_location[i]
    if count >= share_num:
        min_ = mid + 1
    else:
        max_ = mid - 1

print(min_ - 1)