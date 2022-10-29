import json

def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data1")
  list2 = event.get("data2")
  operation = event.get("operation")
  if operation == "find_odd_even":
    return find_odd_even(list1)
  elif operation == "find_average":
    return find_average(list1)
  elif operation == "find_prime":
    return find_prime(list1)
  elif operation == "find_square":
    return find_square(list1)
  elif operation == "find_sum":
    return find_sum(list1)
  elif operation == "find_multiply":
    return find_multiply(list1)
  elif operation == "find_maximum":
    return find_maximum(list1)
  elif operation == "find_minimum":
    return find_minimum(list1)
  elif operation == "find_uneven":
    return find_uneven(list1)
  elif operation == "find_primes":
    return find_primes(list1)
  elif operation == "join_list":
    return do_join_list(list1,list2)
  elif operation == "remove_list":
    return do_remove_list(list1, list2)
  elif operation == "multiply_list":
    return do_multiply_list(list1, list2)
  elif operation == "divide_list":
    return do_divide_list(list1, list2)
  elif operation == "largest_number":
    return find_largest_number(list1)
  elif operation == "smallest_number":
    return find_smallest_number(list2)
  elif operation == "second_largest":
    return find_second_largest(list1)
  else:
    return {
    }
def find_odd_even(data):
  even_list = []
  odd_list = []
  for i in data:
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  return {
    "even_numbers" : even_list,
    "odd_numbers" :  odd_list
  }

def find_average(data):
  average = sum(data)/max(len(data),1)
  return{
    "average" : average
}

def find_prime(data):
  prime_list = []
  for i in data:
    c = 0
    for j in range(1,i):
      if i % j == 0:
        c +=1
    if c == 1:
      prime_list.append(i)
  return{
    "prime_number" : prime_list
  }

def find_square(data):
  find_square = []
  for i in data:
    find_square.append(i*i)
  return {
      "find_square" : find_square
  }

def find_sum(data):
  sum_list = 0
  for i in data:
    sum_list += i
  
  return {
    "find_sum" : sum_list
  }

def find_multiply(data):
  multiply_list = 1
  for i in data:
    multiply_list *= i
  return {
    "multiply_list" : multiply_list
  }

def find_maximum(data):
  max = data[0]
  for i in data:
    if i > max:
      max = i
  return {
    "find_maximum" : max
  }

def find_minimum(data):
  min = data[0]
  for i in data:
    if i < min:
      min = i
  return {
    "find_minimum" : min
  }
  
def find_uneven(data):
  find_uneven = []
  for i in data:
    if i %2 != 0:
      find_uneven.append(i)
  return {
    "find_uneven" : find_uneven
  }

def find_primes(data):
  prime_lists = []
  for i in data:
    if is_primes(i):
      prime_lists.append(i)
  return {
    "prime_numbers" : prime_lists
  }

def is_primes(data):
  if data < 2:
    return False
  if data == 2:
    return True
  for i in range(2, data//2):
    if (data%i)== 0:
      return False
  return True
  
def do_join_list(data1, data2):
  new_list = []
  for i in range(0, len(data1)):
    new_list.append(data1[i] + data2[i])
  return {
    "Adding two list" : new_list
  }

def do_remove_list(data1, data2):
  new_lists = []
  for i in range(0, len(data1)):
    new_lists.append(data1[i] - data2[i])
  return {
    "Substract two list" : new_lists
  }  


def do_multiply_list(data1, data2):
  newList = []
  for i in range(0, len(data1)):
    newList.append(data1[i] * data2[i])
  return {
    "Multiply two list" : newList
  }  

def do_divide_list(data1, data2):
  newLists = []
  for i in range(0, len(data1)):
    newLists.append(data1[i] / data2[i])
  return {
    "Divide two list" : newLists
  }  

def find_largest_number(data1):
  largest_number = data1[0]

  for i in data1:
    if i > largest_number:
      largest_number = i
  return {
    "largest_number" : largest_number
  }

def find_smallest_number(data2):
  smallest_numbers = data2[0]

  for i in data2:
    if i < smallest_numbers:
      smallest_numbers = i
  return {
    "smallest_number" : smallest_numbers
  }  

def find_second_largest(data1):
  secondLargest = 0
  largest = min(data1)

  for i in range(len(data1)):
    if data1[i] > largest:
      secondLargest = largest
      largest = data1[i]
    else:
      secondLargest = max(secondLargest, data1[i])
  return {
    "second largest" : secondLargest
  }

