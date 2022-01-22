from check_functions.json_check import json_check
import json


def fetch_values():
    """
    :return: filename and extension if exists, else => False

    """

    file = json_check()

    if file:
        f = open(file, "r")

        json_data = f.read()

        if json_data:
            final_data = json.loads(json_data)
            filename = final_data.get("file")
            extension = final_data.get("extension")
            if filename and extension:
                return filename, extension
            else:
                return False
        else:
            return False
    else:
        return False
