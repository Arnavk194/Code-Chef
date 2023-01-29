t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    h = {6,7,13,14,20,21,27,28}
    h.update(arr)
    print(len(h))