arr = [1,2,-1,3]
n = len(arr)
l=[]
arr = sorted(arr,reverse=True)
count = 0
for j in range(n):
    if arr[j] == j:
        count += 1


print(count)
