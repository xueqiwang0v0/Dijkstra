#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:03:27 2020

@author: xueqiwang
"""

def getGraph(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    
    graph = {}
    for line in lines:
        temp = line.split()
        vertex = int(temp[0])
        edges = {}
        for i in range(1, len(temp)):
            node = int(temp[i].split(',')[0])
            length = int(temp[i].split(',')[1])
            edges[node] = length
        graph[vertex] = edges
        
    return graph
        
def dijkstra(graph, start):
    X = set() # vertices processed so far
    X.add(start)
    V = set(graph.keys())
    A = dict()
    A[start] = 0
    
    vs = []
    ws = []
    ls = []
    while X != V:
        # get all the edges (v,w) that v in X and w not in X
        for v in X:
            for w, l in graph[v].items():
                if w not in A:
                    vs.append(v)
                    ws.append(w)
                    ls.append(A[v] + l)
        # find the one that minimizes A[v]+l
        w = ws[ls.index(min(ls))]
        # add w to X
        X.add(w)
        A[w] = min(ls)
        
        vs = []
        ws = []
        ls = []
    return A
        
    
    
graph = getGraph('dijkstraData.txt')
paths = dijkstra(graph, 1)
 
tmp = []
for keys in [7,37,59,82,99,115,133,165,188,197]:
    tmp.append(paths[keys])
print(tmp)