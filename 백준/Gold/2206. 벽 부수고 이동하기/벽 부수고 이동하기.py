# 벽 부수고 이동하기
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        cur_x, cur_y, c = queue.popleft()
        
        if cur_x == N - 1 and cur_y == M - 1:
            return visited[cur_x][cur_y][c]
        
        for x,y  in zip(dx,dy):
            nx = cur_x + x
            ny = cur_y + y

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 다음 이동할 곳이 벽이고, 벽파괴 기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[cur_x][cur_y][0] + 1
                queue.append((nx, ny, 1))

            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[cur_x][cur_y][c] + 1
                queue.append((nx, ny, c))
                
    return -1


print(BFS(0, 0, 0))
