a=int(input())
count=0
while a>=5:
    count+=a//5
    a//=5
print(count)