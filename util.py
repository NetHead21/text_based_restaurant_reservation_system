import os
from typing import Optional


def get_file_index(file_name: str) -> int:
    try:
        with open(file_name, "r") as file_reader:
            for count, _ in enumerate(file_reader):
                pass
            return count + 2
    except Exception:
        return 1


def save_data(file_name: str, guest_data: str) -> bool:
    try:
        with open(file_name, "a") as file_writer:
            entry_num: int = get_file_index(file_name)
            file_writer.write(f"{entry_num}, {guest_data}\n")

        return True

    except Exception as e:
        print(f"Error while writing file. {e}")
        return False


def get_data(file_name: str) -> list:
    try:
        with open(file_name, "r") as file_reader:
            return [data.split(",") for data in file_reader.readlines()]

    except Exception:
        print("No Records Retrieve.")
        return []


def remove_file(file_name: str) -> Optional[Exception]:
    try:
        os.remove(file_name)
    except Exception as e:
        return e


def delete_data(file_name: str, reservation_name: str) -> bool:
    reservations: list = get_data(file_name)
    remove_file(file_name)

    for reservation in reservations:
        reserve_data: list = [element.strip() for element in reservation]

        if reservation_name in reserve_data:
            continue

        guest_reserve_list = ", ".join(reserve_data[1:])
        save_data(file_name, guest_reserve_list)

    return True


if __name__ == "__main__":
    print(get_data("hotel.txt"))
