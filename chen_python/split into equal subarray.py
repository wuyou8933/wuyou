##split point include
def Splitequal(Arr):
	if len(Arr) <= 1:
		return
	n = len(Arr)
	leftsum = 0
	for i in range(0, n):
		leftsum += Arr[i]
	rightsum = 0
	for i in range(n-1, -1, -1):
		rightsum += Arr[i]
		leftsum -= Arr[i]
		if rightsum == leftsum:
			return i
	return -1

def printTwopart(Arr):
	splitpoint = Splitequal(Arr)
	if splitpoint == -1:
		print("No such point")
		return
	for i in range(0,len(Arr)):
		if splitpoint == i:
			print("")
		print(Arr[i], end=" ")
Arr = [1,2,3,4,5,5]
printTwopart(Arr)
## delete split point
def divideArray(arr):
	n = len(arr)
	sum = 0
	for i in range(0, n):
		sum += arr[i]
	sum_so_far = 0
	for i in range(0, n):
		if 2 * sum_so_far + arr[i] == sum:
			return i
		sum_so_far += arr[i]
	return -1
arr = [6,2,3,2,1]

print(divideArray(arr))