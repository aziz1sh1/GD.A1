file_to_open = 'GDsample 1.py'

try:
    with open(file_to_open, 'r') as file:
        script_contents = file.read()
        exec(script_contents)
except FileNotFoundError:
    print(f"The file {file_to_open} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Open the file in read mode
file_path = 'result.txt'  # Change this to the path of your text file
try:
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
        
        # Print the contents to the console
        print(file_contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
