from datetime import datetime
from Engine import Engine
import os

# default csv file to read if user doesn't have csv file of their own
DEFAULT_CSV = "FilesToDelete.csv"

def get_date() -> str:
    """Gets user input for date in which to delete a file"""
    while True:
        user_date = input("Type a date in \"YYYY-MM-DD 00:00:00:000\" (year, month, day, hour, minutes, seconds, and milliseconds): ")
        print()
        try:
            datetime.fromisoformat(user_date)
            return user_date
        except ValueError:
            print(f"{user_date} is not valid")


def get_path() -> str:
    """Gets user input for file to delete"""
    while True:
        user_path = input("Type a path to file/directories to delete: ")
        print()
        if os.path.exists(user_path):
            return user_path
        else:
            print(f"{user_path} is not valid")


def get_csv() -> str:
    """Gets user input for csv file to read for Engine object
    
    It will return DEFAULT_CSV if user doesn't provide input
    """
    while True:
            csv_path = input("Type the path of csv file to read (hit Enter to use default one): ")
            print()
            if len(csv_path) == 0:
                return DEFAULT_CSV
            else:
                if os.path.exists(csv_path):
                    return csv_path
                else:
                    print(f"{csv_path} is not valid")


def main() -> None: 
    """The main program"""
    # initializing Engine by reading csv file
    csv_path = get_csv()
    E = Engine(csv_path)
    path_and_date = {}
    
    # printing schedules
    print(E)
    print()

    # getting user input
    add_input = input("Do you want to add a file to delete? (type y for yes, hit enter to skip) ")
    print()
    while add_input == "y":
        user_path = get_path()
        user_date = get_date()
        path_and_date[user_path] = user_date
        add_input = input("Do you want to add another file to delete? (type y for yes, hit enter to skip) ")
        print()

    # adding the user input to Engine
    for p, d in path_and_date.items():
        E.add_file_to_delete(p, d)

    # deleting files
    E.delete()

    # printing schedules
    print(E)
    print()

if __name__ == "__main__":
    main()