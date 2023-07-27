def choosePivot1(A):
    return 0


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
    print (A, i)
    memory=A[p]
    A[p]=A[i-1]
    A[i-1]=memory
    return A[:i-1],A[i:], memory

def quickSort(A, comp=0):
    n=len(A)
    p=choosePivot1(A)
    if n==1 or n==0:
        return A, comp
    else:
        comp+=n-1
        memory=A[0]
        A[0]=A[-1]
        A[-1]=memory
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
    