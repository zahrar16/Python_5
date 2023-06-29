

def star_lozi (n):

    for i in range(1, n+1):
        print(((n-i)+1) * ' ' + (2*i-1) * '*')

    print(((2 * n) + 1) * '*')

    for j in range(n ):
        print((j+1) * ' ' + (2*n-(((j + 1) * 2 )- 1)) * '*')


star_lozi(int(input()))        