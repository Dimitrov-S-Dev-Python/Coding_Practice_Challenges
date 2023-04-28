"""
Write a program that copies the content of a file to another file.
If the new file doesn't exist, the program should create it.
Expected Output:
For example, if this is the content of the original text file:

"Computer Science is no more about computers than astronomy is about telescopes.
" by Edsger W. Dijkstra
"The computer was born to solve problems that did not exist before." by Bill Gates
"Quiet people have the loudest minds." by Stephen Hawking
"Tell me and I forget. Teach me and I remember. Involve me and I learn."
by Benjamin Franklin
"Intelligence is the ability to adapt to change." by Stephen Hawking
After running the program, the content of the copy (new text file) should also be:

"Computer Science is no more about computers than astronomy is about telescopes."
by Edsger W. Dijkstra
"The computer was born to solve problems that did not exist before." by Bill Gates
"Quiet people have the loudest minds." by Stephen Hawking
"Tell me and I forget. Teach me and I remember. Involve me and I learn."
by Benjamin Franklin
"Intelligence is the ability to adapt to change." by Stephen Hawking
"""
file_path = "content.txt"
copy_path = "copy_content.txt"

with open(file_path) as file, open("copy_content.txt", "w") as copy:
    for line in file:
        copy.write(line)
