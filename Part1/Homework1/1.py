# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:16:27 2023

@author: Gustolandia
"""

def invert(A, inv=0):
    if len(A)==1 or len(A)==1:
        return A, inv
    else:
        B = A[:len(A)//2]
        C = A[len(A)//2:]
        B2, inv1=invert(B, inv)
        C2, inv2=invert(C, inv)
        inv=inv1+inv2
        i=0
        #print(B2,C2,inv1,inv2, inv)
        j=0
        k=0
        kMax=len(C2)+len(B2)
        final=[0]*(len(C2)+len(B2))
        while k<kMax:
            if i==len(B2):
                final[k]=C2[j]
                k+=1
                j+=1
            elif j==len(C2):
                final[k]=B2[i]
                k+=1
                i+=1
            elif int(B2[i])<=int(C2[j]):
                final[k]=B2[i]
                k+=1
                i+=1
            else:
                final[k]=C2[j]
                k+=1
                j+=1
                inv+=len(B2)-i
        return final, inv

if __name__ == "__main__":
    text_file = open("data.txt", "r")
    ListToSort = text_file.read().splitlines()
    text_file.close()
    final, inv=invert(ListToSort)
    print (inv)
                
    