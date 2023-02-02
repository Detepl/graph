def dfs(visited, graph, node):
     if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    
    

graph = {
    "0":{"1","2"},
    "1":{"4","5"},
    "2":{"3"},
    "3":{},
    "4":{"6"},
    "5":{},
    "6":{}
    }

dfs([],graph,"0")
