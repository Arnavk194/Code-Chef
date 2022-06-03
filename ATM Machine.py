t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    for j in arr:
        if k - j >= 0:
            k = k - j
            print("1",end = "")
        else:
            print("0",end = "")
    print("")

