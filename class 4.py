# #create 5 vegetable 

# vegetable = {'cabbage','tomatto','onion','carrot','garlic'}
# print(vegetable)

# # add new 

# fruits = {"apple" "banana", "cherry"}
# fruits.add("mango")
# print (fruits)

# # Use a loop to print each item in the set {"python", "java", "c++"}

# nn= {"python", "java", "c++"}
# for x in nn:
#     print(x)

# # Remove "dog" from the set {"dog", "cat", "rabbit"}.

# animal={"dog", "cat", "rabbit"}
# animal.remove("dog")
# print(animal)

# # Check if "cat" is in the set {"dog", "cat", "rabbit"}.

# animal={"dog", "cat", "rabbit"}
# print("cat" in animal)

# # Medium Exercises
# # Combine the sets {1, 2, 3} and {3, 4, 5} using union().
# a={1, 2, 3}
# b={3, 4, 5} 
# print (a|b)

# # Find the intersection of {1, 2, 3, 4} and {3, 4, 5, 6}.
# a={1, 2, 3,4}
# b={3, 4, 5,6} 
# print(a.intersection(b)) 

# # # Use the difference() method to find items in {1, 2, 3, 4} but not in {3, 4, 5, 6}.
# a={1, 2, 3, 4 }
# b={3, 4, 5, 6 } 
# print(a.difference(b))

# # Create a set of numbers from 1 to 5 and remove all items using clear().
# num={1,2,3,4,5}
# num.clear()
# print(num)

# # Write a program to find duplicates in a list using a set.
# def find_duplicates(input_list):
#     seen = set()  # To track elements we've seen
#     duplicates = set()  # To store duplicates

#     for item in input_list:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)

#     return list(duplicates)

# # Example usage
# input_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 3]
# duplicates = find_duplicates(input_list)
# print(f"Duplicate elements: {duplicates}")


# Hard Exercises
# Use a set to remove duplicate characters from a string.
# Input: "hello"
# Output: {'h', 'e', 'l', 'o'}
# Create two sets of student names and find the symmetric difference.
# Check if the set {1, 2} is a subset of {1, 2, 3}.
# Write a function that takes two sets and returns a new set with all unique elements from both sets.
# Create a program that counts the unique words in a sentence using a set.

# list = var 
# set  = let
# tuple = const


# # Create a tuple of five colors and print it.
# color = ("Green", "Yellow", "Red", "Blue", "orange")
# print(color)

# # Access the second and last item of a tuple.
# color = ("Green", "Yellow", "Red", "Blue", "orange")
# print(color[1])
# print(color[4])

# # Slice the tuple
# colors = ("red", "blue", "green", "yellow", "purple")
# middle_three = colors[1:4]

# # Check if "orange" exists
# exists = "orange" in ("red", "blue", "green")

# # Print all items in the tuple
# for fruit in ("apple", "banana", "cherry"):
#     print(fruit)

# #middle 

# # Merge two tuples
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# merged_tuple = tuple1 + tuple2

# # Count occurrences of an item in a tuple
# sample_tuple = (1, 2, 3, 2, 4, 2, 5)
# count = sample_tuple.count(2)

# # Extract numeric items from a tuple
# mixed_tuple = ("apple", 42, 3.14, "banana", 7)
# numeric_items = tuple(item for item in mixed_tuple if isinstance(item, (int, float)))

# # Find length of a tuple without len()
# sample_tuple = ("a", "b", "c", "d", "e")
# length = sum(1 for _ in sample_tuple)

# # Reverse a tuple using negative indexing
# original_tuple = (1, 2, 3, 4, 5)
# reversed_tuple = original_tuple[::-1]
