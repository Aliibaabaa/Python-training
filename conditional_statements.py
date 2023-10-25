# if-else statement

x = 10

if  x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")
    
#if-elseif-else

if  x > 10:
    print("x is greater than 5")
elif x == 10:
    print("x is equals to 10") 
else:
    print("x is less than 5")
    

y = 10.2
# AND - OR
if y >= 1 and y <= 10:
    print("1")
elif y >= 11 and y <= 20:
    print("2") 
else:
    print("3")


if y >= 1 or y <= 10:
    print("1")
elif y >= 11 or y <= 20:
    print("2") 
else:
    print("3")
    
# for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I love", fruit + "s!")
    
    
count = 1

while count < 5:
    print("Count:", count)
    count += 1