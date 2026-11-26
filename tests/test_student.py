"""Tests for student subject management."""

import pytest

from grader.student import Student
from grader.subject import Subject


def test_student_with_multiple_subjects():
    student = Student("001", "John Smith")
    first = Subject("CS105", "Python", 85)
    second = Subject("MA101", "Calculus", 75)
    student.add_subject(first)
    student.add_subject(second)
    assert student.get_subject("CS105") is first
    assert list(student.iter_subjects()) == [first, second]
    assert student.average_score == 80
    assert "John Smith" in str(student)


@pytest.mark.parametrize("student_id,name", [("", "John"), ("001", "")])
def test_empty_student_fields(student_id, name):
    with pytest.raises(ValueError):
        Student(student_id, name)


def test_empty_student_has_no_average():
    assert Student("001", "John").average_score is None


def test_subject_dictionaries_are_independent():
    first = Student("001", "John")
    second = Student("002", "Alice")
    first.add_subject(Subject("CS105", "Python", 85))
    assert second.subjects == {}


def test_duplicate_and_missing_subjects():
    student = Student("001", "John")
    student.add_subject(Subject("CS105", "Python", 85))
    with pytest.raises(ValueError):
        student.add_subject(Subject("CS105", "Python", 75))
    with pytest.raises(KeyError):
        student.get_subject("MA101")
    student.remove_subject("CS105")
    assert student.subjects == {}
