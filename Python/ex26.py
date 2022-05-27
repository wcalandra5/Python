# Fix this code

# This looks fine
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# This looks fine
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # really
    return word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print1 = print_first_word(words)
    print2 = print_last_word(words)
    return print1, print2 # How you get it in one return statement - workaround

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print1 = print_first_word(words)
    print2 = print_last_word(words)
    return print1, print2


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

six = 10 - 2 + 3 - 5
print "This should be six: %d" % six

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


sentence = "All good things come to those who wait."

# Unless we are importing, but let's just do it normally without the ex25 stuff - remove ex25. references
words = break_words(sentence)
sorted_words = sort_words(words)

print print_first_word(words)
print print_last_word(words)
print print_first_word(sorted_words)
print print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words

print print_first_and_last(sentence)

print print_first_and_last_sorted(sentence)
