import json

def handler(event, context):
  print('received event:')
  print(event)

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)