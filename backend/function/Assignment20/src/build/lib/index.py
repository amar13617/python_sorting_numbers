import json

def handler(event, context):
  print('received event:')
  print(event)
  
  return {
      'statusCode': 200,
      
      'body': json.dumps('Hello from Amar Kumar')
  }