f=['Roti', 'aloo', "Paneer", "Naan"]
co=[60, 45,180,10]

# display menu with cost

for i in range(len(f)):
    print(i+1, "    ",f[i], "   ",co[i])

x=[] # for storing what the cust. orders
print("welcome to our restaurant!!")
a=("Enter S.No with quantity.")


#loop to get customer orders

while True:
    a=int(input(("Enter S.No of food")))
    if a>len(f):
        a=len(f)-1
    b=int(input(("Quantity of "+f[a-1]+":")))
    c=input("Anything else? Type yes or no")
    x.append(a)
    x.append(b) # list will be : [S.no, Quantity, S.no, Quantity...]
    c=c.upper() # ensure that c is always caps
    if c=="YES":
        continue # go back and ask again
    else:
        c=input("Proceed to get bill? Type yes or no")
        c=c.upper()
        if c=="NO":
            continue
        else:
            break
n=1
final=0
y,z=[],[] # seperating S. No, present at even locations
for i in range(len(x)):
    if i%2==0:
        y.append(x[i])
    else:
         z.append(x[i])
         
# display final bill

for i in range(len(y)):
    item=f[y[i]-1]
    cost=co[y[i]-1]
    total=z[i]*cost
    final+=total
    print(item, cost, z[i],total)
print("Please pay $"+str(final))
fb=input("Your Feedback please")
x=[]+[fb]
print(x)
