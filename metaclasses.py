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
print(username.__class__.__class__)  # type

print("#" * 100)


# In Python, we can customize the class CREATION process by passing the metaclass keyword in the class definition.
# This can also be done by inheriting a class that has already passed in this keyword


class IDEMeta(type):
    pass


class JetBrains(metaclass=IDEMeta):
    pass


class Pycharm(JetBrains):
    pass


class AndroidStudio(JetBrains):
    pass


print(IDEMeta.__class__)  # type ==>  'IDEMeta' created by metaclass [type]
print(JetBrains.__class__)  # IDEMeta ==>  'JetBrains' created by metaclass [IDEMeta]
print(
    Pycharm.__class__
)  # IDEMeta  ==> 'Pycharm' inherits from  'JetBrains' that is created by metaclass [IDEMeta]
print(
    AndroidStudio.__class__
)  # IDEMeta   ==> 'AndroidStudio' inherits from  'JetBrains' that is created by metaclass [IDEMeta]

print("#" * 100)

# When defining a class and no metaclass is defined the default [type metaclass] will be used.
# If a metaclass is given and it is not an instance of type(), then it is used directly as the metaclass.


print("*" * 100)


# __new__ is used when one wants to define dict or bases tuples before the class is created.
# The return value of __new__is usually an instance of cls.
# __new__ allows subclasses of immutable types to customize instance creation.
# It can be overridden in custom metaclasses to customize class creation.
# __init__ is usually called after the object has been created so as to initialize it.


class Request:

    def __new__(cls, *args, **kwargs):
        cls.headers = dict(lang="en", content_type="json")
        if kwargs.get("nid") is not None:
            cls.headers["nid"] = kwargs["nid"]
        return super().__new__(cls)


print(Request, Request.__class__)

post = Request(nid="64654654")

print(post, post.__class__)
print(post.headers)

get_req = Request()

print("get request", get_req)


class Car:

    def get(self):
        print("GET")


class Demo:
    pass


bmw = Car()

bmw.get()
Car.get(bmw)

print(Car.__new__(Car))
print(Car().__new__(Car))

print(bmw.__new__(Car))

print(Demo().__new__(Car))
print(Car().__new__(Demo))
