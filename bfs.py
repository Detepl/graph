def bfs(visited,graph,queue):
    rez_bfs=queue.copy()
    while queue:
        s = queue.pop(0)

        for neighbour in graph[s]:
            if neighbour not in visited:
                rez_bfs.append(neighbour)
                visited.append(neighbour)
                queue.append(neighbour)
    return rez_bfs

graph = {
    "0":{"1","2"},
    "1":{"4","5"},
    "2":{"3"},
    "3":{},
    "4":{"6"},
    "5":{},
    "6":{}
    }

print(bfs([],graph,["0"]))