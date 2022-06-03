t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    temp=0
    c=False
    for j in range(len(l)):
        if (l[j]+temp)-b<0:
            print(f"NO {j+1}")
            c=True
            break
        else:
            temp=(l[j]+temp)-b
    if not c:
        print("YES")