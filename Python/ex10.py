tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# This makes a flipping line, like a tire spoke - pretty cool
# while True:
   # for i in ["/", "-", "|", "\\", "|"]:
     #   print "%s\r" % i,

r_test = "Escape %r me." % '\n'
s_test = "Escape %s me string." % '\n'

print r_test
print s_test