# ********************************************Encapsulation*************************************************f
# from abc import ABC, abstractmethod
# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     filename="data.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%d/%m/%Y %H:%M:%S",
# )


# class Base(ABC):
#     def __init__(self, age: int, cost: float, year_built: int, weight: float) -> None:
#         self.__age: int = age
#         self.__cost: float = cost
#         self.__year_built: int = year_built
#         self.__weight: float = weight

#     def get_spacecraft_info(self) -> str:
#         return f"Space craft {self.__age} years old, costs around {self.__cost} USD, \n\
# was built in {self.__year_built} and weights around {self.__weight} Kgs"

#     @abstractmethod
#     def get_full_report(self) -> None:
#         pass


# class SpaceShuttle(Base):
#     EARTH_ORBIT_HEIGHT = 250

#     def __init__(
#         self,
#         age: int,
#         cost: float,
#         year_built: int,
#         weight: float,
#         fuel_price: float,
#         burn_rate: float,
#         people_needed: int,
#         base_salary: int,
#     ) -> None:
#         super().__init__(age, cost, year_built, weight)
#         self.__fuel_price: float = fuel_price
#         self.__burn_rate: float = burn_rate
#         self.__people_needed: int = people_needed
#         self.__base_slary: float = base_salary

#     def get_burn_rate_variable(self) -> float:
#         return 2500 / self.EARTH_ORBIT_HEIGHT

#     def get_fuel_cost(self) -> float:
#         fuel_cost = self.__fuel_price * self.__burn_rate * self.get_burn_rate_variable()
#         return fuel_cost

#     def get_people_expends(self) -> float:
#         return self.__people_needed * self.__base_slary

#     def get_full_report(self) -> float:
#         fuel_cost = self.get_fuel_cost()
#         people_cost = self.get_people_expends()
#         total_cost = fuel_cost + people_cost
#         spacecraft_info = self.get_spacecraft_info()
#         logging.info(f"{spacecraft_info}")
#         logging.info(f"Fuel costs for lifting this rocket would be {fuel_cost} USD")
#         logging.info(f"Salary costs for lifting the rocket would be {people_cost} USD")
#         logging.info(f"Total costs for lifting the rocket would be {total_cost} USD")
#         print(
#             f"{spacecraft_info}. Fuel costs for lifting this spacecraft would be {fuel_cost} USD \n\
# Salary costs for lifting the rocket would be {people_cost} USD \n\
# Total costs for lifting the rocket would be {total_cost} USD"
#         )


# space_cowboy = SpaceShuttle(
#     age=25,
#     cost=25000000.0,
#     year_built=1989,
#     weight=45000000,
#     fuel_price=20.0,
#     burn_rate=1500,
#     people_needed=200,
#     base_salary=100000,
# )
# # print(space_cowboy.get_fuel_cost())
# space_cowboy.get_full_report()


# **********************************Method Chaining*******************************************


# class Person:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.name_length = None
#         self.email = None

#     def set_name_length(self) -> "Person":
#         self.name_length = len(self.name)
#         return self

#     def create_email(self, surname: str) -> "Person":
#         DEFAULT_EMAIL_PROVIDER = "@yahoo.com"
#         self.email = self.name + "." + surname + DEFAULT_EMAIL_PROVIDER
#         return self


# person = Person("Vytautas")
# person.set_name_length().create_email("Kestutaitis")
# print(f"Email: {person.email}\nName length: {person.name_length}")


# class A:
#     def __init__(self, value: int) -> None:
#         self.value = value

#     def increment(self) -> None:
#         self.value += 1


# class C:
#     def __init__(self, lempa) -> None:
#         self.lempa = lempa


# class B(A, C):
#     def __init__(self, value: int, step: int) -> None:
#         super().__init__(value=value)
#         C.__init__(self, lempa=step)
#         self.step = step

#     def increment(self) -> None:
#         super().increment()
#         self.value += self.step


# b = B(5, 3)
# b.increment()
# print(b.value)  # output: 9


# class Person:
#     def __init__(self) -> None:
#         self.name = None
#         self.age = None

#     def set_name(self, name: str) -> "Person":
#         self.name = name
#         return self

#     def set_age(self, age: int) -> "Person":
#         self.age = age
#         return self


# person = Person()

# person.set_name("Algirdas").set_age(27)

# print(f"Name: {person.name}\nAge: {person.age}")


# class Currency:
#     EURAI = "EUR"

#     def __init__(self) -> None:
#         self.code = None
#         self.amount = None
#         self.exchange_rate = None
#         self.new_amount = None

#     def set_code(self, code: str) -> "Currency":
#         self.code = code
#         return self

#     def set_amount(self, amount: float) -> "Currency":
#         self.amount = amount
#         return self

#     def set_new_amount(self, new_amount: float) -> "Currency":
#         self.new_amount = new_amount
#         return self

#     def set_exchange_rate(self, exchange_rate: float) -> "Currency":
#         self.exchange_rate = exchange_rate
#         return self

#     def convert(self, code: str, exchange_rate: float) -> float:
#         self.set_code(code=code)
#         self.set_exchange_rate(exchange_rate=exchange_rate)
#         converted = self.amount * self.exchange_rate
#         return converted

#     def __str__(self) -> str:
#         return f"{self.amount} of currency {self.EURAI} is equal {self.new_amount} of currency {self.code}"


# eur = Currency()
# eur.set_code("EUR").set_amount(1000)
# eur.set_new_amount(eur.convert("USD", 1.2))
# print(eur)
