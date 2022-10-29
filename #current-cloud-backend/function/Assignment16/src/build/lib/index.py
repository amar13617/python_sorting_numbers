import json
import datetime

def handler(event, context):
  currentDT = datetime.datetime.now()
  
  return {
      'statusCode': 200,
      'body': json.dumps(str(currentDT))
  }