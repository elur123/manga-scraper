import json
import os

class HarimangaSelector:

    def _selector(self, fileName: str):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, fileName)

        data = None
        with open(file_path, "r") as file:
            data = json.load(file)

        return data