class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"
    
class Child(object):

    def __init__(self):
        self.other = Other() # just set the other property to the other class, no inheritance needed
    
    def implicit(self):
        self.other.implicit() # will print other implicit piece
    
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered() # no super needed - get it from other directly, will print the other altered piece
        print "CHILD. AFTER OTHER altered()"
    
son = Child()

son.implicit()
son.override()
son.altered()