"""
Lists practices
for python
chapter 6 in TAU.

What are lists?
- collection of data 
- can contain any/all data types in a single list
- can contain other collections (lists, dictionaries, tuples) as a list items
- mutable (items can be added, removed, changed)
- maintain order (can use index to find an item)

"""

fruits = ["peaches", "pears", "apples", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]


#check membership 
print("apple" in fruits)
print("apples" in fruits)

#to count how many items in the list
print(fruits.count("apples"))
print(fruits.count("apple"))
'''
print(fruits,years)

#adding a new item in the list
fruits.append("oranges")
print(fruits)

#adding multiple item using list extend
fruits.extend(years)
print(fruits)

#method removing items in a list
fruits.remove("oranges")
print(fruits)

#removing by using index, python list starts from 0
fruits.pop(0)
print(fruits)

#removing by using the concept negative indexing
fruits.pop(-1)
print(fruits)

#sort method can only be used with alike items like all int
numbers = [5,1928,4,17,68]
numbers.sort()
print(numbers)
'''