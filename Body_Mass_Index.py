n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    c = a / b ** 2
    print(c)
    if(c <= 18):
        print("1")
    elif(c <= 19 and c >= 24):
        print("2")
    elif(c <= 25 and c >= 29):
        print("3")
    elif(c >= 30):
        print("4")