import sys

def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in range(1, n + 1):
        if graph[x][i] and not visited[i]:
            dfs(i)

def bfs(x):
    queue = [x]
    visited[x] = True
    while queue:
        x = queue.pop(0)
        print(x, end=' ')
        for i in range(1, n + 1):
            if graph[x][i] and not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
