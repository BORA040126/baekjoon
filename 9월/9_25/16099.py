a = int(input())
l=[]
for i in range(a):
    lt, wt, le, we = map(int, input().split())

    area_telecom = lt * wt
    area_eurecom = le * we
  
    if area_telecom > area_eurecom:
        l.append("TelecomParisTech")
    elif area_telecom < area_eurecom:
        l.append("Eurecom")
    else:
        l.append("Tie")
 
for i in range(len(l)):
    if i == len(l) - 1:
        print(l[i], end="")
    else:
        print(l[i])