"""An example of for in syntax."""

names: list[str] = ["Suzanne", "Christine", "Marissa", "angela", "Yuki"]

# Example with while loop 
print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1 

# now a for in loop equal to above while loop 
print("for output:")
for name in names:
    print(name)