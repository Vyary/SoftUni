# You will be given number n. After that, you'll receive different strings n times. '
# Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters:
# comma ",", period ".", or underscore "_":

# number_of_strings = int(input())
# text_is_not_pure = False
#
# for _ in range(number_of_strings):
#     current_text = input()
#     for letter in current_text:
#         if letter == ',' or letter == '.' or letter == '_':
#             text_is_not_pure = True
#             break
#     if text_is_not_pure:
#         print(f'{current_text} is not pure!')
#     else:
#         print(f'{current_text} is pure.')
#
#

number_of_strings = int(input())
for string in range(number_of_strings):
    current_string = input()
    if ',' in current_string or '.' in current_string or '_' in current_string:
        print(f'{current_string} is not pure!')
    else:
        print(f'{current_string} is pure.')
