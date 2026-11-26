"""Exercise the CLI across two application launches."""

import json
import shutil
import subprocess
import sys
from pathlib import Path


def test_cli_saves_updated_grades_across_restart(tmp_path):
    source = Path(__file__).resolve().parents[1]
    shutil.copy(source / "main.py", tmp_path)
    shutil.copytree(source / "grader", tmp_path / "grader",
                    ignore=shutil.ignore_patterns("__pycache__"))
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "students.json").write_text("{}", encoding="utf-8")

    first_input = (
        "1\n1\n680001\nJohn Smith\n"
        "2\n680001\nCS105\nPython\n85\n"
        "2\n680001\nMA101\nCalculus\n75\n"
        "2\n680001\nEN101\nEnglish\n65\n"
        "7\n2\n680001\nn\n1\n3\n680001\nMA101\n95\n7\n3\n"
    )
    first = subprocess.run(
        [sys.executable, "main.py"], input=first_input, text=True,
        capture_output=True, cwd=tmp_path, check=True,
    )
    assert "Average Score: 75.00" in first.stdout
    assert "Score updated. Grade: A" in first.stdout

    second = subprocess.run(
        [sys.executable, "main.py"], input="2\n680001\nn\n3\n",
        text=True, capture_output=True, cwd=tmp_path, check=True,
    )
    assert "Average Score: 81.67" in second.stdout
    records = json.loads((tmp_path / "data" / "students.json").read_text(
        encoding="utf-8"))
    assert records["680001"]["subjects"]["MA101"]["score"] == 95
