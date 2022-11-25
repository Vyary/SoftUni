raw_key = input()
instruction = input()

while instruction != "Generate":
    split_instruction = instruction.split(">>>")
    command = split_instruction[0]
    if command == "Contains":
        substring = split_instruction[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        upper_or_lower = split_instruction[1]
        start_index = int(split_instruction[2])
        end_index = int(split_instruction[3])
        if upper_or_lower == "Upper":
            raw_key = (
                raw_key[:start_index]
                + raw_key[start_index:end_index].upper()
                + raw_key[end_index:]
            )
            print(raw_key)
        elif upper_or_lower == "Lower":
            raw_key = (
                raw_key[:start_index]
                + raw_key[start_index:end_index].lower()
                + raw_key[end_index:]
            )
            print(raw_key)
    elif command == "Slice":
        start_index = int(split_instruction[1])
        end_index = int(split_instruction[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

    instruction = input()
print(f"Your activation key is: {raw_key}")


"""                                Task:
You are about to make some good money, but first, you need to think of a way 
to verify who paid for your product and who didn't. You have decided to let 
people use the software for a free trial period and then require an activation
key to continue using the product. Before you can cash out, the last step is
to design a program that creates unique activation keys for each user. 
So, waste no more time and start typing!

The first line of the input will be your raw activation key. 
It will consist of letters and numbers only. 
After that, until the "Generate" command is given, you will be receiving
strings with instructions for different operations that need to be performed
upon the raw activation key.
There are several types of instructions, split by ">>>":

"Contains>>>{substring}":
    If the raw activation key contains the given substring, 
        prints: "{raw activation key} contains {substring}".
    Otherwise, prints: "Substring not found!"

"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
    Changes the substring between the given indices (the end index is exclusive)
        to upper or lower case and then prints the activation key.
    All given indexes will be valid.
"Slice>>>{startIndex}>>>{endIndex}":
    Deletes the characters between the start and end indices 
        (the end index is exclusive) and prints the activation key.
    Both indices will be valid.
Input
    The first line of the input will be a string consisting of 
        letters and numbers only. 
    After the first line, until the "Generate" command is given, 
        you will be receiving strings.
Output
    After the "Generate" command is received, print:
        "Your activation key is: {activation key}"
        
Examples        
            Input                     Output
    abcdefghijklmnopqrstuvwxyz  abghijklmnopqrstuvwxyz
    Slice>>>2>>>6               abgHIJKLMNOPQRstuvwxyz
    Flip>>>Upper>>>3>>>14       abgHIjkLMNOPQRstuvwxyz
    Flip>>>Lower>>>5>>>7        Substring not found!
    Contains>>>def              Substring not found!
    Contains>>>deF              Substring not found!
    Generate                    Your activation key is: abgHIjkLMNOPQRstuvwxyz
"""
