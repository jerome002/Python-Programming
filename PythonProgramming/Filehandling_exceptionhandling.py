
def modify_line(line):
    # modification: reverse each line
    return line[::-1]

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Modify each line
        modified_lines = [modify_line(line.strip()) + '\n' for line in lines]

        # Write to a new file
        with open("modified_output.txt", 'w') as output_file:
            output_file.writelines(modified_lines)

        print(" File was read and modified_output.txt has been created successfully!")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read. Please check permissions or file status.")

if __name__ == "__main__":
    main()
