# Write to the file
with open('data.txt', 'w') as file:
    file.write('Hello World\n')
    file.write('This is a test file.\n')
    file.write('Python is great!\n')

# Read what was written
with open('data.txt', 'r') as file:
    content = file.read()
    print("Initial content:")
    print(content)

# Append to the file
with open('data.txt', 'a') as file:
    file.write('Appending a new line.\n')
    file.write('This is the appended line.\n')

# Read again after appending
with open('data.txt', 'r') as file:
    content_2 = file.read()
    print("After appending:")
    print(content_2)

