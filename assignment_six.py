text_file = open("text_file", "r")

file_contents = text_file.readlines()
print(file_contents)
line_count = len(file_contents)

file_contents = [''.join(file_contents)]
print (str(file_contents))

word_count = file_contents.split()
print(word_count)


# word_count = file_contents.count(" ")
# print(word_count)
