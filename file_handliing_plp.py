# File Read & Write Challenge with Error Handling

# Ask the user for a filename
filename = input("Enter the name of the file to read: ")

try:
    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"File processed successfully! Modified file saved as '{new_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
