# class Circle:
#     PI = 3.14159

#     def __init__(self, radius: float) -> None:
#         self.radius = radius

#     def area(self) -> float:
#         return Circle.calculate_area(self.radius)

#     @staticmethod
#     def calculate_area(radius: float) -> float:
#         return Circle.PI * radius ** 2

# from abc import ABC, abstractmethod


# class Temperature(ABC):
#     KELVIN_CELSIUS = 273.15
#     KELVIN_FAHRENHEIT = 458.87

#     @abstractmethod
#     def kelvins_to_celsius(self) -> float:
#         pass

#     @abstractmethod
#     def kelvins_to_fahrenheit(self) -> float:
#         pass


# class Kelvins(Temperature):

#     @staticmethod
#     def kelvins_to_celsius(temperature_in_kelvins: float) -> float:
#         return temperature_in_kelvins - Temperature.KELVIN_CELSIUS

#     @staticmethod
#     def kelvins_to_fahrenhei(temperature_in_kelvins: float) -> float:
#         return temperature_in_kelvins - Temperature.KELVIN_FAHRENHEIT


# print(Kelvins.kelvins_to_celsius(300))
# print(Kelvins.kelvins_to_fahrenhei(400))


# class Units:

#     def __init__(self, feet: float, inches: float, miles: float, yards: float, pounds: float) -> None:
#         self.feet = feet
#         self.inches = inches
#         self.miles = miles
#         self.yards = yards
#         self.pounds = pounds

#     @staticmethod
#     def feet_to_meeters(feet: float) -> float:


# class TimeUtils:
#     @staticmethod
#     def time_to_seconds(time_string: str) -> int:
#         time_list = time_string.split(":")
#         sec_hour = int(time_list[0]) * 3600
#         sec_min = int(time_list[1]) * 60
#         sec_sec = int(time_list[2])
#         return sec_hour + sec_min + sec_sec


# print(TimeUtils.time_to_seconds("23:05:13"))

# from typing import List


# class Employee:
#     def __init__(self, name: str, salary: int) -> None:
#         self.name = name
#         self.salary = salary

#     @staticmethod
#     def calculate_payroll(list_of_instances: List["Employee"]) -> int:
#         return sum(member.salary for member in list_of_instances)


# empl_one = Employee("Jonas", 45000)
# empl_two = Employee("Algirdas", 25000)
# empl_three = Employee("Kazkas", 11000)

# list_of_empl = [empl_one, empl_two, empl_three]

# print(Employee.calculate_payroll(list_of_empl))

