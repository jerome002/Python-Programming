
numbers = [1, 2, 3, 4, 5]
# Using a for loop to iterate through the list of numbers
for number in numbers:
    # Print the numbers
    print(" numbers:", number)
    # Check if the number is even
    if number % 2 == 0:
        # Skip even numbers
        print("Skipping even number:", number)
        # continue statement will skip the rest of the loop for this iteration
        continue
    # Print odd numbers
    print("Odd number:", number)
    # a nested loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")
