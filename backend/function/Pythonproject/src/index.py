import json

def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data")
  operation = event.get("operation")
  if operation == "find_square":
    return find_square(list1)
  elif operation == "find_reverse":
    return find_reverse(list1)
  elif operation == "factorial_number":
    return factorial_number(list1)
  elif operation == "Fibonacci":
    return Fibonacci(list1)
  else:
    return {

    }
def find_square(data):
    res = []
    for i in data:
        res.append(i*i)
    
    return {
        "find_square" : res
    }

def find_reverse(data):
  reverse_number = []
  for i in reversed(data):
    reverse_number.append(i)
  
  return {
    "find_reverse" : reverse_number
  }

def factorial_number(data):
  if data == 1:
    return 1
  else:
    return (data * factorial_number(data-1))

def Fibonacci(data):
  if data == 0:
    return 0
  elif data ==1 or data ==2:
    return 1
  else:
    return Fibonacci(data-1) + Fibonacci(data-2)

  