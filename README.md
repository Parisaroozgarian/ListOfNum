# List Manipulation Program

This Python program demonstrates basic list manipulation operations, including changing an element, removing an element, and adding elements to another list. The program is encapsulated in a class mylist, which provides various methods to interact with the list.

## Features
- Initialization: Create a list of specified size, initialized with zeros.
- Change Element: Replace an element at a specific index with another value.
- Show List: Display the current state of the list.
- Append Element: Add a new element to the end of the list.
- Delete Element: Remove an element at a specific index from the list.
- Add Lists: Add elements of two lists of the same size and return a new list with the result.

## Class: mylist
### Methods
- __init__(self, n): Initializes the list with n elements, all set to 0.
- changesize(self): Updates the size attribute to reflect the current list size.
- set(self, n, x): Sets the element at index n to x.
- show(self): Prints the current list.
- append(self, x): Appends x to the list and updates the size.
- delete(self, i): Deletes the element at index i and updates the size.
- add(self, m2): Returns a new list that is the element-wise sum of the current list and another list m2.


## Example Usage

python
Copy code
# Create an instance of mylist with 5 elements
A = mylist(5)

# Set elements at specific indices
A.set(2, 7)
A.set(3, 8)

print('A:')
print(type(A))

print('B:')
B = mylist(5)
print(type(B))
B.set(2, 7)
B.set(4, 8)
B.show()

print('C:')
C = A.add(B)
print(type(C))
C.show()


## Explanation
1. Initialization: Create two lists, A and B, each with 5 elements.
2. Set Elements: Modify specific elements in both lists.
3. Show List: Display the contents of list B.
4. Add Lists: Create a new list C by adding corresponding elements of A and B.
5. Display Result: Show the contents of the resultant list C.
