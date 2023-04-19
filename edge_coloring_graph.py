import random
#генерация простых неориентированных, невзвешанных графов
n=int(input("Введите кол-во вершин графа - "))
graph=[[0 for j in range(0,n)]for i in range(0,n)]
for i in range(1,n):
    for j in range(0,i):
        k=random.randint(0,1)
    
        graph[i][j]=k
        graph[j][i]=graph[i][j]
        

#t_graph - транспонированный граф (где столбцы в исх. графе это строки)
t_graph = [[0 for j in range(0,len(graph))]for i in range(0,len(graph))]

for i in range(0,len(graph)):
    for j in range(0,len(graph)):
        t_graph[j][i]=graph[i][j]


def choose_colour(strk, stlb, colours):#находит в строке цвет с минимальным индексом, который не используется
    strk.extend(stlb)
    for i in colours:
        if i not in strk:
            return i
    return max(colours)+1



colours=[2]
#пебирает нераскрашенные вершины, отправляет в функцию choose_colour строку и столбец с этим элементом, и красит в полученный цвет
for i in range(0,len(graph)):
    for j in range(i+1,len(graph)):
        
        if graph[i][j]==1:
            colour = choose_colour(graph[i],t_graph[j],colours)
            
            graph[i][j] = colour
            graph[j][i] = colour

            t_graph[i][j] = colour
            t_graph[j][i] = colour

            if colour not in colours:
                colours.append(colour)


print(colours)
for i in range(0,len(graph)):
    for j in range(0,len(graph)):
        print(graph[i][j],end=" ")
    print()
            
        
    


