
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

