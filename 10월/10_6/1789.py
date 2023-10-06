a=input()
count_0=0
count_1=0
for i in a:
    if i=="0":
        count_0+=1
    else:
        count_1+=1

count_0=count_0//2
count_1=count_1//2

print("0"*count_0+"1"*count_1)

