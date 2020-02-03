input1 = input().split()
a = int(input1[0])
b = int(input1[1])

if b-45 >= 0:
    b = b-45
elif b-45 < 0:
    b = b + 60 - 45
    if a>0:
        a = a - 1
    else:
        a = 24 - 1

print(a, b,sep='\n')