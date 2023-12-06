# https://realpython.com/python-classes/

class Dog:
    def __init__(self, name, breed, age, tired):
        self.Name = name
        self.Breed = breed
        self.Age = age
        self.Tired = tired
        self.tricks = []

    def __repr__(self):
        return f"Name: {self.Name}, Breed: {self.Breed}, Age: {self.Age}"

    def Sleep(self):
        if self.Tired == True:
            return "I will sleep"
        else:
            return "I don't want to sleep"

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido", "Husky", 15, tired=True)
print(d)
print(d.Sleep())
d.add_trick("roll over")
print(d.tricks)

e = Dog("Buddy", "Labrador", 5, tired=False)
print(e)
print(e.Sleep())
e.add_trick("play dead")
print(e.tricks)


class Cat(Dog):
    "This is a cat class"
    play = True

    def __init__(self, name, breed, age, tired, furry, season="summer", number=1):
        Dog.__init__(self, name, breed, age, tired)
        self.Furry = furry
        self.Season = season
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if isinstance(value, int):
            raise ValueError("This is not a number!")

        self._number = value

    def __str__(self):
        return f"Name: {self.Name}, Age: {self.Age}"

    def season(self, season):
        self.Season = season
        return self.Season

    def __del__(self):
        print("Destructor called")


c = Cat("Mata", "Tcbby", 13, tired=False, furry=True)
print(c)
print(c.__doc__)
print(c.play)
print(c.season("fall"))
print(c.Sleep())
c.add_trick("sleep")
print(c.tricks)


print(isinstance(c, Cat))
print(issubclass(Cat, Dog))

del c


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x, y)

    def __eq__(self, other):
        self_mag = (self.x**2) + (self.y**2)
        other_mag = (other.x**2) + (other.y**2)
        return self_mag == other_mag

    def __lt__(self, other):
        self_mag = (self.x**2) + (self.y**2)
        other_mag = (other.x**2) + (other.y**2)
        return self_mag < other_mag


p1 = Point(1, 2)
print(p1)
p2 = Point(2, 3)
print(p2)

print(p1 + p2)
print(p1 * p2)
print(p1 == p2)
print(p1 < p2)


class Test:
    def _decorator(func):
        def func_wrapper(self, x):
            print(f"start magic {x} - {func.__name__}")
            func(self, x * 2)
            print(f"end magic {x} - {func.__name__}")

        return func_wrapper

    @_decorator
    def bar(self, n):
        print(f"normal call {n}")


test = Test()
test.bar(3)
