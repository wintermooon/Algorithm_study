def solution(n, computers):
    visited_list = [False]*(n)
    v = 0
    answer = 0
    while False in visited_list:
        v = visited_list.index(False)
        dfs(computers, visited_list, v)
        answer +=1
    return answer

def dfs (graph, visited_list,v):
    visited_list[v] = True
    for i in range(len(graph[v])):
            if v != i and graph[v][i] == 1 and visited_list[i] == False:
                dfs(graph, visited_list, i)


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))