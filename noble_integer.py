arr = list(map(int,input("Enter the array elemenst : ").split()))
n = len(arr)
l=[]
arr = sorted(arr)
count = 0
for j in range(n):
    if arr[j] == j:
        count += 1


print(count)
