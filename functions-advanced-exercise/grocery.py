def grocery_store(**kwargs):
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ""

    for item in sorted_items:
        result += f"{item[0]}: {item[1]}\n"

    return result


"""                     Task:
Create a function called grocery_store() that receives a different number of key-value
pairs. The key will be the product's name and the value - its quantity.
You should return a sorted receipt for all products. They should be sorted by their
quantity in descending order. If there are two or more products with the same quantity,
sort them by their name's length in descending order. If there are two or more products
with the same name's length, sort them by their name in ascending order
(alphabetically). In the end, return a string in the following format:
"{product_name1}: {product_quantity1}
{product_name2}: {product_quantity2}
…
{product_nameN}: {product_quantityN}"

Example:
Test Code:
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
Output:
pasta: 12
eggs: 12
bread: 5
"""
