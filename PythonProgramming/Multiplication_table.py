
# Multiplication table from 1 to 5
for i in range(1, 6):  # Outer loop: 1 to 5
    for j in range(1, 6):  # Inner loop: 1 to 5
        print(f"{i} x {j} = {i * j}")
    print()  # Print a blank line after each row for better formatting
