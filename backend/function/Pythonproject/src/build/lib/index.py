import json

def handler(event, context):
  print('received event:')
  print(event)
  
def factorial(x):
    if x == 1:
        return 1
    else:
        
        return (x * factorial(x-1))
num = 7
result = factorial(num)
print("The factorial of", num, "is", result)