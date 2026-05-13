from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import SleepAnalyser, GpaAnalyser


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
