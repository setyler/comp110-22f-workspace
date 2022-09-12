"""Examples of using lists in a simple 'game'."""


from random import randint 


rolls: list[int] = list()
# "list of ints"
# lift[T] = list of type T
# = list() to assign an empty list 

rolls.append(1) 
# method call: calling a function specifically on a given item (in this call rolls)
# lists are ordered sequences, appended items are added directly on the end 
# rolls.append(expr[T]) adds an item to the end of a list 

rolls.append(randint(1, 6))
rolls.append(randint(1,6))

# accessing individual items 

print(rolls)