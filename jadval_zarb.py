

def jadval_zarb (b, c):
    a = []
    for i in range (b):
        a.append([])

    for i in range (b):
        for j in range (c):
            a[i].append((i+1)*(j+1))  


    for row in a:
        print(row)

jadval_zarb (int(input("enter rows")), int(input("enter cols")))        