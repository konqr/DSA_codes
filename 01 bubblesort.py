#bubblesort

A = input().split(' ')

for i in range(0,len(A)):
	for j in range(len(A)-1,i,-1):
		if A[j] < A[j-1]:
			temp = A[j]
			A[j] = A[j-1]
			A[j-1] = temp

print(A)