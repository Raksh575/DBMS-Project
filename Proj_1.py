import os

file_name = "example.txt"  # Specify the file name

# Check if the file exists
if os.path.exists(file_name):
    # File exists, read and print its content
    with open(file_name, 'r') as file:
        content = file.read()
    print("File exists")
    print("File content:")
    print(content)
else:
    # If the file doesn't exist, create it and write "Hello, World!"
    with open(file_name, 'w') as file:
        file.write("Hello, World!")
    print(f"File {file_name} created with content: 'Hello, World!'")

# Print the list of all files and directories in the current working directory
print("\nList of files and directories in the current working directory:")
for item in os.listdir():
    print(item)
