def log_and_run(func):
    print("I just got {}".format(func.__name__))
    return func()


def log_and_return(func):
    print("I just got {}".format(func.__name__))
    return func()
  
@log_and_run
def say_hello():
  print('Hello')

@log_and_return
def say_hello():
  print('Hello')

#print('log and run:')
#log_and_run(say_hello)
#
#print('log and return')
#log_and_return(say_hello)