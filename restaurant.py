from view import print_header, main_menu
from guest import input_reservation
from util import save_data, get_data, delete_data


def print_totals(total_num_adults: int, total_num_child: int, grand_total: int) -> None:
    print(f"\nTotal Number of Adults: {total_num_adults}")
    print(f"Total Number of Children: {total_num_child}")
    print(f"Grand Total: {grand_total}")


def print_reservation(info: list) -> None:
    print(
        f"{info[0]:<8}{info[1]},{info[2]:<8}{info[3]:<16}{info[4]:<27}{info[5]:<9}{info[6]:<8}"
    )


def print_reservations(reserve_list: list) -> None:
    if reserve_list:
        print("#\t DATE\t\t TIME\t\t NAME\t\t\t ADULTS\t CHILDREN")
        for info in reserve_list:
            print_reservation(info)


def print_report(info: list) -> None:
    print(
        f"{info[0]:<8}{info[1]},{info[2]:<8}{info[3]:<16}{info[4]:<27}{info[5]:<9}{info[6]:<8}\t{info[7]}",
        end="",
    )


def print_reports(reserve_list: list) -> None:
    total_num_adults: int = 0
    total_num_child: int = 0
    grand_total: int = 0
    for info in reserve_list:
        total_num_adults += int(info[5])
        total_num_child += int(info[6])
        grand_total += int(info[7])
        print_report(info)
    print_totals(total_num_adults, total_num_child, grand_total)


def prepare_report(reserve_list: list) -> None:
    if reserve_list:
        print("#\t DATE\t\t TIME\t\t NAME\t\t\t ADULTS\t CHILDREN\tSUBTOTAL")
        print_reports(reserve_list)


def get_user_input() -> str:
    while True:
        main_menu()
        user_input: str = input("\nEnter from the choices above: ").upper()
        if user_input.isalpha() and user_input in "ABCDE":
            return user_input
        else:
            print("Please choose from the choices only!!!")


class Restaurant:
    def __init__(self):
        self.__adult_rate: int = 500
        self.__children_rate: int = 300
        self.restaurant_db: str = "data.txt"

    def get_adult_rate(self) -> int:
        return self.__adult_rate

    def get_child_rate(self) -> int:
        return self.__children_rate

    def make_reservation(self) -> None:
        reservation_data_tuple = input_reservation()
        adult_total: int = reservation_data_tuple[3] * self.get_adult_rate()
        child_total: int = reservation_data_tuple[4] * self.get_child_rate()
        grand_total: int = adult_total + child_total

        reservation_data: tuple = (
            reservation_data_tuple[1],  # Date
            reservation_data_tuple[2],  # Time
            reservation_data_tuple[0],  # Name
            reservation_data_tuple[3],  # Number of Adults
            reservation_data_tuple[4],  # Number of Children
            grand_total,  # Grand Total
        )
        reservation_data: str = ", ".join(str(item) for item in reservation_data)

        if save_data(self.restaurant_db, reservation_data):
            print("DONE!!!")

    def view_reservation(self, view: str) -> None:
        reservations: list = get_data(self.restaurant_db)
        if view == "reservation":
            print_reservations(reservations)
        else:
            prepare_report(reservations)

    def delete_reservation(self) -> None:
        reservation_name = input("\nEnter the reservation name delete reservation: ")
        if delete_data(self.restaurant_db, reservation_name):
            print(f"Guest {reservation_name} deleted from the system.")

    def main(self) -> None:
        print_header()

        while True:
            user_input = get_user_input()
            if user_input == "A":
                print("\nView All Reservations")
                self.view_reservation("reservation")
            elif user_input == "B":
                print("\nMake Reservation")
                self.make_reservation()
            elif user_input == "C":
                print("Delete Reservation")
                self.view_reservation("reservation")
                self.delete_reservation()
            elif user_input == "D":
                print("\nGenerate Report")
                self.view_reservation("report")
            elif user_input == "E":
                break

        print("Thank You.")
