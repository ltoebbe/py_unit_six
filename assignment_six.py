# Liam Toebbe
# Nov 30, 2023

# text_file = open("text_file", "r")
#
# file_contents = text_file.readlines
# print("file contents straight", file_contents)
# line_count = len(file_contents)
# print("line count: ", line_count)
#
# file_contents_str = str(file_contents)[1:-1]
# print(file_contents_str)
# word_units = file_contents_str.split(' ', -1)
# print(word_units)
# word_count = word_units.count(' ')
# print("word count: ", word_count)

text_file = open("text_file", "r")

file_contents = text_file.readlines()
line_count = len(file_contents)
print("line count: ", line_count)

word_count = 0
for line in text_file.readlines():
    words = line.split()
    word_count = word_count + len(words)
print("wordcount: ", word_count)

content = text_file.read()
character_count = len(content)
print(character_count)
