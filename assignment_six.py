# Liam Toebbe
# Nov 30, 2023

text_file = open("text_file", "r")

file_contents = text_file.readlines()                   # ['L1\n', 'L2, electric boogaloo\n', 'L3 (the threequel)\n', '\n', 'L5- four is blank']
print("file contents straight", file_contents)
line_count = len(file_contents)                         # 5
print("line count: ", line_count)

file_contents_str = str(file_contents)[1:-1]            # 'L1', 'L2, electric boogaloo', 'L3 (the threequel)', , 'L5- four is blank'
print(file_contents_str)
word_units = file_contents_str.split(' ', -1)      # 'L1', 'L2', 'electric', 'boogaloo', 'L3', '(the', 'threequel)', 'L5-', 'four', 'is', 'blank'
print(word_units)
word_count = word_units.count(' ')                      # 11
print("word count: ", word_count)
