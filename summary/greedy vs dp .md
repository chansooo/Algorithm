# greedy vs dp

## Greedy Algorithm은 왜 중요할까?

1. 자연스럽고, 간단하고, 빠르고 쉬운 구현을 할 수 있는 방법이다.
    1. 경험(heuristric)에 기반한 방법
2. Test-bed: 여러 실험들을 기본으로.
    1. baseline performance를 제공. (기준점 제공)
    2. 연구자들이 가장 먼저 접근하는 설계 전략
    3. 정밀도/정확도 향상, 속도 증가, model size 감소
3. May be “optimal”: optimal substructure이 만족할 때
    1. local optimal → global optimal: proof required

# Knapsack Problem

- example 1.
    - 도둑이 가방(sack)을 가지고 보석방을 감
    - 보석의 무게, 가치가 다름
    - 보석의 일부만 담을 수 있을 때(constraint) 가장 많이 들고갈 수 있는 상황은?
- example 2.
    - 투자가: 사업 아이템들이 있고, 전체 투자금 제한(constraint)
    - 아이템: 사업 주제, 필요 자금, 수익
    - 일부에만 투자할 수 있을 떄 가장 많이 들고갈 수 있는 상황은?
    

Definition: Constrained optimization problem

```c
S = {item_1, item_2, ... , item_n} //문제 구성 요소, object

w_i = {weight_1, weight_2, ... , weight_n}

p_i = {profit_1, profit_2, ... , profit_n}

W = sack size
```

⇒ Find A(a subset of S) //아이템의 일부 조합을 찾는다

제약

1. maximizes the profits in A
2. sum of the weight in A ≤ W

Q: Solve the KS

A: 

1. BF: $2^n$ enumeration → EXP time complexity
2. D&C: optimal ckwdmf tn dlTsmsrk? 
3. DP
4. Greedy

## Greedy

→ 언제 Greedy는 optimal solution 을 제공하는가?

→ idea2는 0/1 KS → Fractional KS로 변경되면 optimal

→ Fractional: 남은 sack에 item을 나누어서 일부분을 담을 수 있다

```jsx
//idea 1
// Greedy: largest profit first
(w1 w2 w3) = (25kg, 10kg, 10kg)
(p1 p2 p3) = ($10, $9, $9)
W = 30kg

-> A = {item_1) 현재무게: 25->35 
=> 불가능
```

```jsx
//idea 2
// Greedy: largest profit per Unit weight first
(w1 w2 w3) = (5kg, 10kg, 20kg)
(p1 p2 p3) = ($50, $60, $140)
W = 30kg

--> p/w = ($10, $6, $7)
--> A = {item_1, item_3} total_profit = 50+140 = 190
--> optimal A = {i2, i3} 
```

## DP

### DP key point

- optimal substructure? → yes
- principle of optimality? → yes
- local subproblems → global optimal solution

### Design

- Recurrence equation
1. 1차원 array 
    
    아이템을 담은 상태에서 profit 최대치 → 기록
    
    P[i] = i_th item까지 선택한 상태의 profit 누적
    
    P[i] = APSP i번째 도시를 방문/경유할지를 결정하는 문제와 유사
    
    p[i] = item_i를 담거나, 못 담거나
    
    = max (P[i-1], P[i-1]+p_i) ← 맞나요? 아닙니다 
    
    → weight에 대한 고려가 없음
    
2. 2차원 array: item 가치, 무게
    
    P[i, w] = max 1) P[i-1, w] // item_i를 못 담는 경우
    
                      2) P[i-1, w] + p_i // item_i를 담는 경우
    
    → 맞나요? 아닙니다. 
    
    → item_i를 담기 위해서는 그 전 sack의 w_i만큼이 비어 있어야한다.
    
3. Final
    
    P[i, w] = max 1) P[i-1, w] // item_i를 못 담는 경우
    
                      2) P[i-1, w- $w_i$] + p_i  //담을 때 현재 가방 수용 가능 weight 에서 w_i를 빼준다
    
- Example
    
    ```jsx
    S = {item_1, item_2, ... item_4}
    W = 10kg(sack size)
    p_i = (10, 40, 30, 50)
    w_i = (5, 4, 6, 3)
    ```
    
    | P[i, w] | 0 | 1kg | 2kg | 3kg | 4kg  | 5kg | 6kg | 7kg | 8kg | 9kg | 10kg |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | item i =0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 10 | 10 | 10 | 10 | 10 |
    | 2 | 0- | 0 | 0 | 0 | 40 | 40 | 40 | 40 | 40 | 50 | 50 |
    | 3 | 0 | 0 | 0 | 0 | 40 | 40 | 40 | 40 | 40 | 50 | 70 |
    | 4 | 0 | 0 | 0 | 50 | 50 | 50 | 50 | 90 | 90 | 90 | 90 |
    
    P[1,4] = p[i-1, w] = p[1-1, 4] = P[0,4] = 0
    
    P[1,5] = P[i-1, w-w_i] + p_i = P[i-1, w-w_i] + p_1 = 0 + p_1 = 10
    
    item_2 rhals == Floyd for APSP
    
    → 2번 도시 선택 문제는 1번 도시까지의 subproblem이 모두 해결된 상태에서 2번의 이슈를 추가 계산
    
    P[2,4] = max 1)P[1,4] = 0
    
                           2) P[1,0] + P_2 = 0 + 40 = 40
    
    P[2,5] = max 1)P[1,5] = 10
    
                           2) P[1,0] + P_2 = 0 + 40 = 40
    
    P[2,9] = max 1)P[1,9] = 10
    
                           2) P[1, 9-w_2] + P_2 = P[1, 5] + 40 = 10 + 40 = 50
    
    APSP. CMM. 
    

### Analysis

Time complexity: T(n, w) = TC for each subprob * nw = 상수 * nw = O(nw)

→ if W is huge → terrible performance

→ polynomial time complexity: input size ‘n’

→ W value: depends on numeric value of input W

⇒ Pseudo polynomial time complexity

→ improve 노력. 

→ 전체 셀을 다 계산하는 건 필요가 없어! 필요한 것만 하자!

 ⇒ DP optimization

operations = 1+2+$2^2$+...+$2^{n-1}$ =O( $2^n$)

Final TC = min {O(nW), O( $2^n$)}

⇒ BF와 다를 것이 없다...

- Q: 왜 이런 현상이 일어났을까요?
    
    → 문제의 난이도가 다르기 때문에.