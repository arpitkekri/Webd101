t=int(input())
for i in range (t):
    a = input().split(" ")
    x=int(a[0])
    y=int(a[1])
    z=int(a[2])
    if z >= (x+y) or y >= (x+z) or x >= (y+z):
        print('NO')
    else:
        print('YES')



        