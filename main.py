import csv
#Menu
l=[]
f=open('menu.csv', 'r', newline='\r\n')
r=csv.reader(f)
for i in r:
    print(i[0],end='\t')
    print(i[1],end=(30-len(i[1]))*' ')
    print(i[2])
    l+=[i]


x=[] # for storing what the cust. orders
print("Welcome to our Restaurant!!")
a=("Enter S.No with quantity.")


#loop to get customer orders

while True:
    a=int(input(("Enter S.No of food:")))
    if a>len(l):
        print('Please enter valid S.No')
        continue
    b=int(input(("Quantity of "+l[a-1][1]+":")))
    c=input("Anything else? Type yes or no:")
    x+=[l[a-1]+[b]] # list will be like : 
    #[['3', 'Grilled Chicken Wrap', '100', 20], ['8', 'French Fries', '60', 1]]
    #                                      qty                              qty
    c=c.upper() # ensure that c is always caps
    if c in ["YES", 'Y','YEAH','YEA']:
        continue # go back and ask again
    else:
        c=input("Proceed to get bill? Type yes or no:")
        c=c.upper()
        if c not in ["NO",'N', 'NAY', 'NOPE', 'NOP']:
            break


#BILL
final=0
print('S.No', end='    ')
print('Item Name', end=21*' ')
print('Cost  ' ,end= '' )
print('Qty')
for i in range(len(x)):
    print(i, end='\t')
    print(x[i][1], end=(30-len(x[i][1]))*' ')
    print(x[i][2], end='    ')
    print(int(x[i][3]))
    final+=int(x[i][2])*x[i][3]
print("Total Bill Amount: ₹ "+str(final))

#Feedback form

name=input("Your Name : ")
contact=input("Your Email/Phone : ")
fb=input("LEAVE US A FEEDBACK : ")
rating=int(input('How would you rate your experience with us(on a scale of 10)'))
print('Thank You for visiting us!')
from datetime import datetime
now = datetime.now()
with open('Feedback.txt', mode ='a')as f:
    f.write(name+'\t'+str(now)+'\n'+str(rating)+'/10 ')
    f.write(contact+'\n')
    f.write(fb+'\n\n')
