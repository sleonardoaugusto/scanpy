import json


class Database:
    file = 'database.json'

    def save(self, data: dict):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
