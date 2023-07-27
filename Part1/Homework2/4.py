def choosePivot1(A):
    if len(A)%2==0:
        sortedAr=sorted([int(A[0]), int(A[int(len(A)/2)-1]),int(A[-1])])
    else:
        sortedAr=sorted([int(A[0]), int(A[int(len(A)/2)]),int(A[-1])])
    print(sortedAr)
    return A.index(str(sortedAr[1]))



def partition(A, p):
    i=0
    P=int(A[p])
    for j in range(len(A)):
        if P==int(A[i]):
            i=i+1
        elif int(A[j])<P:
            memory=A[j]
            A[j]=A[i]
            A[i]=memory
            i=i+1
    memory=A[p]
    A[p]=A[i-1]
    A[i-1]=memory
    return A[:i-1],A[i:], memory

def quickSort(A, comp=0):
    n=len(A)
    p=0
    
    if n==1 or n==0:
        return A, comp
    else:
        print(A)
        x=choosePivot1(A)
        comp+=n-1
        memory=A[0]
        A[0]=A[x]
        
        A[x]=memory
        l,r, m=partition(A,p)
        l, comp=quickSort(l,comp)
        r, comp=quickSort(r,comp)

        A=[*l,m,*r]
        return A, comp
    
if __name__ == "__main__":
    text_file = open("QuickSort.txt", "r")
    ListToSort = text_file.read().splitlines()
    text_file.close()
    A, comp=quickSort(ListToSort)
    
    print (A, comp)
    