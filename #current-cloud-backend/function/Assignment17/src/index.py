import json

def handler(event, context):
    print(event)
    
    list1 = [10, 21,4,45,66,93]
    a = "hello world"
    print(a)

    for num in list1:
        if num % 2 == 0:
            return(num, end = " ")
