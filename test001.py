<<<<<<< HEAD
class Person:
    def __init__(self, name, age):
        self.__name = name      # private attribute
        self.__age = age        # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

# Example usage
person = Person("Alice", 30)
print(person.get_name())  # Alice
print(person.get_age())   # 30

person.set_age(35)
print(person.get_age())   # 35

person.set_age(-5)        # Age must be positive.
=======
nothing to show
>>>>>>> gitbranch1
