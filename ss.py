import os

def rename_files(directory):
    # Change to the directory containing the files
    os.chdir(directory)

    # List all files in the directory
    files = os.listdir()

    # Filter out files that don't match the pattern "00001.png", "00002.png", etc.
    files = [f for f in files if f.endswith('.png') and f.startswith('000')]

    # Sort the files to maintain the order
    files.sort()

    # Rename each file
    for file in files:
        # Extract the number from the filename
        number = int(file.split('.')[0])

        # Create the new filename
        new_filename = f"frame{number}.png"

        # Rename the file
        os.rename(file, new_filename)

    print("Files renamed successfully.")

# Example usage
rename_files('.')  # Replace with your directory path
