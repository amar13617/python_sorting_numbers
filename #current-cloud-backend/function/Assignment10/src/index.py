import json

def handler(event, context):
  print('received event:')
  print(event)
  
  return {
      'statusCode': 200,
      'body': json.dumps('message = 'Hello {} {}!'.format(event['first_name'], event['last_name'] 
    return { 
        'message' : message
    }')
  }