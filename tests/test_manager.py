"""Tests for student collection operations."""

import pytest

from grader.manager import StudentManager
from grader.student import Student
from grader.subject import Subject


def test_register_find_and_remove_students():
    manager = StudentManager()
    first = Student("001", "John")
    second = Student("002", "Alice")
    manager.add_student(first)
    manager.add_student(second)
    assert manager.find_student("001") is first
    assert manager.find_student("unknown") is None
    assert len(manager.get_all_students()) == 2
    manager.remove_student("001")
    assert manager.find_student("001") is None
    with pytest.raises(KeyError):
        manager.remove_student("001")


def test_duplicate_student_id():
    manager = StudentManager()
    manager.add_student(Student("001", "John"))
    with pytest.raises(ValueError):
        manager.add_student(Student("001", "Alice"))


def test_update_score_uses_validation():
    manager = StudentManager()
    student = Student("001", "John")
    student.add_subject(Subject("CS105", "Python", 85))
    manager.add_student(student)
    manager.update_score("001", "CS105", 65)
    assert student.get_subject("CS105").grade == "C"
    with pytest.raises(ValueError):
        manager.update_score("001", "CS105", True)
    with pytest.raises(KeyError):
        manager.update_score("002", "CS105", 90)
