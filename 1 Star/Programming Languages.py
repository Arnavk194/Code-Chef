t = int(input())
for i in range(t):
    a,b,a1,b1,a2,b2 = map(int,input().split())
    if ((a1 == a or a1 == b) and (b1 == a or b1 == b)):
        print("1")
    elif ((a2 == a or a2 == b) and (b2 == a or b2 == b)):
        print("2")
    else:
        print("0")
