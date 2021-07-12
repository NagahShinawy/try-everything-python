"""
created by Nagaj at 12/07/2021
"""


# every thing in python is an OBJECT, which means, every thing has a type created somehow


def themes(*args):
    for color in args:
        print(color, end=" ")
    print()


print(themes)
print(type(themes))  # themes function is instance of <class 'function'>
themes("red", "green", "yellow", "black", "white", "pink")
print("#" * 100)


# meta class : is class defines the rules for another class. [type] ==> type used to create classes
# when you create class, you use metaclass[type] to create it, it's happens automatically , you don't need to do it.


# type metaclass used to create class [TodoList]
class TodoList:
    # when we create class, we call 'type' constructor automatically to create our user define class
    pass


class Car:
    pass


class Profile:
    pass


home_tasks = TodoList()

print(TodoList)
print(home_tasks)

print(type(home_tasks))
print(isinstance(home_tasks, TodoList))

print(type(TodoList))

print(isinstance(TodoList, type))
print(isinstance(TodoList, object))


# when we create class, we call 'type' constructor automatically to create our user define class
# 1- way#1 to create class[automatically] that python does it in behind the scenes


class User:
    pass


print(User)
print(User.__class__)

# explicitly way to create our own class, the below code is equal to [class User:pass] above
myuser = type("User", (), {})

print(myuser)
print(myuser.__class__)

print(
    User == myuser
)  # False. 2 different objs[classes] of class[type], so it returns False
print(User.__class__ == myuser.__class__)  # True, the same type so it returns True


class Drug:
    name = "panadol"
    price = "5$"
    mg = 500


print(Drug().price)

Drug = type(
    "Drug", (), {"name": "panadol", "price": "5$", "mg": 500}
)  # 'type' is metaclass creates classes for us

panadol = Drug()
panadol.market_name = "Panadol Extra"

print(panadol)

print(dir(panadol))

print(panadol.price)
print(panadol.name)
print(panadol.mg)
print(panadol.market_name)

users = []


class User:
    def __init__(self, username, email, image=None):
        self.username = username
        self.email = email
        self.image = image

    def is_exists(self):
        return self in users

    def __repr__(self):
        return f"<{self.username}>"

    def save(self):
        if not self.is_exists():
            users.append(self)

    def update(self, username):
        if username:
            self.username = username

    def delete(self):
        if self.is_exists():
            users.remove(self)


john = User("john", "john@test.com")
james = User("james", "james@test.com")
leon = User("leon", "leon@test.com")
for user in [john, james, leon]:
    user.save()

print(users)

leon.save()
print(users)

james.delete()
print(users)

print("#" * 100)


def show_userprofile(self):
    print(f"Your Username is: {self.username}")
    print(f"Your email is: {self.email}")


UserProfile = type(
    "UserProfile", (User,), {"show_userprofile": show_userprofile}
)  # create 'UserProfile' class using type meta class that inherits from 'User' class

sara = UserProfile("Sara", "sara@test.com")

sara.update(username="sara-smiths")
sara.save()

print(users)

sara.show_userprofile()

print("#" * 100)


# when you write this, this class with its attrs passed to meta class above it that define our own class
class Error:

    # called before init, it is first thing that is always called
    def __new__(cls, *args, **kwargs):
        print("ERROR IS GOING TO CREATE")
        return cls

    def __init__(self):
        print("init called")

    #
    # def __init__(self, desc):
    #     self.desc = desc


bad_request = Error()

print(bad_request)


# we will built our own class


# class is blueprint for how objs behave.
# the same, Meta class is blueprint for how other classes behave & work & defined
class Meta:

    # called before init method
    def __new__(cls, class_name, bases, attrs):
        print(f"CLASS '{class_name}' IS CREATING WITH ATTR {attrs}")
        return type(class_name, bases, attrs)


print("*" * 100)
House = Meta("House", (), {"location": "45-56 cairo"})

print(House.location)


class Device(metaclass=Meta):  # Meta: is a class define the rules of another class
    brand = "Huawei"
    madein = "China"

    def device_info(self):
        print("Brand", self.brand)
        print("Made in", self.madein)


mobile = Device()
print(mobile.brand)

print("#" * 100)


class HuaweiLaptop(Device):
    name = "Mac book"

    def __init__(self, year):
        self.year = year

    def info(self):
        print(f"Laptop is {self.name}")


lap = HuaweiLaptop(2010)
print(lap.year)
print(lap.name)
print(lap.brand)
print(lap.madein)
lap.info()

print("$" * 100)


class StudentMeta:

    def __new__(cls, *args, **kwargs):
        if not args:
            return cls
        attrs = args[-1]
        if 'school' in attrs:
            attrs["SCHOOL"] = attrs["school"]
            del attrs["school"]
        return type(*args)


class Student(metaclass=StudentMeta):
    school = "MANS EDU"

    # School = "MANS EDU"

    def __init__(self, st_name, st_age, cls_room):
        self.cls_room = cls_room
        self.st_age = st_age
        self.st_name = st_name


john = Student("John", 23, "3-a")

print(john.st_name)
# print(john.school)  # error changed to SCHOOL
print(john.SCHOOL)  # error changed to SCHOOL

print("*" * 100)


class Family:
    city = "ALEX"

    def __new__(cls, *args, **kwargs):
        members = args[0]
        if members <= 1:
            raise ValueError(f"Family can not be [{members}] member!")
        return cls

    def __init__(self, members):
        self.members = members

    def info(self):
        print(self.members)


sh = Family(10)

print
