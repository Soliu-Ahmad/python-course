# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1  # value = value + 1


value = 1
while value <= 10:
    value += 1 # value = value + 1
    if value == 5:
        continue
    print(value)
else:
    print("the loop is done"  +  str(value))

names = ['Alice', 'Bob', 'Cathy']
for name in names:
    print(name)

for x in "hello":
    print(x)


for i in names:
    if i == 'Bob':
        break
    print(i)
    
for i in names:
    if i == 'Bob':
        continue
    print(i)
    
for xx in range(4):  # start, stop, step
    print(xx)
    
# for xx in range(12):  # start, stop, step
#     print(xx)
for xx in range(5, 101, 5):  # start, stop, step
    print(xx)
else:
    print("Glad that\'s over!")
    
names = ['Alice', 'Bob', 'Cathy']
action = ['codes', 'eats', 'sleeps']

# for name in names:
#     for act in action:
#         print(name + " " + act + ".")
        
for name in names:
    for act in action:
        print(name + " " + act + ".")