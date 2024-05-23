import operator

graph = {'Oradea':['Zerind','Sibiu'],'Zerind':['Oradea','Arad'],'Arad':['Zerind','Timisoara','Sibiu'],'Timisoara':['Arad','Lugoj'],'Lugoj':['Timisoara','Mehadia'],'Mehadia':['Lugoj','Dobreta'],'Dobreta':['Mehadia','Craiova'],'Craiova':['Dobreta','Rimnicu Vilcea','Pitesti'],'Sibiu':['Arad','Oradea','Rimnicu Vilcea','Fagaras'],'Rimnicu Vilcea':['Sibiu','Craiova','Pitesti'],'Fagaras':['Sibiu','Bucharest'],'Pitesti':['Bucharest','Rimnicu Vilcea','Craiova'],'Bucharest':['Fagaras','Pitesti','Giurgiu','Urziceni'],'Giurgiu':['Bucharest'],'Urziceni':['Bucharest','Hirsova','Vaslui'],'Hirsova':['Urziceni','Eforie'],'Eforie':['Hirsova'],'Vaslui':['Urziceni','Iasi'],'Iasi':['Vaslui','Neamt'],'Neamt':['Iasi']}
hsld = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}
dist = {}
fringe = {}

start = 'Arad'
goal = 'Bucharest'

#fringe[start] = hsld[start]
#print fringe

def greedyBestFirstSearch(start,goal):
    if (hsld[start]==hsld[goal]):
        print 'Fount Road'
        return 0
    
    while True:
        if graph.has_key(start):
            for n in graph[start]:
                fringe[n] = hsld[n] 
                #print n,fringe[n]
            
        fringe1 = (sorted(fringe.items(), key=operator.itemgetter(1)))
        #fringe = fringe1
        #print (fringe1)
        print start,'(',hsld[start],') ->',
        start = fringe1[0][0]
        fringe.__delitem__(start)
        if fringe1[0][1] == hsld[goal]:
            print start,'(',hsld[start],')',
            break
                  
greedyBestFirstSearch(start,goal)    
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       