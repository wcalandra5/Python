# Here's some strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # The \n delimiter is the same as C++
# If you used the \n with the %r formatter, then it will be ugly in display. Cause raw data, right?

print "Here are the days:", days
print "Here are the months: ", months # Extra space here for some reason, not necessary

print """
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
