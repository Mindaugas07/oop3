# *******Class methods************

# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

#     @classmethod
#     def from_square(cls, side_length: float) -> 'Rectangle':
#         return cls(side_length, side_length)

# rectangle1: Rectangle = Rectangle(3.0, 4.0)
# rectangle2: Rectangle = Rectangle.from_square(2.0)

# print(rectangle1.area())  # 12.0
# print(rectangle2.area())  # 4.0


# import datetime

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
#         age = cls.get_age(birth_year)
#         return cls(name, age)

#     @staticmethod
#     def get_age(birth_year: int) -> int:
#         return datetime.date.today().year - birth_year

# person: Person = Person.from_birth_year('John', 1990)
# print(person.name)  # John
# print(person.age)  # 33


# class Car:
#     total_cars_sold: int = 0

#     def __init__(self, make: str, model: str):
#         self.make = make
#         self.model = model
#         Car.total_cars_sold += 1

#     @classmethod
#     def get_total_cars_sold(cls) -> int:
#         return cls.total_cars_sold


# car1: Car = Car("Toyota", "Camry")
# car2: Car = Car("Honda", "Civic")

# print(Car.get_total_cars_sold())  # 2


# class Point:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y

#     @classmethod
#     def from_tuple(cls, point_tuple: tuple[float, float]) -> 'Point':
#         x, y = point_tuple
#         return cls(x, y)

# point: Point = Point.from_tuple((3, 4))
# print(point.x)  # 3
# print(point.y)  # 4


# class Student:
#     all_students: list["Student"] = []

#     def __init__(self, name: str, grade: float):
#         self.name = name
#         self.grade = grade
#         Student.all_students.append(self)

#     @classmethod
#     def get_highest_grade(cls) -> "Student":
#         return max(cls.all_students, key=lambda student: student.grade)

#     @classmethod
#     def get_lowest_grade(cls) -> "Student":
#         return min(cls.all_students, key=lambda student: student.grade)


# student1: Student = Student("John", 90)
# student2: Student = Student("Jane", 95)
# student3: Student = Student("Alice", 80)

# print(Student.all_students)

# print(Student.get_highest_grade().grade)  # Jane
# print(Student.get_lowest_grade().name)  # Alice


# class Factorial:

#     @classmethod
#     def factorial(cls, number: int) -> int:
#         fact = 1
#         for num in range(2, number + 1):
#             fact *= num
#         return fact


# some_thing: Factorial = Factorial.factorial(10000)
# print(some_thing)


# class String_reverse:
#     @classmethod
#     def reverse_string(cls, name: str) -> str:
#         return name[::-1]


# new_string: String_reverse = String_reverse.reverse_string("Mindaugas")

# print(new_string)


# class PrimeNumbers:
#     PRIME_NUMBER_LIST = []

#     @classmethod
#     def prime_numbers(cls, number: int) -> list:
#         if number < 3:
#             return cls.PRIME_NUMBER_LIST
#         for num in range(2, number):
#             flag = 0
#             for x in range(2, num):
#                 if (num % x) == 0:
#                     flag = 1
#             if flag == 0:
#                 cls.PRIME_NUMBER_LIST.append(num)

#         return cls.PRIME_NUMBER_LIST


# prime_number_check: PrimeNumbers = PrimeNumbers.prime_numbers(3)
# print(prime_number_check)


# class BankAccount:
#     def __init__(self, balance=0) -> None:
#         self.balance = balance

#     def deposit(self, deposit_amount: float) -> float:
#         self.balance += deposit_amount

#     def withdraw(self, withdraw_amount: float) -> float:
#         if withdraw_amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= withdraw_amount

#     @classmethod
#     def from_balance(cls, starting_balance: float) -> "BankAccount":
#         new_balance = starting_balance
#         return cls(new_balance)

#     @staticmethod
#     def transfer(
#         account_one: "BankAccount", account_two: "BankAccount", amount: float
#     ) -> "BankAccount":
#         account_one.withdraw(amount)
#         account_two.deposit(amount)


# bank_acc_one = BankAccount()
# bank_acc_one.deposit(15.5)
# print(bank_acc_one.balance)
# bank_acc_one.withdraw(14)
# print(bank_acc_one.balance)

# bank_acc_three = BankAccount.from_balance(250)
# print(bank_acc_three.balance)
# bank_acc_four = BankAccount.from_balance(800)
# print(bank_acc_four.balance)

# BankAccount.transfer(bank_acc_four, bank_acc_three, 150)
# print(bank_acc_three.balance)

from typing import List


class SpaceStation:
    def __init__(self, astronauts: List[dict]) -> None:
        self.astronauts = astronauts
