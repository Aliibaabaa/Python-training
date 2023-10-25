#basic arithmetic


#use for loop to find and print the sum all even numbers from 1-20

sum = 0

for num in range(1, 21):
    if num % 2 == 0:
        print(num)
        sum += num
        
print('Sum:' , sum)
print(f'Sum is: {sum}')