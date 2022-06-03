t = int(input())
temp = 0
for i in range(t):
    a = int(input())
    arr = list(map(int,input().split()))
    for j in range(a):
        if(arr[j]<=1000):
            temp=+1
        else:
            pass
    print(temp)