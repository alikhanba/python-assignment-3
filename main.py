import os
import csv
import json

class FileManager:
    def __init__(self,filename):
        self.filename=filename
    def check_files(self):
        if os.path.exists(self.filename):
         print("File found")
         return True
        else:
            print("File does not exist")
            return False
    def create_output_folder(self,folder='output'):
        if os.path.exists(folder):
            print("folder found")
        else:
            os.makedirs(folder)
            print("folder created")
        return True

class DataLoader:
    def __init__(self,filename):
        self.filename=filename
        self.students=[]

    def load_data(self):
        try:
            with open(self.filename, mode="r", encoding='utf-8')as f:
                reader=csv.DictReader(f)
                self.students=list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error:File '{self.filename}' not found.")
            return []


    def preview_data(self,n=5):
        print(f"Frist {n} rows:")
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-"*30)

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        # Base version — will be overridden in child classes
        print("Not implemented — use a child class")

    def print_results(self):
        # Base version — loops over result and prints each key-value pair
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class SleepAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        low_sleep_gpas = []
        high_sleep_gpas = []

        for s in self.students:
            try:
                sleep = float(s['sleep_hours'])
                gpa = float(s['GPA'])
                if sleep < 6:
                    low_sleep_gpas.append(gpa)
                else:
                    high_sleep_gpas.append(gpa)
            except ValueError:
                print(f"Warning: could not convert value for student {s.get('student_id')} — skipping row.")
                continue

        avg_low = sum(low_sleep_gpas) / len(low_sleep_gpas) if low_sleep_gpas else 0
        avg_high = sum(high_sleep_gpas) / len(high_sleep_gpas) if high_sleep_gpas else 0
        diff = abs(avg_high - avg_low)

        self.result = {
            "total_students": len(self.students),
            "low_sleep": {"students": len(low_sleep_gpas), "avg_gpa": round(avg_low, 2)},
            "high_sleep": {"students": len(high_sleep_gpas), "avg_gpa": round(avg_high, 2)},
            "gpa_difference": round(diff, 2)
        }

    def print_results(self):
        print("=" * 30)
        print("SLEEP VS GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"SleepAnalyser: Sleep vs GPA Analysis, {len(self.students)} students"



class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = []
        high_performers = 0

        for s in self.students:
            try:
                gpa = float(s['GPA'])
                gpas.append(gpa)
                if gpa > 3.5:
                    high_performers += 1
            except ValueError:
                print(f"Warning: could not convert GPA for student {s.get('student_id')} — skipping row.")
                continue

        self.result = {
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2) if gpas else 0,
            "max_gpa": round(max(gpas), 2) if gpas else 0,
            "min_gpa": round(min(gpas), 2) if gpas else 0,
            "high_performers": high_performers
        }

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"




class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser
        self.saver = saver

    def generate(self):
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report complete.")




class ResultSaver:
    def __init__(self,result,output_path):
        self.result=result
        self.output_path=output_path
    def save_json(self):
        try:
            with open(self.output_path,'w') as f:
                json.dump(self.result,f,indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving:{e}")

if __name__ == "__main__":
    fm = FileManager('students.csv')
    if not fm.check_files():
        exit()
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    students_data = dl.load_data()
    if not students_data:
        exit()
    dl.preview_data()

    analysers = [SleepAnalyser(students_data), GpaAnalyser(students_data)]

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)

    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()

    saver = ResultSaver(analysers[0].result, 'output/result.json')
    report = Report(analysers[0], saver)
    report.generate()







