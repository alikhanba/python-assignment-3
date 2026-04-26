import os
import csv
import json

class FileManagaer:
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
    def __init__(self,students):
        self.students=students
        self.result={}

    def analyse_sleep_vs_gpa(self):
        low_sleep_gpas=[]
        high_sleep_gpas=[]
        for s in self.students:
            try:
                sleep=float(s['sleep_hours'])
                gpa=float(s['GPA'])
                if sleep<6:
                    low_sleep_gpas.append(gpa)
                else:
                    high_sleep_gpas.append(gpa)
            except ValueError:
                print(f"Warning: could not convert value for student{s.get('student_id')} — skipping row.")
                continue
        avg_low=sum(low_sleep_gpas)/len(low_sleep_gpas) if low_sleep_gpas else 0
        avg_high=sum(high_sleep_gpas)/len(high_sleep_gpas) if high_sleep_gpas else 0
        diff=abs(avg_high-avg_low)
        self.result= {
            "total_students": len(self.students),
            "low_sleep":{"students": len(low_sleep_gpas),"avg_gpa":round(avg_low,2)},
            "high_sleep":{"students": len(high_sleep_gpas),"avg_gpa":round(avg_high,2)},
            "gpa_difference": round(diff,2)
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("Sleep vs GPA Analysis")
        print("-" * 30)
        res = self.result
        print(f"Students sleeping < 6 hours : {res['low_sleep']['students']} avg GPA: {res['low_sleep']['avg_gpa']}")
        print(f"Students sleeping >= 6 hours : {res['high_sleep']['students']} avg GPA: {res['high_sleep']['avg_gpa']}")
        print(f"GPA difference : {res['gpa_difference']}")
        print("-" * 30)

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

if __name__== "__main__":
    fm=FileManagaer('students.csv')
    if not fm.check_files():
        exit()
    fm.create_output_folder()

    dl=DataLoader('students.csv')
    students_data=dl.load_data()
    if students_data:
        dl.preview_data()
        analyser=DataAnalyser(students_data)
        analyser.analyse_sleep_vs_gpa()
        analyser.print_results()

        saver=ResultSaver(analyser.result,'output/result.json')
        saver.save_json()








