from sys import argv

script, user_name, mood = argv # User types username in the command line
prompt = 'Type here: ' # Clever use of this to indicate place to type for user

print "Hi %s, I'm the %s script. I see you are %s." % (user_name, script, mood)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) # No text necessary, prompted with the carrot

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)