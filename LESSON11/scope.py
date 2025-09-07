name = "Dave"
count = 1

def another_function():
    color = "blue"
    
    def greeting(name): 
        print(color)
        count = 5
        print(count)
        print(name + ", welcome to Python programming!")
    
    greeting("Alice")  # Call the function here

another_function()