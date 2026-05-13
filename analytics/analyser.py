class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
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
