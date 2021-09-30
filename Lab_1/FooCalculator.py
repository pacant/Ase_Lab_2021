import calc as c

class FooCalculator:
    # empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        c.sum(m, n)

    def divide(self, m, n):
        c.divide(m, n)


calculator = FooCalculator()
print(c.sum(4,4))
print(c.divide(10,2))



