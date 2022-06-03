a = int(input())
for i in range(a):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    b = (x * n)- sum(arr)
    print(max(b,0))
    

