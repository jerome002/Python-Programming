
with open("input.txt", "w") as file:
    file.write("Hello World\n")
    file.write("I am learning Python.\n")
    file.write("Python is great!\n")
    file.write("Python for web dev\n")
    file.write("Python for data science\n")
    file.write("Python for machine learning\n")
    file.write("Python for data analysis\n")
    file.write("Python for automation\n")
    file.write("Python for scripting\n")
    file.write("Python for testing\n")
    file.write("Python for web scraping\n")
    file.write("Python for game development\n")
    file.write("Python for GUI development\n")
    file.write("Python for mobile development\n")
    file.write("Python for cloud computing\n")
    file.write("Python for IoT\n")
    file.write("Python for cybersecurity\n")
    file.write("Python for data visualization\n")
    file.write("Python for big data\n")
    file.write("Python for blockchain\n")
    file.write("Python for quantum computing\n")
    file.write("Python for edge computing\n")
    file.write("Python for augmented reality\n")
    file.write("Python for virtual reality\n")
    file.write("Python for 3D printing\n")
    file.write("Python for robotics\n")
    file.write("Python for natural language processing\n")
    file.write("Python for computer vision\n")
    file.write("Python for speech recognition\n")
    file.write("Python for image processing\n")
    file.write("Python for audio processing\n")
    file.write("Python for video processing\n")
    file.write("Python for data mining\n")
    file.write("Python for data warehousing\n")
    
    # process_text.py

# Step 1: Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 2: Count the number of words
words = content.split()
word_count = len(words)

# Step 3: Convert text to uppercase
uppercase_content = content.upper()

# Step 4: Write to output.txt
with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(uppercase_content + "\n")
    file.write(f"\nWORD COUNT: {word_count}\n")

# Step 5: Print success message
print("✅ output.txt created successfully!")
# Step 6: Read and print the contents of output.txt
with open("output.txt", "r") as file:
    output_content = file.read()
    print(output_content)