"""A student and their registered subjects."""

from grader.subject import Subject


class Student:
    """Manage the subjects belonging to one student."""

    def __init__(self, student_id: str, name: str):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.subjects: dict[str, Subject] = {}

    def add_subject(self, subject: Subject) -> None:
        """Add a subject, rejecting duplicate codes."""
        if not isinstance(subject, Subject):
            raise TypeError("A Subject object is required.")
        if subject.subject_code in self.subjects:
            raise ValueError("Subject code is already registered.")
        self.subjects[subject.subject_code] = subject

    def remove_subject(self, subject_code: str) -> None:
        """Remove a subject by its code."""
        if subject_code not in self.subjects:
            raise KeyError("Subject not found.")
        del self.subjects[subject_code]

    def get_subject(self, subject_code: str) -> Subject:
        """Find a registered subject by its code."""
        if subject_code not in self.subjects:
            raise KeyError("Subject not found.")
        return self.subjects[subject_code]

    def iter_subjects(self):
        """Yield each subject belonging to the student."""
        yield from self.subjects.values()

    @property
    def average_score(self) -> float | None:
        """Return the mean score, or None for no subjects."""
        if not self.subjects:
            return None
        return sum(subject.score for subject in self.iter_subjects()) / len(self.subjects)

    def __str__(self) -> str:
        return f"{self.student_id} - {self.name} ({len(self.subjects)} subjects)"
