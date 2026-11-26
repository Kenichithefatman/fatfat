"""Tests for score validation and grade boundaries."""

import pytest

from grader.subject import Subject


@pytest.mark.parametrize("score,grade", [
    (100, "A"), (80, "A"), (79, "B"), (70, "B"),
    (69, "C"), (60, "C"), (59, "D"), (50, "D"),
    (49, "F"), (0, "F"),
])
def test_grade_boundaries(score, grade):
    assert Subject("CS105", "Python", score).grade == grade


@pytest.mark.parametrize("score", [-1, 101, 1.5, "85", True, False])
def test_invalid_scores(score):
    with pytest.raises(ValueError):
        Subject("CS105", "Python", score)


def test_score_update_changes_grade():
    subject = Subject("CS105", "Python", 85)
    subject.score = 65
    assert subject.grade == "C"


@pytest.mark.parametrize("code,name", [("", "Python"), ("CS105", "")])
def test_empty_subject_fields(code, name):
    with pytest.raises(ValueError):
        Subject(code, name, 85)
