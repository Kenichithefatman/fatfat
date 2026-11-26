"""Load and atomically save student records as JSON."""

import json
import os
import tempfile
from pathlib import Path

from grader.manager import StudentManager
from grader.student import Student
from grader.subject import Subject

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "data" / "students.json"


def load_students(path: Path = DEFAULT_PATH) -> StudentManager:
    """Rebuild students from JSON; reject corrupt or invalid records."""
    path = Path(path)
    manager = StudentManager()
    try:
        with path.open("r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        return manager
    except (json.JSONDecodeError, UnicodeError) as error:
        raise ValueError(f"Invalid data file: {error}") from error

    try:
        if not isinstance(records, dict):
            raise TypeError("Expected a student dictionary.")
        for student_id, record in records.items():
            if not isinstance(record, dict) or set(record) != {"name", "subjects"}:
                raise ValueError("Invalid student record.")
            if not isinstance(record["subjects"], dict):
                raise TypeError("Invalid subjects dictionary.")
            student = Student(student_id, record["name"])
            if student.student_id != student_id:
                raise ValueError("Invalid student ID key.")
            for code, item in record["subjects"].items():
                if not isinstance(item, dict) or set(item) != {"name", "score"}:
                    raise ValueError("Invalid subject record.")
                subject = Subject(code, item["name"], item["score"])
                if subject.subject_code != code:
                    raise ValueError("Invalid subject code key.")
                student.add_subject(subject)
            manager.add_student(student)
    except (TypeError, ValueError) as error:
        raise ValueError(f"Invalid data file: {error}") from error
    return manager


def save_students(manager: StudentManager, path: Path = DEFAULT_PATH) -> None:
    """Write valid records to a temporary file, then replace the original."""
    path = Path(path)
    if path.exists():
        load_students(path)  # Do not replace a corrupted file.
    records = {}
    for student_id, student in manager.students.items():
        records[student_id] = {
            "name": student.name,
            "subjects": {
                code: {"name": subject.subject_name, "score": subject.score}
                for code, subject in student.subjects.items()
            },
        }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=".students-", suffix=".tmp", delete=False,
        ) as file:
            temporary_path = Path(file.name)
            json.dump(records, file, indent=4, ensure_ascii=False)
            file.write("\n")
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
