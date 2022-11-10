"""Examples of optional parameters and Union types."""


def hello(name: str = "World") -> str: 
    """A delightfull greeting."""
    greeting: str = "Hello, " + name
    return greeting 


# single argument 
print(hello("Sally"))

# no argument
print(hello())