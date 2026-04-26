import os
import csv
import json
if os.path.exists("students.csv"):
    print("File found")
else:
    print("File does not exist")

if os.path.exists("output"):
    print("folder found")
else:
    os.makedirs("output")
    print("folder created")

students=[]
with open('students.csv', mode="r", encoding='utf-8')as f:
    reader=csv.DictReader(f)
    for row in reader:
        students.append(row)

print(f"\nTotal students:{len(students)}")
print(f"\nFirst 5 rows: ")
for s in students[:5]:
    print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")


low_sleep_gpas=[]
high_sleep_gpas=[]
for s in students:
    sleep=float(s['sleep_hours'])
    gpa=float(s['GPA'])
    if sleep<6:
        low_sleep_gpas.append(gpa)
    else:
        high_sleep_gpas.append(gpa)

avg_low=sum(low_sleep_gpas)/len(low_sleep_gpas)
avg_high=sum(high_sleep_gpas)/len(high_sleep_gpas)
diff=abs(avg_high-avg_low)
print("\nSleep vs GPA Analysis")
print("-" * 30)
print(f"Students sleeping < 6 hours : {len(low_sleep_gpas)}")
print(f"Average GPA (< 6 hours) : {round(avg_low, 2)}")
print(f"Students sleeping >= 6 hours : {len(high_sleep_gpas)}")
print(f"Average GPA (>= 6 hours) : {round(avg_high, 2)}")
print(f"\nDifference in avg GPA : {round(diff, 2)}")
print("-" * 30)

result={
    "analysis": "Sleep vs GPA",
    "total_students":len(students),
    "low_sleep":{
        "students":len(low_sleep_gpas),
        "avg_gpa": round(avg_low,2)
    },
    "high_sleep":{
        "students": len(high_sleep_gpas),
        "avg_gpa": round(avg_high,2)
    },
    "gpa_difference":round(diff,2)
}
with open('output/result.json','w') as f:
    json.dump(result,f,indent=4)
print("\nResult saved to output")

