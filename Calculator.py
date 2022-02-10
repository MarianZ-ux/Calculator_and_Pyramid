# Exercise #1
# Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs... Loop until the user chooses not to perform any more calculations.
# Hint: Take yesterday's code from the extra exercise...



print('Welcome to my basic calculator!')

num1 = int(input('Enter 1st integer'))
method = input('Input symbol(+, -, *, /):')
num2 = int(input('Enter 2nd integer'))

if (method == '+'):
    ans = num1 + num2
elif (method == '-'):
    ans = num1 - num2
elif (method == '*'):
    ans = num1 * num2
elif (method == '/'):
    ans = num1 / num2

ask = input('Would you like to quit? (y/n) ')
def input(ask):
    while ask == 'n':
        continue
    if ask == 'y':
        print('Have a fantabulous day')

print('Total =   ', ans)


# num = [0,1,2,3,4,5,6,7,8,9]
# product/, quotient*, diff-, result+
#         print(input=('Total cleared. Enter next integer':))
#         
# print(f('Your total = {ans}')