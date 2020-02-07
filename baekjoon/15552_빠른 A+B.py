import sys
length = int(sys.stdin.readline())
arr = []

for i in range(length):
    input1 = list(map(int,sys.stdin.readline().split()))
    arr.append(input1[0] + input1[1])
    
for i in range(length):
    print(arr[i],sep='\n')