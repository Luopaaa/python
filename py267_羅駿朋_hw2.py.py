#for

n=int(input('輸入的值:'))


for i in range(1,n+1):
    for j in range(1,n+1):
        print('%d * %d = %d'%(i,j,i*j))


#

i=0
j=0
n=int(input('輸入的值:'))

while i <n:
    j=0
    i += 1
    while j < n:
        j += 1      
        print('%d * %d = %d'%(i,j,i*j))

