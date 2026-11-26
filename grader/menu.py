"""Terminal menus for administrators and students."""

from grader.manager import StudentManager
from grader.storage import load_students, save_students
from grader.student import Student
from grader.subject import Subject


def ask_score(prompt: str) -> int:
    """Read an integer score; Subject checks its range."""
    try:
        return int(input(prompt).strip())
    except ValueError as error:
        raise ValueError("Score must be an integer from 0 to 100.") from error


def require_student(manager: StudentManager) -> Student:
    """Ask for an ID and return the matching student."""
    student_id = input("Enter student ID: ").strip()
    if not student_id:
        raise ValueError("Student ID cannot be empty.")
    student = manager.find_student(student_id)
    if student is None:
        raise KeyError("Student not found.")
    return student


def save_change(manager: StudentManager) -> None:
    """Persist a change, reverting memory if saving fails."""
    try:
        save_students(manager)
    except (OSError, ValueError):
        try:
            manager.students = load_students().students
        except (OSError, ValueError):
            manager.students = {}
        raise


def show_subjects(student: Student) -> None:
    """Display registered subjects using the custom generator."""
    if not student.subjects:
        print("No subjects registered.")
        return
    for subject in student.iter_subjects():
        print(f"{subject.subject_code:<10} {subject.subject_name:<18} "
              f"{subject.score:>5} {subject.grade:>7}")


def register_student(manager: StudentManager) -> None:
    """Register and save a new student."""
    student = Student(input("Enter student ID: "), input("Enter student name: "))
    manager.add_student(student)
    save_change(manager)
    print("Student registered successfully.")


def add_subject(manager: StudentManager) -> None:
    """Register a subject for a selected student."""
    student = require_student(manager)
    code = input("Enter subject code: ")
    name = input("Enter subject name: ")
    score = ask_score("Enter score: ")
    subject = Subject(code, name, score)
    student.add_subject(subject)
    save_change(manager)
    print(f"Subject added successfully. Grade: {subject.grade}")


def update_score(manager: StudentManager) -> None:
    """Change a registered subject's score."""
    student = require_student(manager)
    show_subjects(student)
    code = input("Enter subject code: ").strip()
    score = ask_score("Enter new score: ")
    manager.update_score(student.student_id, code, score)
    save_change(manager)
    print(f"Score updated. Grade: {student.get_subject(code).grade}")


def view_all(manager: StudentManager) -> None:
    """List all registered students."""
    print(f"{'Student ID':<15} {'Name':<20} Subjects")
    print("-" * 45)
    for student in manager.get_all_students():
        print(f"{student.student_id:<15} {student.name:<20} {len(student.subjects)}")
    print(f"Total students: {len(manager.students)}")


def delete_subject(manager: StudentManager) -> None:
    """Delete a subject after confirmation."""
    student = require_student(manager)
    show_subjects(student)
    code = input("Enter subject code: ").strip()
    student.get_subject(code)
    if input("Delete this subject? (y/n): ").strip().lower() != "y":
        print("Deletion cancelled.")
        return
    student.remove_subject(code)
    save_change(manager)
    print("Subject deleted.")


def delete_student(manager: StudentManager) -> None:
    """Delete a student after confirmation."""
    student = require_student(manager)
    print(student)
    if input("Delete this student? (y/n): ").strip().lower() != "y":
        print("Deletion cancelled.")
        return
    manager.remove_student(student.student_id)
    save_change(manager)
    print("Student deleted.")


def admin_menu(manager: StudentManager) -> None:
    """Run administrator actions until the user returns."""
    actions = {
        "1": register_student, "2": add_subject, "3": update_score,
        "4": view_all, "5": delete_subject, "6": delete_student,
    }
    while True:
        print("\n============== ADMIN MENU ==============")
        print("1. Register Student\n2. Add Subject and Score")
        print("3. Update Subject Score\n4. View All Students")
        print("5. Delete Subject\n6. Delete Student\n7. Return to Main Menu")
        choice = input("Enter your choice: ").strip()
        if choice == "7":
            return
        if choice not in actions:
            print("Invalid choice. Please try again.")
            continue
        try:
            actions[choice](manager)
        except (ValueError, KeyError, OSError) as error:
            print(f"Error: {error.args[0]}")


def student_menu(manager: StudentManager) -> None:
    """Let students view results without changing records."""
    while True:
        try:
            student = require_student(manager)
            print("\n============ ACADEMIC RESULTS ============")
            print(f"Student ID: {student.student_id}")
            print(f"Student Name: {student.name}\n")
            print(f"{'Code':<10} {'Subject':<18} {'Score':>5} {'Grade':>7}")
            print("-" * 44)
            show_subjects(student)
            print(f"Total Subjects: {len(student.subjects)}")
            average = student.average_score
            print(f"Average Score: {average:.2f}" if average is not None
                  else "Average Score: N/A")
        except (ValueError, KeyError) as error:
            print(f"Error: {error.args[0]}")
        if input("Search again? (y/n): ").strip().lower() != "y":
            return


def run_menu(manager: StudentManager) -> None:
    """Run the main menu until exit or end of input."""
    while True:
        print("\n========================================")
        print("          STUDENT GRADER SYSTEM")
        print("========================================")
        print("1. Admin Mode\n2. Student Mode\n3. Exit")
        try:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                admin_menu(manager)
            elif choice == "2":
                student_menu(manager)
            elif choice == "3":
                print("Goodbye!")
                return
            else:
                print("Invalid choice. Please try again.")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return
