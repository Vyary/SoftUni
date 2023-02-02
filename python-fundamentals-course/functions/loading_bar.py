# You will receive a single integer number between 0 and
# 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.

def loading_bar(percent: int) -> str:
    if percent == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        loaded = int(percent / 10)
        rest = 10 - loaded
        return f'{percent}% [{"%" * loaded}{"." * rest}]\nStill loading...'


percentage = int(input())
print(loading_bar(percentage))
