## Raising Exception

try:
  raise NameError('Hi there')
except NameError:
  print('An Exception')
  raise


try:
    amount = 1999
    if amount < 2999:
          
        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")
              
# if false then raise the value error
except ValueError as e:
        print(e)

