#float
# principal = 1000.0
# rate = 0.05 #5% annual interest rate
# time = 5 #years
#Calculate the final amount
# final_amount = principal * (1 + rate) ** time
# print(f"The final amount after {time} years is ${final_amount: .2f}")

#string
# user_message = "Hello, how are you today?"
# response = "I'm doing well, thank you!"
# #Concatenate and display the conversation
# full_conversation = user_message + " " + response
# print(full_conversation)

#boolean variables
# is_authenticated = True
# has_access_key = True
# #Check access permission
# if is_authenticated and has_access_key:
#     print("Access granted to the secure area.")
# else:
#     print("Access denied.")
#variable declaration and assignment
product_name = "Laptop"
product_quantity = 50
product_price = 1200.00
#calculate the tota; value of the product in stock
total_value = product_quantity * product_price
#display the product information
# print(f"Product Name: {product_name}")
# print(f"Available quantity: {product_quantity}")
# print(f"Unit Price: ${product_price:.2f}")
# print(f"Total value in stock: {total_value:.2f}")
#dynamic typing example
# variable = 42
# print(f"variable is of type: {type(variable).__name__}")
#change the variable to a string
# variable = "hello, python!"
# print(f"variable is now of type: {type(variable).__name__}")
#change the variable to a list
# variable = [1, 2,3, 4, 5]
# print(f"variable is of type: {type(variable).__name__}")
# #change variable to a dictionary
# variable = {"name": "John", "age": 30}
# print(f"variable is of type: {type(variable).__name__}")
# #change the variable to a boolean
# variable = True
# print(f"variable is of type: {type(variable).__name__}")
# item 1
item1_name = "Laptop"
item1_quantity = 2
item1_price = 1200.00
#item 2
item2_name = "Smartphone"
item2_quantity = 3
item2_price = 600.00
# #calculate the total cost
total_cost = (item1_quantity * item1_price + item2_quantity * item2_price)
# print(f"Item 1: {item1_name} (Quantity: {item1_quantity}, Price: ${item1_price:.2f} each)")
# print(f"Total Cost: ${total_cost:.2f}")
#create a formatted receipt
# receipt = f"receipt for your purchase:\n\n"
# receipt += f"Item 1: {item1_name} x{item1_quantity}\t${item1_quantity * item1_price:.2f}\n"
# receipt += f"Item 1: {item2_name} x{item2_quantity}\t${item2_quantity * item2_price:.2f}\n"
# receipt += f"----------------------------------------\n"
# receipt += f"Total Cost\t\t${total_cost:.2f}\n"
# print(receipt)
#sample article
import datetime
#sample article data
# article_data = [
#     {
#         "title": "Python for the beginners",
#         "author": "Alice",
#         "content": "Python is a versatile and beginner-friendly programming language.",
#     },
#     {
#         "title": "Data Science with Python",
#         "author": "Bob",
#         "content": "Python is widely used for data analysis and machine learning.",
#     },
# ]
# #built-in functions example
# for article in article_data:
#     #calculate the word count
#     content = article["content"]
#     word_count = len(content.split())
#     #format the publication date
#     publication_date = datetime.date.today()
#     #display article information
#     print(f"Title: {article['title']}")
#     print(f"Author: {article['author']}")
#     print(f"Word Count: {word_count}")
#     print(f"Publication Date: {publication_date}")