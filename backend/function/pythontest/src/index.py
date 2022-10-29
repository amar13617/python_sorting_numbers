import json

def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data")
  operation = event.get("operation")
  if operation == "find_odd_even":
    return find_odd_even(list1)
  elif operation == "find_average":
    return find_average(list1)
  else:
    return {
    }

def find_odd_even(data):
  even_list = []
  odd_list1 = []
  for i in data:
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list1.append(i)
    
  return {
    "odd_Numbers" : odd_list1,
    "even_Numbers" : even_list
  }

def find_average(data):
  average = sum(data)/max(len(data),1)
    
  return {
      "average" : average
  }

  