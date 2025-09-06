# function are resuable blocks of code
def greet(name):
    print("Hello " + name)
    print("Welcome to Python programming!")
greet("Alice")
greet("Bob")
greet("Cathy")

def sum(num1, num2=3):
    if type(num1) is not int or type(num2) is not int:
        # return "Both arguments must be integers."
        return
    return num1 + num2
    
    
total = sum(3)
print(total)
# print(sum(1, 7))
# print(sum(100, 3))
# sum(2, 3)
# sum(1, 7)
# sum(100, 3)

def multiple_items(*args):
        print(args)
        print(type(args))


multiple_items("Alice", "Bob", "Cathy")

def mult_named_args(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_args(name="Alice", age=30, city="New York")
mult_named_args(fruit="Apple", vegetable="Carrot")
mult_named_args(country="USA", language="English", population=330000000)