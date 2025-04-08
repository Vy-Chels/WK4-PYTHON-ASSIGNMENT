# File Read & Write with Error Handling

def read_and_modify_file():
    # Ask the user to enter the name of the file to read
    filename = input("Enter the name of the file to read (e.g., sample.txt): ")

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Create a new filename for the modified file
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        # Handle case where the file does not exist
        print("Error: The file you entered does not exist.")

    except IOError as e:
        # Handle other input/output errors
        print(f"Error: Could not read or write to the file.\nDetails: {e}")


# Call the function to execute the program
read_and_modify_file()