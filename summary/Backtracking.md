# Backtracking

Brute-Force design:

Q. How to implement BF?

- Ex. 동전 2개의 모든 조합 나열
    
    → For-loop 구현
    
    → Graph 탐사: DFS, BFS 
    
- Ex. 미로공원. Maze problem
- Ex. 4 - Queen problem: place 4 Qs onto 4x4 chess board

### Idea: 모든 탐색 가능한 조합을 검사하고 나열할 필요가 있을까?

Backtracking의 정의

1. DFS(깊이 우선 탐색) of a tree except that nodes are visited if promising
2. Backtrack if NON-promising: pruning
3. Do a DFS of state-space tree. (formal)
    
    checking whether each node is promising, and if it is nonpromising, backtracking to the node’s parent.
    

do a DFS of a state-space tree, checking whether each node is promising, and if it is nonpromising, backtracking to the node’s parent

### N-Queens problem

- Time complexity: ex. 8-Queen problem → 64^8: 조합 수
    
    → search- space tree.
    

4-Queens problem

- step 1
    
    
    | Q1 | Q |  |  |  |
    | --- | --- | --- | --- | --- |
    | Q2 | 안됨 | 안됨 | Q |  |
    | Q3 | 안됨  | 안됨 | 안됨 | 안됨 |
    | Q4 |  |  |  |  |
    
    → Q3이 들어갈 수 있는 곳이 없음 
    
    → Q2 백트래킹
    
- step 2
    
    
    | Q1 | Q |  |  |  |
    | --- | --- | --- | --- | --- |
    | Q2 | 안됨 | 안됨 | Q→X | Q |
    | Q3 | 안됨  | Q | 안됨 | 안됨 |
    | Q4 | 안됨 | 안됨  | 안됨 | 안됨 |
    
    → Q3을 두번째에 놓으니까 안됨. 
    
    → Q3을 다른 곳에 놓아도 문제가 있음 
    
    → Q2로 백트래킹
    
    →Q2도 갈 곳 없음
    
    → Q1로 백트래킹
    
    ![Screen Shot 2022-05-06 at 5.34.54 PM.png](Backtracking%20044a55923e8f49d0a415b97f19a9fc71/Screen_Shot_2022-05-06_at_5.34.54_PM.png)
    

### Design key: promising function의 설계

- N-queens 문제는 promising func가 명확히 주어짐
    
    DP. B.coefficient 문제는 reccurrence equation 주어지는 것처럼
    

### Analysis key

- optimality: 답이 있으면 반드시 정답을 찾는다.
- trivial ≠ efficiency
- time complexity = exponential. (not poly time) BF complexity
- 중요성: empirical test 실험적 성능

⇒ backtracking은 BF보다 이론적으로 빠르지 않지만 답이 무조건 나오고, 실험적인 성능으로 노드수가 얼마나 안 생기는지를 파악해서 사용해야한다는 것을 인지해야한다.

### Sum of Subset Problem(Subset Sum Problem)

: a special case of 0/1 KS

```jsx
S = {item1, item2,... ,item_n}
weight = {weight1, weight2, ..., weight_n)
W: fixed weight(Given)
```

→ Find A such that the sum of weights in A equals W

변형문제 

```jsx
//Game server load balancing 
weight_i = {5, 6, 10, 11, 16}
W = 21
```

→ {i1, i2, i3}, {i1, i5}, {i3, i4}

- design
    - Brute-force
        - 모든 가능한 부분집합 나열
            1. for loop
            2. DFS
            
            → O(2^n)
            
    - Backtracking for subset sum problem
        
        Design: 
        
        step1. promising function
        
        - promising function = 수학적 표현 ⇒ T/F return
        
        1) i-th level: 
        
        weight + weight(i+1) > W
        
        → 다음 step 생각하지 않아도 됨
        
        2) weight + 미래 총 weight 합 < W
        
        → solution 만들 수 없으므로 다음 step 생각하지 않아도 됨
        
        ⇒ IF condition, then STOP
        
        ```jsx
        function promising(i: index){
        	return (Boolean: T/F) promising 1), 2) 조건 위배 여부
        }
        ```
        
        Analysis:
        
        1. optimal solution generated
        2. Execution time; timer. depending on promising functions
        3. 실제 생성된 노드수 = 15/31 ⇒ performance gain
        
        step2. DFS traverse/visit
        

Ex)

![Screen Shot 2022-05-06 at 6.33.01 PM.png](Backtracking%20044a55923e8f49d0a415b97f19a9fc71/Screen_Shot_2022-05-06_at_6.33.01_PM.png)

## Graph Coloring

== Vertex coloring problem

== m-coloring problem

- Ex) 강의실 무선 마이크 주파수 다르게 하기~
    
    ![Screen Shot 2022-05-06 at 6.47.30 PM.png](Backtracking%20044a55923e8f49d0a415b97f19a9fc71/Screen_Shot_2022-05-06_at_6.47.30_PM.png)
    

### CS solution

1. BF: complexity = T(n, m) = O(m^n)
    
    Q1. how to find minimun ‘m’? → NO . → efficient polynomial alo 적용 x
    
    Q2. given m(fixed), m-colaborable? → Yes or No (alg O)
    
    ⇒ Backtracking for GC
    
    위의 예제에 적용해보자!
    
    - 한 노드를 하나의 depth라고 생각
    - v1 → 빨, v2→ 파, v3→ 빨 ⇒ backtracking 이런 식으로
        
        ![Screen Shot 2022-05-06 at 7.00.59 PM.png](Backtracking%20044a55923e8f49d0a415b97f19a9fc71/Screen_Shot_2022-05-06_at_7.00.59_PM.png)
        
    - 

## Hamiltionian Circuits (HC) Problem

= Hamiltonian Path, Hamiltionian Cycle Problem

- Given a connected and undirected graph, HC 는 vertex를 오직 한 번씩만 지나고 다시 start vertex로 돌아와야함
- Promising fn:
    1. i_th node → i+1 node
    2. (n-1)_th node → 출발 노드
    3. i_th node cannot be one of zero ~ (n-1)th_nodes
- Analysis:
    - BF complexity: O(n!), DP
    - Backtracking: node 생성 수 , running time
    

# Knapsack

```jsx
S = {item1, item2,... ,item_n}
weight = {weight1, weight2, ..., weight_n)
price = { price1, price2, ... , price_n}
W: fixed weight(Given)
```

![Screen Shot 2022-05-17 at 12.49.19 AM.png](Backtracking%20044a55923e8f49d0a415b97f19a9fc71/Screen_Shot_2022-05-17_at_12.49.19_AM.png)

### Promising function

- nonpromising한지 판별하기 위해서
1. weight > W 
    
    → stop, not expand(가지 밑으로 내려가지 x)
    
2. subset sum
    - weight + w(next item) > W
    
    → stop
    
    - weight + w(total sum of next items) < W (앞으로 나올 모든 애들 더해도 W보다 작으면 가지 X)
    
    → stop
    

⇒ 0/1 knapsack에서는 기준점이 변한다

→ 왜? profit을 가장 크게 해줘야하기 때문에 profit이 계속 변한다.

⇒ 다이아 + 금 집합의 profit > 금 + 큐빅 집합 nonpromising

⇒ Nonpromising function == Bounding function (갈 필요 없으면 가지치기 안 하고 멈춘다)

### Bound function

= 지금까지의 profit(`g`) + 남은 아이템이 줄 수 있는 이익의 최대 추정치(`h`)

(중요) bound function = `g` + `h` < 현재 했던 것들 중 BEST (nonpromising) (향후 하는 짓이 의미가 없다)

h: 우리가 다르게 계산할 수 있음. 그때그때 달라요~

bound = 현재(g) + 미래 예측(h: idea 필요한 곳) < Best 

h: heuristic 경혐. 인사이트

### Bound function for 0/1 Knapsack Problem

bound function = g + h

g = (item_1, item_2, ... item_i) → sum of profit_j (j = 1...i)

h = (item_i+1, item_i+2, ... , item_k) → sum of profit_j (j = i+1...k) (k는 담을 수 있는 최대점)

+

(item_k+1의 일부) p_k+1/w_k+1  *   (W - (w1+w2+...+wk))

### Backtracking 예제

```jsx
S = {item1, item2, item3 ,item_4}
price = {40, 30, 50, 10)
weight = { 2, 5,10 , 5}
W: 16
```

각 node당 g와 h를 나눠서 계산하면서 진행

g, W, h 값을 넣으면서 진행해보자..

![Screen Shot 2022-05-17 at 1.47.51 AM.png](Backtracking%20044a55923e8f49d0a415b97f19a9fc71/Screen_Shot_2022-05-17_at_1.47.51_AM.png)