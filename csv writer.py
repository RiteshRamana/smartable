import csv

print("Manager's Page \n")

def add():
    name=input('Enter the name of the item to be added : ')
    cost=int(input("Enter the item's cost : "))
    with open('menu.csv', mode ='r')as f:
        r=csv.reader(f)
        c=0
        for line in r:
            if line!=[]:
                c+=1
    with open('menu.csv', mode ='a')as f:
        w=csv.writer(f)
        w.writerow([c+1, name, cost])
        print('record added')


def rem():
    
    f=open('menu.csv', 'r', newline='\r\n')
    r=csv.reader(f)
    l=[]
    for i in r:
        print(i[0],end='\t')
        print(i[1],end=(30-len(i[1]))*' ')
        print(i[2])
        l+=[i]
    Sno=int(input('Enter S.No of Item to remove : '))
    f.close()
    
    for i in range(len(l)-1):
        if l[i][0]==str(Sno):
            l.remove(l[i])
        l[i][0]=i+1
    
    with open('menu.csv', mode ='w')as f:
        c=1
        csv.writer(f).writerows(l)
        c+=1

    print('record removed')


def fb():
    with open('Feedback.txt', mode ='r')as f:
        l=f.readlines()
        print(l)
        for i in l:
            print(i)
def upd():
    
    l=[]
    with open('menu.csv', mode ='r', newline='\r\n')as f:
        r=csv.reader(f)
        for i in r:
            print(i[0],end='\t')
            print(i[1],end=(30-len(i[1]))*' ')
            print(i[2])
            l+=[i]
    
    Sno=int(input('Enter S.No of Item to update : '))
    name=input('enter new name : ')
    cost=int(input('enter new cost : '))
    with open('menu.csv', mode ='w')as f:
        w=csv.writer(f)
        l=l[:Sno-1]+[[Sno,name,cost]]+l[Sno:]
        for i in l:
            w.writerow(i)
            
            

ip=int(input('1. Add \n2. Update \n3. Remove \n4. See Feedback\n'))
while ip in [1,2,3,4]:
    if ip==1:
        add()
    elif ip==2:
        upd()
    elif ip==3:
        rem()
    elif ip==4:
        fb()
    else:
        print('PLS ENTER VALID VALUE')
    print('TO perform any other function, enter 1,2,3,4.')
    ip=int(input('To exit enter any other number'))
