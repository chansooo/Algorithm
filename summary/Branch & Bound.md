# Branch & Bound

# Design

- N-Queens Problem
    
    → Non-optimization Problem(최적화를 요구하지 x)
    
- 0/1 KS Problem
    
    → Optimization Problem (최적화 문제)
    

→Compute 

- promising func
- bounding func
- evaluation func

→ Nonpromising if < Best

→ f = g(exact) + h(estimate)

Maximization Optimization Problem (ex. 0/1 KS)

: 각 node에서 upper bound 계산

Minimization Optimization Problem(ex. TSP)

: 각 node에서 lower bound 계산 (얼마나 더 짧아질 수 있는지 미래 계산)

Backtracking = DFS + bound function

→ Q: DFS를 BFS로 전환하면? 

→ Branch and Bound 전략

시작해봅시당 

NEW algorithm design: Branch and Bound

Question: Backtracking vs Branch and Bound

Tips:

Backtracking = `DFS` + bound function

B&B = `BFS` + bound function

→ 조합을 방문하는 방법의 차이

Q1. DFS vs BFS 장단점을 논하시오

→ in practice, B&B >> Backtracking(BFS >> DFS_

→ 왜냐면 BFS가 더 reliable

Q2. f=g+h < Best (bound function) 관점에서 비교

→ tree traverse(child visiting) 순서에 따라, g value와 h value는 update 차이가 발생한다.

> 미래 estimate ‘h-value’가 좋으면(정확한 예측이 가능하면), BFS로 진행하는 것이 좋다.
→ start root 에서 pruning이 일찍 발생하면 밑에 가지를 안 봐도 된다!
> 

> backtracking은 탐색을 진행할수록 ‘g-value’가 빨리 갱신된다.
→ g-value가 정확해지고, h-value에 대한 불확실성이 빠른 속도로 줄어든다.
> 

Key point:

우리가 h-value 설계/추정/수식유도 등에 경험을 통해 자신감이 향상되면 B&B가 우월함

→ 그렇지 않으면 그냥 Backtracking으로 하자..

### 예시

```jsx
S = {item1, item2, item3 ,item_4}
price = {40, 30, 50, 10)
weight = { 2, 5,10 , 5}
W: 16
```

g, w, f를 표시하며 BFS를 진행 (upper bound를 생각하면서 진행하는 것을 잘 생각하자)

![Screen Shot 2022-05-17 at 4.04.17 PM.png](Branch%20&%20Bound%2072fc6c1476b0479482b269f6e5504f8e/Screen_Shot_2022-05-17_at_4.04.17_PM.png)

depth를 기준으로 진행이 되기 때문에 일찍 bound값이 계산이 되어 최적화를 더 잘 할 수 있다.

## Improbe the standard Branch-and-Bound

### Idea

- node를 방문하는 순서를 기반으로
- promising func와 bound func가 업데이트 되는 것을 관찰
- 방문 순서를 바꿔보자

### New B&B algorithm

- New Branch and Bound with Best-First
    
    ![Screen Shot 2022-05-18 at 2.00.20 PM.png](Branch%20&%20Bound%2072fc6c1476b0479482b269f6e5504f8e/Screen_Shot_2022-05-18_at_2.00.20_PM.png)
    
    - f의 값이 큰 쪽을 먼저 해준다
    - upper bound, promising 값이 최대인 곳을 찾아서 간다.
    - 가서 의미 있는 곳만 간다
- 만약 promising/bound-value가 다른 값이 배정된다면?
- Best-frist B&B: + greedy approach (local optimal choice)
    
    → 이것이 optimal한지 확인해야함 (증명이 필요)
    

## H-value

### Guideline for h-value

: h-value의 range를 설정하며 범위를 좁혀감

1. 0 < h < INF
2. $h^*$: global optimal value → h와 $h^*$의 관계성 유추
    1. h > $h^*$: overestimate 
    2. h < $h^*$: underestimate
3. overestimate 선호 (왜냐하면 실수가 나오지 않음(pruning 해야하는거 안 하는 상황 x)
    1. optimal로 진행가능한 가지를 pruning out하지 않음
    2. 보수적인 pruning, 안정적인 pruning
    3. pruning되는 subtree 가지의 수는 적을 수 있음
        
        ex) 0/1 KS : fractional
        
4. 0 < $h^*$ < h < INF
    
    h는 $h^*$보다 큰 값 중에서 가장 작은 값이 좋다 (왜냐하면 pruning power)
    
    → h = $h^*$ + alpha(small value)
    
5. Q: 0/1 KS에서 활용한 frac. KS를 이용한  h-value보다 더 pruning이 많이 되는 h-value 수식을 제시하시오

0/1 KS problem : h = overestimate expression

→upper bound → maximization optimization

Minimization Optimization Problems : TSP

→ h = underestimate value

→lower bound