# If you type "python" and then "import ex25" in the terminal, you can use these functions.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # split should come in handy for separating things
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words) # Looks like this is built-in from Python

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # Pop 0 for first, -1 for last
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)