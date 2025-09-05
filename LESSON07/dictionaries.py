# Dictionaries

band = {
    'name': 'The Beatles',
    'guitarist': 'George Harrison',
    'drummer': 'Ringo Starr',
}

band2 = dict(name='The Beatles', guitarist='George Harrison', drummer='Ringo Starr')
print(band)
print(band2)
print(type(band))
print(len(band))


# Access items

print(band['name'])
print(band.get('guitarist'))


# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key and value pairs as tuples
print(band.items())

# verify a key exists
print('name' in band)
print('bass' in band)

# change values
band['drummer'] = 'Pete Best'
band.update({'drummer': 'Ringo Starr'})
print(band)

#Remove items
print(band.pop('guitarist'))
print(band)

band["drummer"] = 'Ringo Starr'
print(band)

# tuples are immutable lists
print(band.popitem())
print(band)

# Delete and clear
band['drummer'] = 'Ringo Starr'
del band['drummer']
print(band)

band2.clear()
print(band2)

del band2

# Copy a dictionary
# band2 = band # create a reference to band
# print("Bad copy")
# print(band2)
# print(band)

# band2['name'] = 'The Rolling Stones'
# print(band)

band2 = band.copy()  # creates a shallow copy of band
band2["drummer"] = 'Charlie Watts'  # modifies band2 only
print("Good copy")
print(band)
print(band2)

# Or Using dict() constructor function to create a copy
band3 = dict(band)
print("Another good copy")
print(band3)

# Nested dictionaries
member1 = {
    'name': 'John Lennon',
    'role': 'rhythm guitar, vocals'
}

member2 = {
    'name': 'Paul McCartney',
    'role': 'bass, vocals'
}


band = {
    "memeber1": member1,
    "member2": member2
}

print(band)
print(band['memeber1']['name'])


# Sets 
nums = {1, 2, 3, 4, 5}
nums2 = set((4, 5, 6, 7, 8))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate values allowed
nums = {1, 2, 2, 3, 4, 4, 5}
print(nums)

# True is a dupete of 1, False is a duplicate of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in the set
print(3 in nums)


# but you cannot refer to an element in the set with an index position or a key



# add a new element to a set
nums.add(8)
print(nums) 

# Add elements from another set or list
morenums = {7, 8, 9}
nums.update(morenums)
print(nums)

# you can use update with list, tuples, and disctionaries, too


# Merge two sets to create a new set
one = {1, 2, 3}
two = {3, 4, 5}

mynewset = one.union(two)
print(mynewset)