from dataclasses import dataclass, astuple
import datetime


@dataclass
class Guest:
    name: str


@dataclass
class Reservation(Guest):
    date: str
    time: str
    number_adults: int
    number_children: int

    def __post_init__(self) -> None:
        month, day, year = tuple(map(int, self.date.split("/")))
        date_format = datetime.date(year, month, day)
        final_date = date_format.strftime("%b %d, %Y")
        self.date = final_date

    @property
    def get_info(self) -> tuple:
        return astuple(self)


def get_input() -> tuple:
    name: str = input("Enter guest name: ")
    date: str = input("Enter the reservation date ex: '9/28/2023': ")
    time: str = input("Enter the reservation time ex: '10:30AM': ")
    number_adults: int = int(input("Enter number of adults: "))
    number_children: int = int(input("Enter number of children: "))
    return (name, date, time, number_adults, number_children)


def input_reservation() -> tuple:
    name, date, time, number_adults, number_children = get_input()
    reserve = Reservation(name, date, time, number_adults, number_children)
    return reserve.get_info


if __name__ == "__main__":
    # reserve = Reservation("Juniven", "9/27/2013", "10:00AM", 2, 3)
    # infos = reserve.get_info
    # print(infos)
    print(input_reservation())
