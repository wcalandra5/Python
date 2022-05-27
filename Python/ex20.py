from sys import argv
script, input_file = argv

# Basically a sub for the read function, very nice
# f parameter represents file stuff
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) # seek basically advances to a new spot in the file, default being 0, or start of file - 1 would be move past the first character

def print_a_line(line_count, f):
    print line_count, f.readline() # read each line - every time called, goes to new line in file

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# Loop would be better, will probably get there later
current_line = 1
print_a_line(current_line, current_file) # when you call readline, it moves to the next so this sequence makes sense that it corresponds with current_line

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1   # just like C++, += adds and assigns from right - so x = x + y is the same as x += y
print_a_line(current_line, current_file)