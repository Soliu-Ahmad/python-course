users = ['David', 'Alice', 'Bob', 'Cathy']
data = ['David', 20, 30, 40, True]
empty = []
print('David' in empty)
print(users[0])
print(users[-2])

print(users.index('Bob'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Eva')
print(users)

users += ['Frank', 'Grace']
print(users)

users.extend(['Hank', 'Ivy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Zoe')
print(users)

users[2:2] = ['Jack', 'Kathy']
print(users)

users[1:3] = ['Liam', 'Mia']
print(users)

users.remove('Cathy')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)


# empty brackets [] means list in python
data.clear()
print(data)  

users[1:2] = ["David"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

numbers = [5, 3, 8, 1, 4]
numbers.reverse()
print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

print(sorted(numbers, reverse=True))
print(numbers)

numberscopy = numbers.copy()
mynumbers = list(numbers)
mycopy = numbers[:]

print(numberscopy)
print(mynumbers)
mycopy.sort()
print(mycopy)
print(numbers)

print(type(numbers))

mylist = list([1, "New York", True])
print(mylist)


#Tuple

mytupe = tuple(('Alice', 4, False))

anothertuple = (1,2,3,4, 2, 2)

print(mytupe)
print(type(mytupe))
print(type(anothertuple))

newtlist = list(mytupe)
newtlist.append('Bob')
newtuple = tuple(newtlist)
print(newtuple)

(one, two, three, four, *rest) = anothertuple
print(one)
print(three)
print(four)

print(anothertuple.count(2))