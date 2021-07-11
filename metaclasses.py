"""
created by Nagaj at 11/07/2021
"""


class Profile:
    pass


name = "test"
print(name, "==>", type(name))

pro = Profile  # class not OBJ
print(pro, "==>", type(pro))

james = Profile()  # obj of class Profile

print(james, "==>", type(james))

print(isinstance(james, Profile))  # True
print(
    isinstance(james, type)
)  # False because james is obj of profile not Profile itself as class
print(isinstance(james, object))  # True


print("#" * 100)

print(isinstance(pro, Profile))  # False because john is profile class not obj
print(isinstance(pro, type))  # True
print(isinstance(pro, object))  # True


print(type(object))  # type

# user class is instance of [type] & [object]

# type & object something to generate user define classes [ object to be inherited , type the type of new class]
# type is enables us to create classes dynamically.

# The DataCamp class shown below would be created as shown below using type:


class DataCamp:
    pass


print("#" * 100)
print(DataCamp())  # instance of 'DataCamp' class
# type used to create new user defined classes
# DataCamp is the class name while DataCampClass is the variable that holds the class reference
DataCampClass = type("DataCamp", (), {})
print(DataCampClass)  # <class '__main__.DataCamp'>.
# it prints 'DataCamp' not 'DataCampClass' because you passed 'DataCamp' to type as a name of class


print("*" * 100)

# When using type we can pass attributes of the class using a dictionary
PythonClass = type(
    "PythonClass", (), {"start_date": "August 2018", "instructor": "John Doe"}
)
print(PythonClass.start_date, PythonClass.instructor)
print(PythonClass)


print("*" * 100)


# In case we wanted our PythonClass to inherit from the DataCamp class
# we pass it to our second argument when defining the class using type
PythonClass = type("MyPythonClass", (DataCamp,), {"username": "leon", "age": 29})
python = PythonClass()
print(isinstance(python, PythonClass))  # True
print(isinstance(python, DataCamp))  # True
print(isinstance(python, object))  # True
print(isinstance(python, type))  # False

print("$" * 50)
# every class in python created  metaclasses
print("test".__class__, str.__class__)
print(isinstance(PythonClass, type), PythonClass.__class__)
print(isinstance(PythonClass, object))
print(isinstance(type, object), type.__class__)
print(isinstance(object, type), object.__class__)
print(isinstance(type, type))
print(isinstance(object, object))


# When we check the type for float, int, list, tuple, and dict, we will have a similar output.
# This is because all of these objects are of type type.
print(type(list), type(float), type(dict), type(tuple))

username = "test"
print(username.__class__.__class__)
