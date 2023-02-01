import sys
import heapq
input = sys.stdin.readline

def BOJ1197() :
  V, E = map(int, input().split())
  
  graph = [[] for _ in range(V+1)]
  visited = [False for _ in range(V+1)]

  for _ in range(E) :
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

  def prim() :
    result = 0
    queue = []
    queue.append([0, 1])

    while queue :
      curr_cost, curr_node = heapq.heappop(queue)
      if visited[curr_node] == False :
        visited[curr_node] = True
        result += curr_cost
        for next_node, next_cost in graph[curr_node] :
          heapq.heappush(queue, (next_cost, next_node))
          
    return result 

  print(prim())

BOJ1197()