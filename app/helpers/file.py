import os

class File:
    @staticmethod
    def delete(path, file):
        try:
            os.remove(os.path.join(path + file))
        except FileNotFoundError:
            return 0

        return 1