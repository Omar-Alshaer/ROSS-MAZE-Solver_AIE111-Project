#=========================
# bfs.py
#=========================


from collections import deque

def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    prev = [[None for _ in range(cols)] for _ in range(rows)]
    
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    
    visited_order = []
    
    while queue:
        r, c = queue.popleft()
        visited_order.append((r, c))
        
        if (r, c) == goal:
            break
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            
            if grid[nr][nc] == 1:
                continue
            
            if not visited[nr][nc]:
                visited[nr][nc] = True
                prev[nr][nc] = (r, c)
                queue.append((nr, nc))
    
    path = []
    if visited[goal[0]][goal[1]]:
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = prev[cur[0]][cur[1]]
        path.reverse()
    
    return visited_order, path
