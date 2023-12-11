# class Person:
#     def get_age(self) -> int:
#         raise NotImplementedError("!!")


# class Worker(Person):
#     def get_age(self) -> int:
#         return 78


# class Actor(Person):
#     pass


# man = Actor()

# print(man.get_age())

# Create two classes: Shape and Rectangle.
# The Shape class should have the following attributes: name and color.
# It should also have a method called get_area() that returns the abstract area of a shape.

# The Rectangle class should inherit from the Shape class
# and should have the following attributes: width and height.
# It should also override the get_area() method to calculate the area of a rectangle using its width and height.


# class Shape:
#     ABSTRACT_AREA = 14

#     def __init__(self, shape: str, color: str) -> None:
#         self.shape: str = shape
#         self.color: str = color

#     def get_area(self) -> float:
#         return self.ABSTRACT_AREA


# class Rectangle(Shape):
#     def __init__(self, shape: str, color: str, width: float, height: float) -> None:
#         super().__init__(shape, color)
#         self.width: float = width
#         self.height: float = height

#     def get_area(self) -> float:
#         return f"The area of {self.shape} is {self.width * self.height}."


# rectangle_blue = Shape(shape="rectangle", color="blue")
# rectangle = Rectangle(shape="rectangle", color="red", width=14.0, height=8.5)
# print(rectangle.get_area())
# print(rectangle_blue.get_area())

# Create a class hierarchy for representing different types of geometric figures, such as rectangles, circles, and triangles.
# Each class should have attributes for defining the shape's characteristics, such as dimensions or parameters.
# Use inheritance and method overriding to define methods for calculating the area and perimeter of different shapes
# Possible shapes: Circle, Polygon, RegularPolygon(Polygon), Rectangle(RegularPolygon)


# from math import pi


# class Shape:
#     ABSTRACT_AREA = 14
#     ABSTRACT_PERIMETER = 14

#     def __init__(self, shape: str, color: str) -> None:
#         self.shape: str = shape
#         self.color: str = color

#     def get_area(self) -> float:
#         raise NotImplementedError("We dont have enough data to calculate area!!")

#     def get_perimeter(self) -> float:
#         raise NotImplementedError("We dont have enough data to calculate perimeter!!")


# class Circle(Shape):
#     def __init__(self, shape: str, color: str, radius: float) -> None:
#         super().__init__(shape, color)
#         self.radius: float = radius

#     def get_area(self) -> float:
#         circle_area = (self.radius**2) * pi
#         return f"The area of {self.shape} is {circle_area}."

#     def get_perimeter(self) -> float:
#         circle_perimeter = 2 * pi * self.radius
#         return f"The perimeter of {self.shape} is {circle_perimeter}"


# class Triangle(Shape):
#     def __init__(
#         self, shape: str, color: str, side_a: float, side_b: float, side_c: float
#     ) -> None:
#         super().__init__(shape, color)
#         self.side_a: float = side_a
#         self.side_b: float = side_b
#         self.side_c: float = side_c

#     def get_area(self) -> float:
#         triangle_area = self.side_a * self.side_b / 2
#         return f"The area of {self.shape} is {triangle_area}."

#     def get_perimeter(self) -> float:
#         triangle_perimeter = self.side_a + self.side_b + self.side_c
#         return f"The area of {self.shape} is {triangle_perimeter}."


# class Polygon(Shape):
#     def __init__(self, shape: str, color: str) -> None:
#         super().__init__(shape, color)


# class RegularPolygon(Polygon):
#     def __init__(self, shape: str, color: str) -> None:
#         super().__init__(shape, color)


# class Rectangle(RegularPolygon):
#     def __init__(self, shape: str, color: str, width: float, height: float) -> None:
#         super().__init__(shape, color)
#         self.width: float = width
#         self.height: float = height

#     def get_area(self) -> float:
#         return f"The area of {self.shape} is {self.width * self.height}."

#     def get_perimeter(self) -> float:
#         rectangle_perimeter = self.width * 2 + self.height * 2
#         return f"The perimeter of {self.shape} is {rectangle_perimeter}"


# circle = Circle(shape="circle", color="black", radius=5.0)
# polygon = Polygon(shape="polygon", color="grey")
# rectangle = Rectangle(shape="rectangle", color="red", width=14.0, height=8.5)
# print(rectangle.get_area())
# print(rectangle.get_perimeter())
# print(circle.get_perimeter())
# print(polygon.get_area())

# *********************************METHOD_RESOLUTION_ORDER************************************


# class A:
#     def foo(self) -> None:
#         print("A.foo")


# class B(A):
#     def foo(self) -> None:
#         print("B.foo")


# class C(A):
#     def foo(self) -> None:
#         print("C.foo")


# class D(C, B):
#     pass


# d = D()

# d.foo()

# print(D.__mro__)


# class Shape:
#     def __init__(self, shape: str, sides: int) -> None:
#         self.shape: str = shape
#         self.sides: int = sides

#     def get_area(self) -> float:
#         raise NotImplementedError("We dont have enough data to calculate area!!")


# class Rectangle(Shape):
#     def __init__(self, shape: str, sides: int, width: float, height: float) -> None:
#         super().__init__(shape, sides)
#         self.width: float = width
#         self.height: float = height

#     def get_area(self) -> float:
#         rectangle_area: float = self.width * self.height
#         return f"Area of {self.shape} is {rectangle_area}"


# class Square(Rectangle):
#     def __init__(
#         self, shape: str, sides: int, width: float, height: float, side_length: float
#     ) -> None:
#         super().__init__(shape, sides, width, height)
#         self.side_length: float = side_length


# square = Square(shape="square", sides=4, width=2.0, height=3.8, side_length=7.8)

# print(square.get_area())
# print(square.side_length)


# class Vehicle:
#     CHARGES = 100

#     def __init__(
#         self,
#         seating_capacity: int,
#         door_amount: int,
#         color: str,
#         fuel_consumption: float,
#     ) -> None:
#         self.seating_capacity: int = seating_capacity
#         self.door_amount: int = door_amount
#         self.fuel_consumption: int = fuel_consumption

#     def get_fare_charge(self) -> float:
#         fare_price = self.seating_capacity * self.CHARGES
#         return f"Fare price is {fare_price}"

#     def make_sound(self) -> str:
#         return f"bbbrrrrrrrrrrrrrrrrrrrrrrrrrrrr"

#     def get_door_number(self) -> int:
#         return f"Vehicle has {self.door_amount} doors"

#     def get_fuel_consumption(self) -> str:
#         return f"Vehicle uses {self.fuel_consumption} litres of fuel"


# class Bus(Vehicle):
#     EXTRA_BUS_CHARGE = 1.1

#     def __init__(
#         self,
#         seating_capacity: int,
#         door_amount: int,
#         color: str,
#         fuel_consumption: float,
#         type: str,
#     ) -> None:
#         super().__init__(seating_capacity, door_amount, color, fuel_consumption)
#         self.type: str = type

#     def make_sound(self) -> str:
#         return f"{self.type} makes sound 'BBRRRRRMMMMMMM'"

#     def get_fare_charge(self) -> float:
#         fare_price = self.seating_capacity * self.CHARGES * self.EXTRA_BUS_CHARGE
#         return f"Total {self.type} charge will be {fare_price}"


# class Train(Vehicle):
#     def __init__(
#         self,
#         seating_capacity: int,
#         door_amount: int,
#         color: str,
#         fuel_consumption: float,
#         type: str,
#         number_of_wagons: int,
#     ) -> None:
#         super().__init__(seating_capacity, door_amount, color, fuel_consumption)
#         self.type: str = type
#         self.number_of_wagons: int = number_of_wagons

#     def make_sound(self) -> str:
#         return f"{self.type} makes sound 'CHOO CHHOO CHOOOOO'"

#     def get_fuel_consumption(self) -> str:
#         train_fuel_consumption: float = self.fuel_consumption * self.number_of_wagons
#         return f"{self.type} uses {train_fuel_consumption} litres of fuel"


# class Taxi(Vehicle):
#     def __init__(
#         self,
#         seating_capacity: int,
#         door_amount: int,
#         color: str,
#         fuel_consumption: float,
#         type: str,
#     ) -> None:
#         super().__init__(seating_capacity, door_amount, color, fuel_consumption)
#         self.type: str = type


# bus = Bus(
#     seating_capacity=45,
#     door_amount=3,
#     color="Yellow",
#     fuel_consumption=10.1,
#     type="Bus",
# )
# train = Train(
#     seating_capacity=60,
#     door_amount=2,
#     color="Yellow",
#     fuel_consumption=20.1,
#     type="Train",
#     number_of_wagons=3,
# )
# taxi = Taxi(
#     seating_capacity=3, door_amount=4, color="pink", fuel_consumption=5.0, type="Car"
# )
# print(bus.get_fare_charge())
# print(bus.make_sound())
# print(train.get_fuel_consumption())
# print(taxi.make_sound())

# *********************************ABSTRACTMETHOD***************************************

from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def get_vehicle_type(self) -> str:
#         pass

#     def return_color(self) -> str:
#         return "White"


# class Plane(Vehicle):
#     def get_vehicle_type(self) -> str:
#         return "Plane"


# plane = Plane()
# print(plane.return_color())


# class Animal(ABC):
#     def __init__(self, name: str) -> None:
#         self.name: str = name

#     @abstractmethod
#     def speak(self) -> None:
#         pass

#     def get_name(self) -> str:
#         return self.name

# class Dog(Animal):
#     def __init__(self, name: str) -> None:
#         super().__init__(name)

#     def speak(self) -> str:
#         return f"Dog says Woof!"

# class Cat(Animal):
#     def __init__(self, name: str) -> None:
#         super().__init__(name)

#     def speak(self) -> str:
#         return f"Cat says Meow!"


class Money(ABC):
    def __init__(self, currency: str, value: float) -> None:
        self.currency: str = currency
        self.value: float = value

    def get_value(self) -> float:
        return f"Value is {self.value}"

    def get_currency(self) -> str:
        return f"Currency is {self.currency}"

    @abstractmethod
    def convert_to_currency(self, target_currency: str, conversion_rate: float) -> None:
        pass


class Cash(Money):
    def __init__(self, currency: str, value: float) -> None:
        super().__init__(currency, value)

    def convert_to_currency(
        self, target_currency: "Cash", conversion_rate: float
    ) -> float:
        converted: float = self.value * conversion_rate
        return f" {self.value} of {self.currency} equals {converted} {target_currency.currency}"


class Card(Money):
    def __init__(self, currency: str, value: float, credit_limit: float) -> None:
        super().__init__(currency, value)
        self.credit_limit: float = credit_limit

    def convert_to_currency(
        self, target_currency: "Card", conversion_rate: float
    ) -> float:
        converted: float = self.credit_limit * conversion_rate
        return f" {self.credit_limit} of credit limit on card in {self.currency} equals {converted} {target_currency.currency}"


cash_eur = Cash("EUR", 100.0)
cash_nok = Cash("NOK", 25000.0)

card_eur = Card("EUR", 1500.0, 45000.0)
card_usd = Card("USD", 4500.0, 100000.0)

print(cash_eur.convert_to_currency(cash_nok, 10.1))
print(card_eur.convert_to_currency(card_usd, 1.2))


# class Building(ABC):
#     def __init__(self, levels: int, purpose: str) -> None:
#         super().__init__()
#         self.levels: int = levels
#         self.purpose: str = purpose

#     def get_purpose(self) -> str:
#         return self.purpose

#     def get_level_number(self) -> int:
#         return self.levels

#     @abstractmethod
#     def get_material(self) -> None:
#         pass

#     @abstractmethod
#     def get_roof(self) -> None:
#         pass

#     @abstractmethod
#     def has_basement(self) -> None:
#         pass


# class Skyscraper(Building):
#     def __init__(
#         self, levels: int, purpose: str, material: str, basement: bool, roof: str
#     ) -> None:
#         super().__init__(levels, purpose)
#         self.material: str = material
#         self.basement: bool = basement
#         self.roof: str = roof

#     def get_material(self) -> str:
#         return self.material

#     def has_basement(self) -> None:
#         if self.basement:
#             return "Has basement"
#         else:
#             return "Does not have basement"

#     def get_roof(self) -> None:
#         return self.roof


# class BrickBuilding(Building):
#     def __init__(
#         self, levels: int, purpose: str, material: str, basement: bool, roof: str
#     ) -> None:
#         super().__init__(levels, purpose)
#         self.material: str = material
#         self.basement: bool = basement
#         self.roof: str = roof

#     def get_material(self) -> str:
#         return self.material

#     def has_basement(self) -> None:
#         if self.basement:
#             return "Has basement"
#         else:
#             return "Does not have basement"

#     def get_roof(self) -> None:
#         return self.roof


# sky = Skyscraper(
#     levels=35, purpose="offices", material="glass", basement=False, roof="Glass"
# )
# brick = BrickBuilding(
#     levels=2, purpose="residential", material="bricks", basement=True, roof="triangle"
# )

# print(sky.get_material())
# print(brick.has_basement())
# print(brick.get_material())
# print(sky.has_basement())
