# functions can be used to store data in more maintained and reusable chunks
#  functions are declared using a def key word which stands for define
# a function is called for execution using then name of the function

def greetings():
    print("Hi there")
    print("welcome abroad")

greetings()

# a parameter is input that you define for a function while 
# an argument is the actual value for a given 
# formatted string

def greeting(first_name, last_name):
     print(f"Hi there {first_name},{last_name}")
     print("welcome abroad")

greeting("Cynthia","Ishimwe")

# 2 types of functions in python

# functions that performs a tasks and functions that calculates and returns a value

# round(function that calculates and returns a value)
# we use a return statement to return a value from the function
# in python all values none is an object that represents the absence of a value

# operations

def increment(number,by):
     return number + by

output = increment(2, 1)
print(output)

# we use keyword arguments to make our codes more readable
def increment(number,by):
     return number + by

print(increment(2, by=1))


def multiply(x, y):
     return x * y

print(multiply(2, 3))


# we can also perform operations through looping

def multiply(*numbers):
     num = 1
     for number in numbers:
          num = num * number
     return num
      
print(multiply(1,2,3,))

# positional arguments
def sum_multiplication(sum,multiplication):
     return(f"the sum of 2 and 6 is {sum} and their product is {multiplication}")

print(sum_multiplication(6+2,6*2))



# def sum_multiplication(sum,multiplication):

# default arguments
def names(firstname="a",secondname="b"):
     return(f"my name is {firstname} {secondname}")
print(names())
print(names("cynthia"))
print(names("cynthia","ishimwe"))
print(names(secondname="cynthia",firstname="ishimwe"))

# args-positional arguments
def classmates(*names):
    
     for name in names:
         print(name)
  
classmates("Veronica","Mary","Marget","Amakove","Marion","Rebecca")

# reverse
person = "james bond"
print(person[::-1])
person2 = "cynthia"
print(person2[::-1])

student = "Rebecca"
print(student[-2::-2])

course = "programming"
print(len(course))
print(course[0])
# slice this prints a new index that returns the first three index but only 2 elements 
print(course[0:4])
# prints out the whole string since there is no specific end slice
print(course[0:])
# this returns a copy of the original string
print(course[0:])



# adds two elements
print(10+3)
# substracts 
print(10-3)
# divides elements
print(10/2)
# divided elements and removes floats
print(10//3)
# divides elements and returns the remainder
print(10%3)
# exponents elements returns the elements to the power of what is passed to it
print(10**3)
# comparison operators are used to compare values
print(10<3)
print(10 >= 3)
print(10 == 10)
print(10 == "10")
print(10 != "10")