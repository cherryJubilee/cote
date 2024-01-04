def solution(tickets):
    graph = {}
    for start, end in sorted(tickets, reverse=True):
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

    path = []
    def dfs(airport):
        while airport in graph and graph[airport]:
            dfs(graph[airport].pop())
        path.append(airport)

    dfs("ICN")
    return path[::-1]