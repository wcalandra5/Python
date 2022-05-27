class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent): # child inherits all behavior from parent
    pass

dad = Parent()
son = Child()

# These will print the same thing - the parent.implicit() piece
dad.implicit()
son.implicit()
