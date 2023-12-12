# ********************************************Encapsulation*************************************************f
from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class Base(ABC):
    def __init__(self, age: int, cost: float, year_built: int, weight: float) -> None:
        self.__age: int = age
        self.__cost: float = cost
        self.__year_built: int = year_built
        self.__weight: float = weight

    def get_spacecraft_info(self) -> str:
        return f"Space craft {self.__age} years old, costs around {self.__cost} USD, \n\
was built in {self.__year_built} and weights around {self.__weight} Kgs"

    @abstractmethod
    def get_full_report(self) -> None:
        pass


class SpaceShuttle(Base):
    EARTH_ORBIT_HEIGHT = 250

    def __init__(
        self,
        age: int,
        cost: float,
        year_built: int,
        weight: float,
        fuel_price: float,
        burn_rate: float,
        people_needed: int,
        base_salary: int,
    ) -> None:
        super().__init__(age, cost, year_built, weight)
        self.__fuel_price: float = fuel_price
        self.__burn_rate: float = burn_rate
        self.__people_needed: int = people_needed
        self.__base_slary: float = base_salary

    def get_burn_rate_variable(self) -> float:
        return 2500 / self.EARTH_ORBIT_HEIGHT

    def get_fuel_cost(self) -> float:
        fuel_cost = self.__fuel_price * self.__burn_rate * self.get_burn_rate_variable()
        return fuel_cost

    def get_people_expends(self) -> float:
        return self.__people_needed * self.__base_slary

    def get_full_report(self) -> float:
        fuel_cost = self.get_fuel_cost()
        people_cost = self.get_people_expends()
        total_cost = fuel_cost + people_cost
        spacecraft_info = self.get_spacecraft_info()
        logging.info(f"{spacecraft_info}")
        logging.info(f"Fuel costs for lifting this rocket would be {fuel_cost} USD")
        logging.info(f"Salary costs for lifting the rocket would be {people_cost} USD")
        logging.info(f"Total costs for lifting the rocket would be {total_cost} USD")
        print(
            f"{spacecraft_info}. Fuel costs for lifting this spacecraft would be {fuel_cost} USD \n\
Salary costs for lifting the rocket would be {people_cost} USD \n\
Total costs for lifting the rocket would be {total_cost} USD"
        )


space_cowboy = SpaceShuttle(
    age=25,
    cost=25000000.0,
    year_built=1989,
    weight=45000000,
    fuel_price=20.0,
    burn_rate=1500,
    people_needed=200,
    base_salary=100000,
)
# print(space_cowboy.get_fuel_cost())
space_cowboy.get_full_report()
