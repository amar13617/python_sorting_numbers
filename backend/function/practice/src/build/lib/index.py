import json

def handler(event, context):
  print('received event:')
  print(event)
  
def find_sort(data):
    sort_number = []
    for i in sorted(data):
        sort_number.append(i)
    return {
        "sorted_number" : sort_number
    }