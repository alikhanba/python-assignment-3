import csv


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_data(self):
        try:
            with open(self.filename, mode="r", encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def preview_data(self, n=5):
        print(f"First {n} rows:")
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)
