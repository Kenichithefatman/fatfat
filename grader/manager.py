"""Operations on the collection of students."""

from grader.student import Student


class StudentManager:
    """Find, add, remove, and update students without doing I/O."""

    def __init__(self):
        self.students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        """Register one student with a unique ID."""
        if not isinstance(student, Student):
            raise TypeError("A Student object is required.")
        if student.student_id in self.students:
            raise ValueError("Student ID is already registered.")
        self.students[student.student_id] = student

    def remove_student(self, student_id: str) -> None:
        """Delete a student by ID."""
        if student_id not in self.students:
            raise KeyError("Student not found.")
        del self.students[student_id]

    def find_student(self, student_id: str) -> Student | None:
        """Return the matching student, or None."""
        return self.students.get(student_id)

    def get_all_students(self) -> list[Student]:
        """Return all registered students."""
        return list(self.students.values())

    def update_score(self, student_id: str, subject_code: str, score: int) -> None:
        """Update a score through the Subject property setter."""
        student = self.find_student(student_id)
        if student is None:
            raise KeyError("Student not found.")
        student.get_subject(subject_code).score = score
