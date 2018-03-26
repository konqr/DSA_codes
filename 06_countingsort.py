A = list(map(int,input().split(' ')))
k = int(max(A))
C = [0 for i in range(k)]
B = [0 for i in range(len(A))]
for j in range(0,len(A)):
	C[A[j]-1] = C[A[j]-1] + 1
for i in range(1,k):
	C[i] = C[i] + C[i-1]
for j in range(len(A)-1,-1,-1):
	B[C[A[j]-1]] = A[j]
	C[A[j]-1] = C[A[j]-1] - 1
print(B)	