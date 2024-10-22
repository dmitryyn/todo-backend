import json
import os


def print_with_indent(value, indent=0):
    indent = '\t' * indent
    print(f"{indent}{value}")

class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        res = {
        'title': self.title,
        'entries': [entry.json() for entry in self.entries]
        }
        return res

    @classmethod
    def from_json(cls, value:dict):
        new_entry = cls(value['title'])
        for item in value.get('entries', []):
            new_entry.add_entry(cls.from_json(item))
        return new_entry

    def save(self, path):
        content = self.json()
        filename = f'{self.title}.json'
        with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False)

    @classmethod
    def load(cls, filename):
        with open (filename, 'r') as f:
            content = json.load(f)
        return cls.from_json(content)
