N = int(input())
arr = list(map(int,input().split(" ")))
a = []

for i in range(len(arr)):
	if i < 3:
		a.append(arr[i])
	else:
		a.append(min(arr[i]+a[i-1], arr[i]+a[i-2], arr[i]+a[i-3]))
	
print(min(a[-1],a[-2],a[-3]))

'''
7
3 1 1 7 4 9 3

결과: 5

'''