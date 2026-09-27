import csv
import os

csv_filepath = os.path.join("automated_report_card_generator", "grades.csv")
reports_dir = "report_cards"

# -- Created class
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks # encapuslation 

    def get_marks(self):
        return self.__marks.copy()

    def display_summary(self):
        print(f"Student Name: {self.name}\nStudent Roll Number: {self.roll_no}\nStudent Marks: {self.__marks}")

    def calc_average(self):
        if not self.__marks:
            return 0.0
        return sum(self.__marks.values())/len(self.__marks)

    def calc_grade(self):
        avg = self.calc_average()
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 40:
            return 'D'
        else:
            return 'F'

    def has_passed(self):
        marks = self.__marks.values()
        for m in marks:
            if m < 40:
                return False
        return True

    def report_card_generator(self, output_dir = reports_dir):
        os.makedirs(output_dir, exist_ok = True)
        file_path = os.path.join(output_dir, f"{self.roll_no}_report.txt")

        with open(file_path, 'w') as f:
            f.write('=' * 40 + "\n")
            f.write("         REPORT INFORMATION         ")
            f.write("=" * 40 + "\n")
            f.write(f"Roll Number: {self.roll_no}\n")
            f.write(f"Student Name: {self.name}\n")
            f.write("-" * 40)
            f.write(" SUBJECT SCORES: \n")
            for sub, sco in self.__marks.items():
                f.write(f" - {sub:<15}: {sco}/100\n")
            f.write("-" * 40)
            f.write(f"Average Score: {self.calc_average():.2f}\n")
            f.write(f"Overall Grade: {self.calc_grade()}\n")
            status = "PASSED" if self.has_passed() else "FAILED"
            f.write(f"Final Result: {status}\n")
            f.write("=" * 40 + "\n")
        print(f"Generated report card for {self.name} ({self.roll_no}) -> {file_path}")


# --- Create a sample csv if there is no file existed
def ensure_sample_csv(filename):
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok = True)

    if not os.path.exists(filename):
        sample_rows = [
            {"RollNo": "101", "Name": "Alice Smith", "Math": "92", "Science": "88", "English": "95"},
            {"RollNo": "102", "Name": "Bob Jones", "Math": "74", "Science": "65", "English": "80"},
            {"RollNo": "103", "Name": "Charlie Brown", "Math": "35", "Science": "50", "English": "60"},
            {"RollNo": "104", "Name": "Dana Scully", "Math": "corrupt", "Science": "90", "English": "90"},
        ]

        with open(filename, 'w', newline = '') as f:
            writer = csv.DictWriter(f, fieldnames = ["RollNo", "Name", "Math", "Science", "English"])
            writer.writeheader()
            writer.writerows(sample_rows)
        print(f"Sample CSV created at {filename}")


def load_students(filename):
    subject_scores = {}
    stud_list = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row_num, r in enumerate(reader, start = 2):
                try:
                    name = r["Name"].strip()
                    roll_no = r["RollNo"].strip()

                    # Dynamic score parsing (excluding metadata columns)
                    subject_scores = {}
                    for col, val in r.items():
                        if col not in ("RollNo", "Name") and col is not None:
                            subject_scores[col] = int(val)

                    student = Student(name, roll_no, subject_scores)
                    stud_list.append(student)

                except (ValueError, KeyError, AttributeError):
                    print(f"⚠️  Skipping row {row_num} (Name: {r.get('Name')}): Corrupted or invalid score data.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    return stud_list

def main():
    ensure_sample_csv(csv_filepath)

    print("\n--- Loading Students from CSV ---")
    students = load_students(csv_filepath)
    print(f"\nSuccessfully loaded {len(students)} student(s).\n")

    print("--- Generating Report Cards ---")
    for s in students:
        s.display_summary()
        s.report_card_generator()

if __name__ == "__main__":
    main()
   
