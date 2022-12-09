import base64


class File:

    @staticmethod
    def convert_file_to_base64(file_path):
        with open(file_path, 'rb') as file:
            my_string = base64.b64encode(file.read())
        return my_string
