arr = list(map(int,input("Enter the array elemenst : ")))
n = len(arr)
l=[]
arr = sorted(arr,reverse=True)
count = 0
for j in range(n):
    if arr[j] == j:
        count += 1


print(count)
