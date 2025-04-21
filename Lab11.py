import os
from matplotlib import pyplot as plt


def data_students(filename):
    students = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            student_id = line[:3]
            name = line[3:].strip()
            students[student_id] = name
    return students

def data_assignments(filename):
    assignments = {}
    name_to_id = {}
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        for i in range(0, len(lines), 3):
            name = lines[i]
            assignment_id = lines[i+1]
            points = int(lines[i+2])
            assignments[assignment_id] = (name, points)
            name_to_id[name] = assignment_id
    return assignments, name_to_id

def data_submissions(folder):
    submissions = {}
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        with open(filepath) as file:
            for line in file:
                student_id, assignment_id, percent = line.strip().split("|")
                submissions[(student_id, assignment_id)] = float(percent) / 100
    return submissions

def calculate_student_grade(student_name):
    student_ID = None
    for student_id, name in students.items():
        if name == student_name:
            student_ID = student_id
            break

    if student_ID is None:
        print("Student not found")
        return

    total_score = 0
    for assignment_id, (name, points) in assignments.items():
        percent = submissions.get((student_ID, assignment_id), 0)
        total_score += percent * points

    grade = round((total_score / 1000) * 100)
    print(f"{grade}%")

def assignment_statistics(assignment_name):
    if assignment_name not in assignment_name_to_id:
        print("Assignment not found")
        return

    assignment_id = assignment_name_to_id[assignment_name]
    points = assignments[assignment_id][1]

    scores = [
        submissions[(student_id, assignment_id)] * points
        for student_id in students
        if (student_id, assignment_id) in submissions
    ]

    if not scores:
        print("Assignment not found")
        return

    percentages = [round(score / points * 100) for score in scores]
    print(f"Min: {min(percentages)}%")
    print(f"Avg: {round(sum(percentages) // len(percentages))}%")
    print(f"Max: {max(percentages)}%")

def display_assignment_graph(assignment_name):
    if assignment_name not in assignment_name_to_id:
        print("Assignment not found")
        return

    assignment_id = assignment_name_to_id[assignment_name]
    points = assignments[assignment_id][1]

    scores = [
        submissions[(student_id, assignment_id)] * 100
        for student_id in students
        if (student_id, assignment_id) in submissions
    ]

    if not scores:
        print("Assignment not found")
        return

    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(f"{assignment_name} Score Distribution")
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")
    plt.show()

students = data_students("data/data/students.txt")
assignments, assignment_name_to_id = data_assignments("data/data/assignments.txt")
submissions = data_submissions("data/data/submissions")

def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph \n")

    selection = input("Enter your selection: ")

    # assignments = read_assignments_file()
    # submissions = read_submissions_file()

    if selection == "1":
        student_name = input("Enter the student's name: ")
        calculate_student_grade(student_name)

    elif selection == "2":
        assignment_name = input("What is the assignment name: ")
        assignment_statistics(assignment_name)

    elif selection == "3":
        assignment_name = input("What is the assignment name: ")
        display_assignment_graph(assignment_name)


if __name__ == "__main__":
    main()