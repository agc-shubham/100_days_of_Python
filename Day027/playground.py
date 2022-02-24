def add(*args):
    print(args[0])
    sum = 0
    for i in args:
        sum+=i
    return sum


print(add(1,2,5,8,6,4,2,3))

def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)

class car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = car(make = "nissan")
print(my_car.model) 
# // prints None