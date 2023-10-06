def printLine():
    print("=" * 33)


def print_header() -> None:
    printLine()
    print("     RESTAURANT RESERVATION SYSTEM")
    printLine()


def main_menu() -> None:
    print("\n")
    printLine()
    print("Please choose from the following: ")
    printLine()
    print("A - View All Reservations")
    print("B - Make Reservation")
    print("C - Delete Reservation")
    print("D - Generate Report")
    print("E - Exit the program")
