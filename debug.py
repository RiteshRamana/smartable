import csv
f=open('menu.csv','w')

food=['Mexican Wrap','Panner Wrap','Grilled Chicken Wrap','Chicken Shawarma','Fried Chicken Burger','Eggroll','Grilled Cheese Sandwich','French Fries','Non veg loaded Pizza','Chesse chicken Pasta','Potato Nuggets','Cappucino','Fresh lime juice','bluemoon','Chocolate Brownie']
co=[85, 70,100,95,130,90,120,60,150,70,100,100,89,90,100]
l=[]
for i in range(len(food)):
    
    csv.writer(f).writerow([i+1, food[i],co[i]])
f.close()
