result = []
def ex():
    n = int(input())
    a = input()
    count = 0
    for i in range(n):
        if(a[i] == 'H'):
            count +=1
        elif(a[i] == 'T'):
            count -=1
        if(count < 0 or count > 1):
            result.append("Invalid")
            return          
    if(count==0):
        result.append("Valid")
    else:
        result.append("Invalid")
for t in range(int(input())):
    ex()
for p in range(len(result)):
    print(result[p])
