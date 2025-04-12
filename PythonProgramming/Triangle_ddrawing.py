
rows = int(input("Enter the number of rows: "))
# Drawing a pyramid using nested loops
# The outer loop iterates through the number of rows
if rows >= 6:
    for i in range(1, rows + 1):
    # Print leading spaces
     print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))


else:
# Drawing right triangle using nested loops
    for k in range(1, rows+1):
        for j in range(1, k+1):
            print("*", end=" ")
        print()