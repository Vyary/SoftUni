# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add
# the result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other,
# add the remaining character codes to the total sum without multiplication.

def ascii_dec_number_multiplier(string_one: str, string_two: str) -> int:
    total_sum = 0
    for index in range(len(string_two)):
        total_sum += ord(string_one[index]) * ord(string_two[index])
    for index in range(len(string_two), len(string_one)):
        total_sum += ord(string_one[index])
    return total_sum


def main():
    string_one, string_two = input().split(' ')
    if len(string_one) >= len(string_two):
        print(ascii_dec_number_multiplier(string_one, string_two))
    else:  # len(string_two) > len(string_one):
        print(ascii_dec_number_multiplier(string_two, string_one))


if __name__ == '__main__':
    main()
