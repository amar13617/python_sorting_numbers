import json
#find created by Amar

def find_sort(data):
  sort_numbers = []
  for i in sorted(data):
    sort_numbers.append(i)
  return{
    "sort_number": sort_numbers
  }
  
def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data")
  operation = event.get("operation")
  n = 8
  if operation == "find_sort":
    return find_sort(list1)
  elif operation == "binary":
    return binary_search(list1, n)
  else:
    return {

    }
def binary_search(data, n):
  low = 0
  high = len(data)-1
  mid = 0
  while low <= high:
    mid = (high + low)//2

    if data[mid] < n:
      low = mid + 1
    elif data[mid] > n:
      high = mid - 1
    else:
      return mid
  
  return -1


  