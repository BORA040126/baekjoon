first=input()
second=input()
l,p=first.split(" ")
a,b,c,d,e=second.split(" ")
vec=int(l)*int(p)
a=int(a)-vec
b=int(b)-vec
c=int(c)-vec
d=int(d)-vec
e=int(e)-vec
print(a,b,c,d,e)