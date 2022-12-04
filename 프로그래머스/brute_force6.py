from collections import deque

def bfs(graph, start, visited): 
    queue = deque([start]) # 현재 노드를 방문 처리함
    visited[start] = True
    count = 0

    while queue:
        v = queue.popleft() # 큐에서 앞의 원소 하나를 뽑음
        count = count + 1
        for i in graph[v]: # 아직 방문하지 않은 원소들을 큐에 넣음
            if not visited[i]:
                queue.append(i)
                visited[i] = True # 방문한 원소를 True로 대이
    
    return count

def solution(n, wires):
    result = n - 2 # 송전탑의 개수 차이의 절댓값 중 최댓값 
    for i in range(len(wires)):
        tmp = wires.copy()
        graph = [[] for i in range(n + 1)]
        visited = [False] * (n + 1)
        tmp.pop(i) # i번째 전선을 제거
        for wire in tmp:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for index, g in enumerate(graph):
            if g != []:
                start = index
                break
        cnt = bfs(graph, start, visited) # bfs를 이용하여 시작점에서 다른 송전탑을 탐색
        other_cnt = n - cnt # 첫번째 전력망의 갯수는 cnt이므로 나머지 전력망은 n - cnt
        if abs(cnt - other_cnt) < result:
            result = abs(cnt - other_cnt)

    return result 

# 출력
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
