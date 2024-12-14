def read_and_modify_file():
    filename = input("Enter the filename to read: ")
    try:
        # Read the original file
        with open(filename, "r") as file:
            content = file.read()
            print("File content read successfully.")
            
        # Modify content (example: make uppercase)
        modified_content = content.upper()
        
        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to {new_filename}.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write the file '{filename}'.")

# Run the program
read_and_modify_file()

