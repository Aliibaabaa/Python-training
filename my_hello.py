#basic syntax

print ('Hello world!')

'''
VARIABLES and DATA TYPES
    integers -- whole numbers
    floats -- decimal numbers
    string -- text (single quote = ; double quote = usually used if there are apostrophes )
    booleans -- true/false
 '''
 
#int
number = 10

#float
decimal = 9.3

#string
word = 'sample string'

#boolean
bool_true = True
bool_false = False

print (word)
print (number , decimal)
print ('This is a ' + word)

 #formatted-strings (f-string) lets you put variables in the string using braces ({});
 # a way to read the variable; similar to backticks in js
print(f'This is a {word}')


def test_function(): #def means define, it would mean define a function (def <function_name>)
    print('This is a test function')

test_function()