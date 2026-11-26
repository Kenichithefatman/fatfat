"""One subject and its calculated grade."""


class Subject:
    """Keep a subject's name and validated score."""

    def __init__(self, subject_code: str, subject_name: str, score: int):
        if not isinstance(subject_code, str) or not subject_code.strip():
            raise ValueError("Subject code cannot be empty.")
        if not isinstance(subject_name, str) or not subject_name.strip():
            raise ValueError("Subject name cannot be empty.")
        self.subject_code = subject_code.strip()
        self.subject_name = subject_name.strip()
        self.score = score

    @property
    def score(self) -> int:
        """Return the validated score."""
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        if type(value) is not int or not 0 <= value <= 100:
            raise ValueError("Score must be an integer from 0 to 100.")
        self._score = value

    @property
    def grade(self) -> str:
        """Calculate a grade from the current score."""
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        return "F"

    def __str__(self) -> str:
        return f"{self.subject_code} - {self.subject_name}: {self.score} ({self.grade})"
