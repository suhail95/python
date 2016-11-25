#  IMPLEMENTATION OF BFS

from pythonds.basic.queue import Queue
graph={0:[1,3,4],1:[2,4],2:[5],3:[4,6],4:[5,7],5:[],6:[4,7],7:[5,8],8:[]}
q=Queue()
waiting=[]
visited=[]

def BFS(graph):
   q.enqueue(0)
   waiting.append(0)
   while not q.isEmpty():
        p=q.dequeue()
        print p,
        visited.append(p)
        for i in graph[p]:
           if i not in visited and i not in waiting:
                q.enqueue(i)
                waiting.append(i)

BFS(graph)
