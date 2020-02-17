#### single for loop '*' pyramid
n = 5
k = n-1
for i in range(n):
	print(' '*k,end='')
	print('*'*(2*i+1))
	k -= 1