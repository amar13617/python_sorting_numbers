import json

def handler(event, context):
    print('received event:')
    print(event)

num1 = 15
num2 = 12
 
# Adding two nos
sum = num1 + num2
 
# printing values
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))