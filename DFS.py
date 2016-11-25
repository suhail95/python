#  IMPLEMENTATION OF DFS

from pythonds.basic.stack import Stack
graph={0:[4,3,2,1],1:[5,4,2],2:[5,3],3:[6],4:[7],5:[8,7,6],6:[9],7:[8],8:[9],9:[]}
s=Stack()
visited=[]
def DFS(graph):
   s.push(0)
   while not s.isEmpty():
       p=s.pop()
       if p not in visited:
            print p,
            visited.append(p)
            for i in graph[p]:
                if i not in visited:
                       s.push(i)

DFS(graph)
