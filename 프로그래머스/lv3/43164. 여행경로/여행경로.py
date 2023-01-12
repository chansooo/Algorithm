from collections import defaultdict
def solution(tickets):
    path = []
    route = defaultdict(list)
    for start, end in tickets:
        route[start].append(end)
    for airport in route.keys():
        route[airport].sort(reverse=True)
    stack = ['ICN']
    while stack:
        top = stack.pop()
        if top not in route or not route[top]:
            path.append(top)
        else:
            stack.append(top)
            stack.append(route[top].pop())
    return path[::-1]