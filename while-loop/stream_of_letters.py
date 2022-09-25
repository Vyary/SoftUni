letter = input()

new_word = ''
secret_word = ''
c_count = 0
o_count = 0
n_count = 0

# ASCII table link -> https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
# 65 is the number of Uppercase A in ASCII table
# 90  is the number of Uppercase Z in ASCII table
# 97  is the number of Lowercase a in ASCII table
# 122  is the number of Lowercase z in ASCII table

while letter != 'End':
    letter_number = ord(letter)  # ord is used to find ASCII number of the letter
    if 65 <= letter_number <= 90 or 97 <= letter_number <= 122:  # check if letter is between A - Z or a - z
        if letter == 'c':
            c_count += 1
            if c_count > 1:
                new_word += letter
                c_count = 1
        elif letter == 'o':
            o_count += 1
            if o_count > 1:
                new_word += letter
                o_count = 1
        elif letter == 'n':
            n_count += 1
            if n_count > 1:
                new_word += letter
                n_count = 1
        else:
            new_word += letter

        if n_count == 1 and o_count == 1 and c_count == 1:
            new_word += ' '
            secret_word = new_word
            c_count = 0
            o_count = 0
            n_count = 0

    letter = input()

print(secret_word)
