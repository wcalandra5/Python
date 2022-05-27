from sys import argv
from os.path import exists

script, from_file, to_file = argv # cleverly define three variables from cmd line

# print "Copying from %s to %s." % (from_file, to_file)

# We could do these two on one line too, how? Use the semicolon!
in_file = open(from_file); indata = in_file.read()

print "The input file is %d bytes long." % len(indata) # len() returns the string length

# print "Deos the output file exist? %r" % exists(to_file) # Imported the exists library - tells us if file exists
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()