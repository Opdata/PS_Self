input1 = input().split()
a = int(input1[0])
b = int(input1[1])

if a > b:
    print(">")
elif a < b:
    print("<")
elif a and b:
    print("==")