rows,columns=list(map(int,input().split()))
B=int(input())
num_list=[]
for i in range(rows):
    row=list(map(int, input().split()))
    modified_row=[element*B for element in row]
    num_list.append(modified_row)

for row in num_list:
    print(row)
