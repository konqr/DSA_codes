import random

def partition(A,p,q):
	x = A[p]
	i = p
	for j in range(p+1,q+1):
		if A[j] <= x:
			i = i+1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp = A[p]
	A[p] = A[i]
	A[i] = temp
	return i
	
def quick_sort(A,p,q):
	if p<q:
		r = partition(A,p,q)
		quick_sort(A,p,r-1)
		quick_sort(A,r+1,q)
		
A = input().split(' ')
quick_sort(A,0,len(A)-1)
print(A)