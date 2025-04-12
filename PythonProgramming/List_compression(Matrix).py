#nested list comprehension
matrix = [[i*j for j in range (1, 4)] for i in range(1, 4)]
print(matrix)
# list comprehension
list =[i**3 for i in range(1, 10) if i%2==0]
print(f" The cubes for the numbers are {list}")