def start_spring(**kwargs):
    types_dictionary = {}

    for key, value in kwargs.items():

        if value not in types_dictionary:
            types_dictionary[value] = []
        types_dictionary[value].append(key)

    sorted_type_dict = sorted(
        types_dictionary.items(), key=lambda x: (-len(x[1]), x[0])
    )

    result = ""
    for type, names in sorted_type_dict:
        sorted_names = sorted(names)
        result += f"{type}:\n"
        result += "\n".join([f"-{name}" for name in sorted_names]) + "\n"

    return result


"""                     Task:
Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth
seems to come to life again. Farmers and gardeners plant their seeds and temperatures
slowly rise.
Write a function called start_spring which will receive a different number of
keyword arguments.
Each keyword holds a key with a name of the spring object (string), and each value
holds its type (string). For example, dahlia="flower", shrikes="bird", dogwood="tree".
The function should sort the given spring objects in collections by their type:
•	The collections sorted by their number of elements in descending order. If two or
more collections have the same number of elements in them, return them in ascending
order (alphabetically) by the type's name.
•	Each collection's elements should be sorted in ascending order (alphabetically) by
the object's name.

Example:
Test Code:
example_objects = {
    "Water Lilly": "flower",
    "Swifts": "bird",
    "Callery Pear": "tree",
    "Swallows": "bird",
    "Dahlia": "flower",
    "Tulip": "flower",
}
print(start_spring(**example_objects))
Output:
flower:
-Dahlia
-Tulip
-Water Lilly
bird:
-Swallows
-Swifts
tree:
-Callery Pear
"""
