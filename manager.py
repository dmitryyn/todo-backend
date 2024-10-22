import os
from typing import List
from resources import Entry

class EntryManager:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for entry in self.entries:
            Entry.save(entry, self.data_path)

    def load(self):

        # if not os.path.isdir(self.data_path):
        #     os.makedirs(self.data_path)
        # else:

        for file in os.listdir(self.data_path):
            if file.endswith('json'):
                entry = Entry.load(os.path.join(self.data_path, file))
                self.entries.append(entry)
        return self

    def add_entry(self, title: str):
        self.title = title
        entry = Entry(title)
        self.entries.append(entry)


grocery_list = Entry('Products')
