class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent): # child inherits all behavior from parent

    def altered(self):
        print "CHILD, BEFORE PARENT altered(). Overridden normally."
        super(Child, self).altered() # THIS WILL PRINT THE PARENT VERSION OF THE ALTERED FUNCTION, NOT THE CHILD
        print "CHILD, AFTER PARENT altered." # THEN THIS WILL EXECUTE

dad = Parent()
son = Child()

# Print
dad.altered()
son.altered()
