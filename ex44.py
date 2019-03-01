class Parent(object):
    age = 20
    def alter(self):
        print("Parent altered")
class Child(Parent):
    def alter(self):
        print("Child before parent altered")
        super(Child,self).alter()
        print("Child after parent altered")

dad = Parent()
son = Child()
dad.alter()
son.alter()
