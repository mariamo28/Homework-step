import json
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    @staticmethod
    def read_from_json(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        students = []
        for student_data in data['students']:
            student = Student(
                student_data['name'],
                student_data['age'],
                student_data['grades']
            )
            students.append(student)
        return students

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    @staticmethod
    def write_averages_to_json(students, output_filename):
        averages = {}
        for student in students:
            averages[student.name] = student.calculate_average()

        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(averages, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    students = Student.read_from_json('students.json')

    print("სტუდენტები:")
    for student in students:
        print(f"{student.name}, {student.age} წლის, საშუალო ქულა: {student.calculate_average()}")