'''идея алгоса: проходим в глубь граф, собирая время выхода каждой вершины,
инвертируем граф, и идём по инвертированну в порядке выхода вершин'''
def dfs(visited, graph, node):
    global time
    if node not in visited:
        visited.append(node)
        
        for i in graph[node]:
            dfs(visited,graph,i)
        time.append(node)
    
    return visited



def dfs_reverse(visited, graph, node):
    global time
    if node not in visited and node in time:
        visited.append(node)
        time.remove(node)
        
        for i in graph[node]:
            dfs_reverse(visited,graph,i)

    return visited



def reverse_graph(graph):
    r_graph={}
    for i in graph:
        for j in graph[i]:
            
            if j not in r_graph:
                r_graph.update({j:{i}})
                
            else:
                a = set(r_graph.pop(j))
                a.update(i)
                r_graph.update({j:a})
           
    return r_graph





graph = {'1': {'2', '3'},
         '2': {'3'},
         '3': {'4'},
         '4': {'1','5'},
         '5': {'6','7'},
         '6': {},
         '7': {'5','8'},
         '8': {'6'}}


time = []


dfs([],graph,'1')

r_graph = reverse_graph(graph)
time.reverse()
comp = []

while len(time)!=0:
    comp.append(dfs_reverse([], r_graph, time[0]))

print(comp)

