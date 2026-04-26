import os
import csv
import json
def check_files():

    if os.path.exists("students.csv"):
        print("File found")
    else:
        print("File does not exist")
        return False

    if os.path.exists("output"):
        print("folder found")
    else:
        os.makedirs("output")
        print("folder created")
    return True


students=[]
def load_data(filename):
    try:
        with open(filename, mode="r", encoding='utf-8')as f:
            reader=csv.DictReader(f)
            students=list(reader)
            print(f"Data loaded successfully: {len(students)} students")
            return students
    except FileNotFoundError:
        print(f"Error:File '{filename}' not found.")
        return []


def preview_data(students,n=5):
    print(f"Frist {n} rows:")
    for s in students[:n]:
        print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
    print("-"*30)

def analyse_sleep_vs_gpa(students):
    low_sleep_gpas=[]
    high_sleep_gpas=[]
    for s in students:
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
    avg_low=sum(low_sleep_gpas)/len(low_sleep_gpas)
    avg_high=sum(high_sleep_gpas)/len(high_sleep_gpas)
    diff=abs(avg_high-avg_low)
    return {
        "total_students": len(students),
        "low_sleep":{"students": len(low_sleep_gpas),"avg_gpa":round(avg_low,2)},
        "high_sleep":{"students": len(high_sleep_gpas),"avg_gpa":round(avg_high,2)},
        "gpa_difference": round(diff,2)
    }

if check_files():
    all_students=load_data('students.csv')
    if all_students:
        preview_data(all_students)
        result=analyse_sleep_vs_gpa(all_students)
        print("\nSleep vs GPA Analysis")
        print("-" * 30)
        print(f"Students sleeping < 6 hours : {result['low_sleep']['students']}")
        print(f"Average GPA (< 6 hours) : {result['low_sleep']['avg_gpa']}")
        print(f"Students sleeping >= 6 hours : {result['high_sleep']['students']}")
        print(f"Average GPA (>= 6 hours) : {result['high_sleep']['avg_gpa']}")
        print(f"Difference in avg GPA : {result['gpa_difference']}")
        print("-" * 30)

        print("\nLambda MAp Filter")
        print("-"*30)

        low_sleep_list=list(filter(lambda s: float(s['sleep_hours'])<6,all_students))
        print(f"Students with sleep,6 hrs:{len(low_sleep_list)}")

        gpa_values=list(map(lambda s: float(s['GPA']),all_students))
        print(f"GPA values (first 5): {gpa_values[:5]}")

        stressed=list(filter(lambda s: float(s['mental_stress_level'])>7,all_students))
        print(f"Students with stress > 7 : {len(stressed)}")
        print("-" * 30)

        with open('output/result.json','w') as f:
            json.dump(result,f,indent=4)






