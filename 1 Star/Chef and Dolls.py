t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        num = int(input())
        if num in arr:
            arr.remove(num)
        else:
            arr.append(num)
    print(arr[0])

    
