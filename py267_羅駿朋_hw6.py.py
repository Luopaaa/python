file = open('stores_old.csv', 'r', encoding='big5')
file2= open('stores_new.csv','w',encoding='big5')

while True:
    line = file.readline()
    a=line.split(',')
    if not line:
        break
    a.pop(1)
    a.pop(1)
    a.pop(2)
    a.pop(4)
    b=str(a).strip('[')
    c=b.strip(']')
    d=c.replace("'",' ')
    print(d)
    file2.write(d+'\n')

file.close() 


