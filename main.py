from check_functions.fetch_values import fetch_values
import schedule
import time


def create_file():
    """
    :return: doesn't return anything, creates file
    """
    if fetch_values():
        file, extension = fetch_values()
        file = open(f'{file}.{extension}', "w")


schedule.every(1).minutes.do(create_file)

while True:
    schedule.run_pending()
    time.sleep(1)
