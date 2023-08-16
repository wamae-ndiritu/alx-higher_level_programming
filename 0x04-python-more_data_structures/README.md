# Data Structures: Set, Dictionary

[0. Squared simple](./0-square_matrix_simple.py)

Write a function that computes the square value of all integers of a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
	- Same size as `matrix`
	- Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, `map`, etc.


[1. Search and replace](./1-search_replace.py)

Write a function that replaces all occurrences of an element by another in a new list.

- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- You are not allowed to import any module


### Key Take Aways

> When you pass a variable to a function the function is able to modify the variable completely.
> If for example you have a list and you pass it as an argument to the function `replace_at_0` as defined below, then the variable would be modified completely

	```
	def replace_at_0(my_List=[]):
		my_list[0] = 20
		return my_list
	```

> Let's define `my_list` and invoke the above function:

	```
	my_list = [1, 2, 3]
	new_list = replace_at_0(my_list)
	print(new_list)
	print(my_List)
	```

> The output will be as follows:

	```
	[20, 2, 3]
	[20, 2, 3]
	```
> This shows that `my_list` was modified directly inside the function `replace_at_0`. To prevent this since you would want to keep the original copy of the list, you could copy the list to a `new_list` inside the function and modify the copy instead of the original one.

	```
	def replace_at_0(my_list=[]):
	new_list = my_list[:] # copies all values of my_list to new_list
	new_list[0] = 20
	return new_list
	```
