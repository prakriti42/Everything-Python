#Prints duplicates present in a list
_list = [1,2,3,4,5,5,6,7,7,7,7,7,7,7,7,7]
_listtwo=[]
for data in _list:
	if _list.count(data) > 1:
		if data not in _listtwo:
			_listtwo.append(data)
print(_listtwo)
#--------------------------------------------------------------------
#Detecting if a word is palindrome.
word = (input("Enter a word.\t")).lower()
reverse = word[::-1]
print("Your input is a palindrome" if word == reverse else "Your input is not a palindrome")
#-----------------------------------------------------------------------
#Dictonary in Python. 
details = {
					 1:{"username":"purplebubbles","password":"Iamgroot"},
					 2:{"username":"sickpea","password":"senorita"},
			}
for key,value in enumerate(details.items()):
	for i in key,value:
		if i== 0: 
			print(details)
#-----------------------------------------------------------------------
#Functions
def say_hi(name="anonymous" , pronoun="not determined for now"):    #default parameters 
	print(f'Hi , {name}.We have set your pronoun as {pronoun}.')
say_hi(name="Prakriti",pronoun="she/her")   #keyword arguments
say_hi(pronoun="he/him",name="Robert")
say_hi()
#----------------------------------------------------------
def power(x,y):
	return x ** y
result = power(2,2)
print(power(result , power(2,2)))
#----------------------------------------------------------------
#Example of a class
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Instantiation of objects of the specific class
cat1 = Cat("meowcha", 10)
cat2 = Cat("tagasi",9)
cat3 = Cat("mona",13)
#a function that finds the oldest cat
def OldestCat(*arguments):
	return max(arguments)
print(f"The oldest cat is {OldestCat(cat1.age,cat2.age,cat3.age)} years old")
#---------------------------------------------------------------------------------
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
		#Example of a class method.
    @classmethod
    def CalculateAge(cls, birthyear):
        return cls('name', abs(birthyear-2020))
animal1 = Animal.CalculateAge(2019)
print(animal1.age)
#------------------------------------------------------------------------------
#Example of inheritance in Python
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Suzy(Cat):
    def sing(self, sounds):
        return f'{sounds}'
#Creating a list of all pets
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]
#Instantiation of the Pet class with all the cats
my_pets = Pets(my_cats)
#Output all of the cats singing using the my_pets instance
my_pets.walk()
#-------------------------------------------------------------------------------------------------------------
def add2(num):
    return num + 2
num = [1,2,3,4,5]
result = map(add2,num)  # map  function
print(list(result))
#-------------------------------------------------------------------------------
#lambda expression : A shorthand for non-reuseable functions
x = lambda x,y,z: print(f"The result is {x+y+z}") 
x(5,5,5)
#-------------------------------------------------------------------------------
my_list = [ x for x in 'purple']  #list comprehension
print(my_list) 
my_list = [ x.upper() for x in 'purple']  #list comprehension with manipulation
print(my_list)
li = [x**2 for x in range(0,10) if x % 2 == 0]   #list comprehension with condition
print(li)      
#-------------------------------------------------------------------------------
my_set = {x for x in 'purple'}  #sets comprehension
print(my_set)
#-----------------------------------------------------------------------
dict1= {
    'a':1,
    'b':2
}
my_dict = {k:v ** 2 for k , v in dict1.items()}  #dictionary comprehension
print(my_dict)
#------------------------------------------------------------------
#removing duplicates from a list way 2
some_list = ['a','b','c','b','d','m','n','n']
dup = set([ x for x  in some_list if (some_list.count(x) > 1)])
print(dup)
#-------------------------------------
def sayHi(name):
    print("Hello {}".format(name))
greet = sayHi   #interchanging function names
del sayHi
greet("purple")
#--------------------------------------------
#Decorater 
def decorator1(func):
    def wrapper():
        print('****************')
        func()
        print("***************")
    return wrapper

@decorator1
def hi():
    print(f"Hola!")

hi()
#---------------------------------------
def decorator1(fun1):
    def wrapper(name):
        print('****************')
        fun1(name)
        print("***************")
    return wrapper

@decorator1
def hi(name):    #passing arguments through decoraters 
    print("Hola!"+ name)

hi("P")
#-------------------------------------------------
#A performance decorater to test the execution time of a function.
from time import time
def timeTaken(func):
    def wrap():
        T1 = time()
        func()
        T2 = time()
        print(f"The execution time of the function was :{T2-T1}s")
    return wrap

@timeTaken
def sum():
    '''A function to print the sum of first 100 natural numbers.'''
    res = 0
    for i in range(1000000):
        res = res + i
    print(f"Sum = {res}") 

sum()
#-----------------------------------------------------------------
#Error handling 
while True:
    try:
        age = int(input("What is your age?\t"))
        10/age
    except ValueError:
        print("Age must be a number.")
    except ZeroDivisionError:
        print("Age cannot be zero")
    else:
        print('Age stored.Thank you!')
        break
#------------------------------------------------------------------
#Error handling by displaying the error 
while True:
    try:
        age = int(input("What is your age?\t"))
        10/age
    except (ValueError,ZeroDivisionError) as error:
        print(error)
    else:
        print('Age stored.Thank you!')
        break
#----------------------------------------------------
#raising an error
#Error handling 

try:
    age = int(input("What is your age?\t")) 
except (ValueError,ZeroDivisionError):
    raise ValueError("Input a number")
    raise ZeroDivisionError("Age cannot be zero")
#----------------------------------------------------------
#Fibonacci Series using generator 
def fib(number):
     a = 1 
     b = 1
     for i in range(number):
        yield a 
        temp = a 
        a = b
        b = temp + b
for x in fib(5):
    print(x , end = " ")
#-----------------------------------------------------------