input1 = int(input())
input2 = str(input())
result = []

for i in range(len(input2)):
    number = int(input2[i:i+1])
    result.append(str(input1 * number))
    result = list(map(int,result))
    
result2=input1 * int(input2)

print(result[2],result[1],result[0],result2, sep='\n')