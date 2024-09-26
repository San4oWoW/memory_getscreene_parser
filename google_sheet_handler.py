import json
import os
import time

import gspread


class Table:
    def __init__(self):
        self.name = "data.json"
        self.gc = gspread.service_account(filename=os.path.abspath("credentials.json"))
        self.sh = self.gc.open_by_key("")
        self.worksheet = self.sh.sheet1

    def write_string(self, string: list):
        self.worksheet.append_row(string)

    def read_json(self) -> list:
        with open(self.name, 'r', encoding='utf-8') as f:
            return json.load(f)

    def clear_table(self):
        self.worksheet.clear()

    def handle_json_for_table(self):
        self.write_string(list(self.read_json()[1].keys()))
        for i in self.read_json():
            self.write_string(list(i.values()))
            time.sleep(1)





# worksheet.clear()
