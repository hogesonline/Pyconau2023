class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person2 = Person("Bob", 40)

print(person1.name)  # Prints "Alice"
person2.say_hello()  # Prints "Hello, my name is Bob and I am 40 years old."


