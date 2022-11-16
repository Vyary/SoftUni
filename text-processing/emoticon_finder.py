# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

start_text = input()
for index in range(len(start_text)):
    if start_text[index] == ':':
        emoticon = ':' + start_text[index + 1]
        print(emoticon)
