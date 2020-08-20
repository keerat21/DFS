# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:23:18 2020

@author: Hp User
"""


class Vertex:
    def __init__(self,n):
        self.name = n;
        self.friends = list();
        
        self.dis = 0
        self.f = 0
        self.color = 'black'
    def add_friend(self, v):
        nset = set(self.friends)
        if v not in nset:
            self.friends.append(v)
            self.friends.sort()
            
class graph:
    vertices = {}
    time = 0
    
    def add_vertex(self, vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for k,val in self.vertices.items():
                if k == u:
                    val.add_friend(v)
                if k == v:
                    val.add_friend(u)
            return True
        else:
            return False 
    
    
    
    def print_graph(self):
        for k in sorted(list(self.vertices.keys())):
            print(k + str(self.vertices[k].friends) + " " + str(self.vertices[k].dis))
            
        
    def _dfs(self, vertex):
        global time
        vertex.color = 'red'
        vertex.dis = time
        time += 1
        for v in vertex.friends:
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])
        vertex.color = 'blue'
        vertex.f = time
        time += 1
        
    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)
        
g = graph()

a = Vertex('A')
g.add_vertex(Vertex('B'))
for i in range(ord('A',ord('k'))):
    g.addvertex(Vertex(chr(i)))
    
edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])
    
g.dfs(a)

g.print_graph()
        
    
