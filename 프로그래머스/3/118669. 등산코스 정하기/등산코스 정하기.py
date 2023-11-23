import heapq
INF = int(1e9)

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for s, e, w in paths:
        graph[s].append((e, w))
        graph[e].append((s, w))
    
    summits_set = set(summits)
    intensity = [INF] * (n + 1)
    q = []
    
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(q, (0, gate))
    
    while q:
        max_intensity, cur_node = heapq.heappop(q)
        if cur_node in summits_set or intensity[cur_node] < max_intensity:
            continue
        for next_node, w in graph[cur_node]:
            cost = max(max_intensity, w)
            if cost < intensity[next_node]:
                intensity[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    min_intensity = INF
    min_summit = 0
    for summit in summits:
        if intensity[summit] < min_intensity:
            min_intensity = intensity[summit]
            min_summit = summit
        elif intensity[summit] == min_intensity and summit < min_summit:
            min_summit = summit

    return [min_summit, min_intensity]

