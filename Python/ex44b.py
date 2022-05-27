class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent): # child inherits all behavior from parent - overrides this function

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

# son will override the parent's override() function - so it will print CHILD override piece
dad.override()
son.override()
