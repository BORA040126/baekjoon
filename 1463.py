#출처: http://samron.tistory.com/129

a = int(input())

array=[0] * (a+1) #0을 담아 a+1 크기로

 

for i in range(2, a+1):

    array [i] = array[i-1] +1  

    if(( i % 3 ) == 0):

        array [i] = min(array [i], array[i//3] + 1)

    if(( i % 2 ) == 0):

        array[i] = min(array[i], array [i//2] + 1)

print(array [a])