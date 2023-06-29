
def star (b, c):
    a =[]
    for i in range(b):
        a.append([])

    for i in range(b):
        if i % 2 == 0:
            for j in range(c):
                if j%2 == 0:
                    a[i].append('*')
                elif j%2 == 1:
                    a[i].append('#')
        else:
            for j in range(c):
                if j%2 == 0:
                    a[i].append('#')
                elif j%2 == 1:
                    a[i].append('*')       

    for row in a:
        print(row)      


star(int(input("enter yor rowa")), int(input("enter your cols")))