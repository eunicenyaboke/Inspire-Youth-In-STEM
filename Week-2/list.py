names = ["Marie","Wairimu","Eunice","Nyaboke","Kezz"]
#accesing items in a list 
print(names)
print(names[0])
print(names[-1])
print(names [3])
print(names [0:3])
fruits = ["Bananas","oranges","apples","melons","pawpaw"]
print(fruits [0:-1])
print(fruits[3])
print("My favorite fruit is",fruits[0].upper())
#Adding two lists
vegetables =["greenpepper","managu","lettuce","onions","spinach"]
stationary = ["pens","ink","paper","pins"]
shoppings = vegetables +stationary
print (shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print ("My name is"+names[2]+ "and my favorite fruit is"+fruits[0] )