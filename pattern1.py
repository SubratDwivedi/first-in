i = 0
while i < 6:
	j = 0
	while j < i:
		print('*',end='')
		j +=1
	i+=1
	print()

n = 10
for i in range(n):
	for j in range(i):
		print('*',end='')
		n -=1
