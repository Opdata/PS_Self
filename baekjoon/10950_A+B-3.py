length = int(input())
a = 0
b = 0
result = []

for i in range(length):
    list_a = list(map(int,input().split()))
    a = list_a[0]
    b = list_a[1]
    result.append(a+b)

for i in range(length):
    print(result[i],sep='\n')