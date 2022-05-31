class Person:

    def __init__(self,my_name):
        self.name = my_name

    def greet(self, your_name):
        self.your_name = your_name
        return f"Hello {self.your_name}, my name is {self.name}"






joe = Person('Joe')
print(joe.greet('Kate')) # should return 'Hello Kate, my name is Joe')
print(joe.name)