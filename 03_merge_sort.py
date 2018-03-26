import math 

def MERGE(A, left, right):
	i = j = k =  0
	while (i<len(left)) and (j<len(right)):
		if left[i] < right[j]:
			A[k] = left[i]
			i+=1
		else:
			A[k] = right[j]
			j+=1
		k+=1
	
	while(i<len(left)):
		A[k] =left[i]
		i+=1
		k+=1
	while(j<len(right)):
		A[k] = right[j]
		j+=1
		k+=1

def Merge_Sort(A):
	left = []
	right = []
	n = len(A)
	if (n<2):
		return
	mid = int(n/2)
	for i in range(0,mid):
		left.append(A[i])
	for i in range(mid,n):
		right.append(A[i])
		
	Merge_Sort(left)
	Merge_Sort(right)
	MERGE(A, left, right)

A = input().split(' ')
Merge_Sort(A)
print(A)
	