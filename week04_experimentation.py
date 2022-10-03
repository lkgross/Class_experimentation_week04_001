
military = ['army', 'navy', 'airforce', 'marines']
print(military)
# Use indexing to access an element in the list.
# Indexing (from the beginning of the list) starts with 0.
print(military[2])
# Indexing (from the end of the list) starts with -2.
print(military[-3])
print(military[-1])
print(military[-2])
# We can modify the element at index -2.
# We can overwrite the element with a new value.
military[-2] = 'air force'
print(military)
# Call the append method on the list to add a new element
# to the end.
military.append('national guard')
print(military)
# Let's start a new list that initially has nothing in it.
# It's an empty list.
mountains = []
print(mountains)
mountains.append('Mount Kilimanjaro')
print(mountains)
mountains.append('Mount Kenya')
print(mountains)
# Print the length of the list.
print(len(military))
print(len(mountains))
mountains.append('Mount Meru')
print(mountains)
# Remember to count from 0 rather than 1.
mountains.insert(2, 'Mount Stanley')
print(mountains)
# Use del to delete:
del mountains[-1]
print(mountains)
# Remove an item by its value rather than its index.
mountains.remove('Mount Stanley')
print(mountains)
print(f"The second tallest mountain in Africa is {mountains.pop()}.")
print(mountains)
mountains.append('Mount Kenya')
mountains.append('Mount Stanley')
mountains.append('Mount Meru')
print(mountains)
highest = mountains.pop(0)
print(f"The tallest mountain in Africa is {highest}.")
print(mountains)
mountains.append(highest)
print(mountains)
print(len(mountains))
heights = [5199, 5109, 5895, 4562]
# We can permanently sort heights from smallest to largest:
heights.sort()
print(heights)
# We can permanently sort heights from largest to smallest:
heights.reverse()
print(heights)
heights = [5199, 5109, 5895, 4562].reverse()
print(heights)
# The sorted() function returns a copy of the list,
# leaving the original list unchanged.
print(mountains)
print(sorted(mountains))
print(mountains)
# Here's a temporary reverse alphabetical order:
print(sorted(mountains, reverse = True))

print('These are the branches:')
for branch in military:
        print('One branch is:')
        print(branch)
print('Those are the branches.')
print()
print('These are the branches:')
for i in range(len(military)):
        print('One branch is:')
        print(military[i])
print('Those are the branches.')