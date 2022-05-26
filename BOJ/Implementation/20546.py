cash = int(input())
stock_price = list(map(int, input().split()))

jun = [0, cash]
sung = [0, cash]
# 준현
for i in range(14):
    stock_count = cash // stock_price[i]
    if stock_count > 0:
     jun[0] += stock_count
     jun[1] -= (stock_count*stock_price[i])
    else:
        continue

#  성민
for i in range(3, 14):
    #떨어질 때
    if stock< stock_price[i-1] < stock_price[i-2] and stock_price[i] < stock_price[i-1]:
        stock_count = cash // stock_price[i]
        if stock_count > 0:
            sung[0] += stock_count
            sung[1] -= (stock_count*stock_price[i])
        else:
            continue
    elif stock_price[i-1] > stock_price[i-2] and stock_price[i] > stock_price[i-1]:
        sung[1] += (sung[0] * stock_price[i])
        sung[0] = 0


jun[1] = jun[1] + jun[0]*stock_price[13]
sung[1] = sung[1] + sung[0] * stock_price[13]

if jun[1] < sung[1]:
    print("TIMING")
elif jun[1] > sung[1]:
    print("BNP")
else:
    print("SAMESAME")