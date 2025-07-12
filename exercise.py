# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

#Output: Before: 100 100 483096446336 483096446336

# Observations:
# 1. For integers, modifying the value creates a new object, hence the id changes   

a += 1
print("After a += 1:", a, b, id(a), id(b))

#Output: After a += 1: 101 100 483096446368 483096446336

# Observations:
#2. For lists, modifying the content does not create a new object, hence the id remains the same

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

#Output: Before: [1, 2, 3] [1, 2, 3] 480869360512 480869360512

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))

#Output: After x.append(4): [1, 2, 3, 4] [1, 2, 3, 4] 480869360512 480869360512





#Tasks:

    #Predict: What will the id values tell us for a vs. b, and for x vs. y?
    #id values of a vs b are the same because b is a reference to a, so they point to the same object in memory because integers are immutable.
    #id values of x vs y will be the same before and after the append operation because x and y are references to the same list object because lists are mutable.

    #Run the code and verify your predictions.

    #Answer in comments:
        #Why did id(a) change but id(x) did not?
# The id(a) changed because integers are immutable, so when we modified a, it created a new integer object.
        #The id(x) did not change because lists are mutable, so when we modified x, it changed the content of the same list object without creating a new one.
        #What does this say about integers vs. lists in Python?
# Integers are immutable, meaning any change creates a new object, while lists are mutable, allowing in-place modifications without changing the object's identity.


# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: Upper‑case each name and store in new list
upper_names = [] #initialize an empty list
for n in names:  # iterate through each name in names
    # Convert each name to upper case and append to upper_names
    upper_names.append(n.upper())

print(upper_names)

#Output: ['ALICE', 'BOB', 'CHARLIE', 'DANA']

# Task B: Use enumerate to print index + 1 alongside name
# Expected output:
# 1. Alice
# 2. Bob
# ...
# Print each name with its index + 1
for idx, name in enumerate(upper_names, start=1):
    print(f"{idx}. {name}")

#Output: 
1. ALICE
2. BOB
3. CHARLIE
4. DANA


# Task C: Demonstrate at least two list methods (e.g., insert, pop, remove, sort)
#   1. Insert a new name at position 2
names.insert(1, "eve")
print("After insert:", names)

#Output: After insert: ['alice', 'eve', 'bob', 'charlie', 'dana']

#   2. Remove "charlie"
names.remove("charlie")
print("After remove:", names)

#Output: After remove: ['alice', 'eve', 'bob', 'dana']

#   3. Sort the list
names.sort()
print("After sort:", names)
# Print the list after each operation.

#Output: After sort: ['alice', 'bob', 'dana', 'eve']


#Discuss: What’s the difference between modifying names vs. creating a new list?
# Modifying the original list changes its content directly while creating a new list keeps the original intact and allows for two separate version.