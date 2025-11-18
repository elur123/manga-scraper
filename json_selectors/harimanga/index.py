import json
import os

class HarimangaSelector:

    def search_selector(self):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "search.json")

        data = None
        with open(file_path, "r") as file:
            data = json.load(file)

        return data