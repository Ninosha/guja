from check_functions.fetch_values import fetch_values
import schedule
import time


def create_file():
    """
    :return:  creates a file and returns True if so
    """

    if fetch_values():
        file, extension = fetch_values()
        open(f'{file}.{extension}', "w")
        return True
    else:
        print("error")
        return False


schedule.every(1).minutes.do(create_file)

while True:
    schedule.run_pending()
    time.sleep(1)
