"""Notes and examplesof tuple and range sequence types"""

# declaring a type alias that 'invents' the point2d type
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)

print(start_position)

# examples of ranges 
a_range: range = range(0, 10, 3)
# access items 
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)

another_range: range = range(0, 10)
# default step is 1 

# only one argument, it specifies the stop marker and start is 0 by default 

zero_start: range = range(10)
for x in zero_start:
    print(x)

names: list[str] = ["Kris", "Alyssa", "Ben", "arnold"]

for name in names:
    print(name)

# range is often used to write for loops where iteration pattern is not consecutive
for i in range(0, len(names), 2):
    print(names[i])