import os

search_directory = input()

# depth = 1 is the source directory
# depth = 2 is 1 folder deep
depth = 2

file_dictionary = {}

# os.walk traverses the directory tree
for root, dirs, files in os.walk(search_directory, topdown=True):

    # Check if the current directory is within the specified search depth
    if root[len(search_directory) :].count(os.sep) < depth:

        for file in files:

            # Try to split the file name and extension
            try:
                filename, ext = file.split(".")
            # If the file does not have an extension, print a
            # message and continue with the next file
            except ValueError:
                print(f"{file} does not have an extension")
                continue

            if ext not in file_dictionary:
                file_dictionary[ext] = []

            file_dictionary[ext].append(file)

sorted_dictionary = sorted(file_dictionary.items(), key=lambda item: item[0])

with open("report.txt", "w") as file:
    for key, values in sorted_dictionary:
        file.write(f".{key}" + "\n")

        for value in sorted(values):
            file.write(f"- - - {value}" + "\n")


"""                     Task:
Write a program that traverses a given directory for all files.
Search through the first level of the directory only and write information about each
found file in report.txt. The files should be grouped by their extension.
Extensions should be ordered by name alphabetically. The files with extensions
should also be sorted by name. report.txt should be saved in the chosen directory.
"""
