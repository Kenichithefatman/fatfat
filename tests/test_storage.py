"""Tests for JSON persistence and corrupted data protection."""

import pytest

from grader import storage
from grader.manager import StudentManager
from grader.storage import load_students, save_students
from grader.student import Student
from grader.subject import Subject


def test_save_and_load_multiple_subjects(tmp_path):
    path = tmp_path / "data" / "students.json"
    manager = StudentManager()
    student = Student("0001", "John")
    student.add_subject(Subject("CS105", "Python", 85))
    student.add_subject(Subject("MA101", "Calculus", 75))
    manager.add_student(student)
    save_students(manager, path)
    loaded = load_students(path)
    assert loaded.find_student("0001").average_score == 80
    assert loaded.find_student("0001").get_subject("MA101").grade == "B"


def test_missing_file_starts_empty(tmp_path):
    assert load_students(tmp_path / "missing.json").students == {}


@pytest.mark.parametrize("contents", ["{bad", "[]", '{"001": {"name": "John"}}',
                                      ('{"001": {"name": "John", "subjects": '
                                       '{"CS105": {"name": "Python", "score": true}}}}')])
def test_corrupted_file_is_preserved(tmp_path, contents):
    path = tmp_path / "students.json"
    path.write_text(contents, encoding="utf-8")
    with pytest.raises(ValueError):
        load_students(path)
    with pytest.raises(ValueError):
        save_students(StudentManager(), path)
    assert path.read_text(encoding="utf-8") == contents


def test_failed_replace_preserves_previous_file(tmp_path, monkeypatch):
    path = tmp_path / "students.json"
    manager = StudentManager()
    manager.add_student(Student("001", "John"))
    save_students(manager, path)
    original = path.read_text(encoding="utf-8")
    manager.add_student(Student("002", "Alice"))

    def fail_replace(source, destination):
        raise PermissionError("Cannot replace file")

    monkeypatch.setattr(storage.os, "replace", fail_replace)
    with pytest.raises(PermissionError):
        save_students(manager, path)
    assert path.read_text(encoding="utf-8") == original
