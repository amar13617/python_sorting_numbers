import json

def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data")
  operation = event.get("operation")
  if operation == "find_sort":
    return find_sort(list1)
  else:
    return {
        
    }
def find_sort(data):
    sort_number = []
    for i in sorted(data):
        sort_number.append(i)
    return {
        "sort_number" : sort_number
    }
