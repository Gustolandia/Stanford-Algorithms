# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:51:55 2023

@author: Gustolandia
"""

def DFS(G,i,explored,t,s,leader,F):
    explored[i-1]=1
    leader[i-1]=s
    for k in G:
        if explored[k[1]-1]==0:
            explored, t,leader, F= DFS(G,i,explored,t,s,leader,F)
    t+=1
    F[i-1]=t
    return explored, t,leader, F

def DFS_loop(G):
    t=0
    s=0
    explored=[0]*G[-1][0]
    leader=explored=[0]*G[-1][0]
    F=[0]*len(G)
    for i in reversed(G):
        if explored[i[0]-1]==0:
            s=i[0];
            explored, t,leader, F= DFS(G,i[0],explored,t,s,leader,F)
    return explored, t,leader, F
    


if __name__ == "__main__":
    text_file = open("SCC1.txt", "r")
    ListTo = text_file.read().splitlines()
    for i in range(len(ListTo)):
        ListTo[i]=ListTo[i].split(" ")
        ListTo[i][0]=int(ListTo[i][0])
        ListTo[i][1]=int(ListTo[i][1])
    text_file.close()
    t=0
    s=0
    explored=[0]*ListTo[-1][0]
    leader=explored=[0]*ListTo[-1][0]
    F=[0]*ListTo[-1][0]
    explored, t,leader, F=DFS(ListTo,i,explored,t,s,leader,F)
    print (explored, t,leader, F)