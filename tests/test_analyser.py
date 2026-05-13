# File found
# Folder found
# Data loaded successfully: 10000 students
# First 5 rows:
# S00001 | 23 | Female | Germany | GPA: 3.81
# S00002 | 26 | Female | USA | GPA: 3.46
# S00003 | 18 | Female | Canada | GPA: 4.0
# S00004 | 20 | Male | Australia | GPA: 3.77
# S00005 | 28 | Female | Australia | GPA: 4.0
# ------------------------------
# ------------------------------
# Running all analysers:
# ------------------------------
# SleepAnalyser: Sleep vs GPA Analysis, 10000 students
# ==============================
# SLEEP VS GPA ANALYSIS REPORT
# ==============================
# total_students: 10000
# low_sleep: {'students': 1818, 'avg_gpa': 3.48}
# high_sleep: {'students': 8182, 'avg_gpa': 3.65}
# gpa_difference: 0.17
# ==============================
# GpaAnalyser: GPA Statistics, 10000 students
# ==============================
# GPA ANALYSIS REPORT
# ==============================
# total_students: 10000
# average_gpa: 3.62
# max_gpa: 4.0
# min_gpa: 1.92
# high_performers: 6557
# ==============================
# Generating report...
# ==============================
# SLEEP VS GPA ANALYSIS REPORT
# ==============================
# total_students: 10000
# low_sleep: {'students': 1818, 'avg_gpa': 3.48}
# high_sleep: {'students': 8182, 'avg_gpa': 3.65}
# gpa_difference: 0.17
# ==============================
# Result saved to output/result.json
# Report complete.
#test_analyse_twice (tests.test_analyser.TestSleepAnalyser.test_analyse_twice) ... ok
#test_result_has_required_keys (tests.test_analyser.TestSleepAnalyser.test_result_has_required_keys) ... ok
#test_result_is_not_empty (tests.test_analyser.TestSleepAnalyser.test_result_is_not_empty) ... ok
#test_total_students (tests.test_analyser.TestSleepAnalyser.test_total_students) ... ok
#----------------------------------------------------------------------
#Ran 4 tests in 0.001s

#OK

import unittest
from analytics.analyser import SleepAnalyser


class TestSleepAnalyser(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"GPA": "3.8", "sleep_hours": "7", "country": "USA",
             "final_exam_score": "95", "study_hours_per_day": "4"},
            {"GPA": "2.5", "sleep_hours": "5", "country": "India",
             "final_exam_score": "72", "study_hours_per_day": "2"},
            {"GPA": "3.9", "sleep_hours": "8", "country": "USA",
             "final_exam_score": "98", "study_hours_per_day": "5"},
            {"GPA": "1.8", "sleep_hours": "4", "country": "Canada",
             "final_exam_score": "55", "study_hours_per_day": "1"},
            {"GPA": "3.5", "sleep_hours": "6", "country": "India",
             "final_exam_score": "88", "study_hours_per_day": "3"},
        ]

    def test_result_is_not_empty(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("low_sleep", analyser.result)
        self.assertIn("high_sleep", analyser.result)
        self.assertIn("gpa_difference", analyser.result)

    def test_analyse_twice(self):
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)


if __name__ == '__main__':
    unittest.main()