rows = 5
for i in range(rows):
    # nested loop for each column
    for j in range(i+1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")