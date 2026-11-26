# Student Grader System

## 1. Project Information

- Course: CS105BKK
- Project: Final Project
- Project Name: Student Grader System
- Project Type: Individual Project
- Language: Python 3.12 or newer
- Application Type: Command-Line Interface (CLI)
- Database Format: JSON

## 2. Project Overview

The Student Grader System is a command-line application designed to manage student academic records.

The system allows administrators to register students, manage multiple subjects, enter scores, update scores, and automatically calculate grades.

Students can enter their student ID to view their academic results across all registered subjects.

All student information must be stored permanently in a JSON file and remain available after restarting the application.

The project must demonstrate the Python concepts taught in CS105BKK while remaining simple, readable, maintainable, and easy to explain during the final presentation.

## 3. Project Objectives

- Manage multiple students.
- Support multiple subjects for each student.
- Automatically calculate grades from scores.
- Search students using their student IDs.
- Display individual academic results.
- Calculate average scores.
- Store data permanently using JSON.
- Demonstrate object-oriented programming.
- Demonstrate composition and encapsulation.
- Demonstrate exception handling.
- Demonstrate a custom generator.
- Include automated tests.
- Satisfy all mandatory teacher requirements.

## 4. Official Teacher Requirements

Source: CS105BKK-final-project.docx

The final project is worth 30% of the course grade.

### Requirement 1: Runnable Application (S5)

- The application must run using Python 3.12 or newer.
- The application must work from a fresh Git clone.
- The application must start using `python main.py` or `python -m <package>`.
- README.md must explain how to run the application on Windows and macOS.

### Requirement 2: Classes (S2–S4)

- Implement at least three classes.
- Each class must have one clear responsibility.
- Use a dataclass, @property, or a dunder method such as __str__.
- Use composition or inheritance where appropriate.

This project will use three primary classes, properties, dunder methods, and composition.

### Requirement 3: Package (S5)

- Include a Python package directory.
- Include at least two modules inside the package.
- Include the following entry-point guard:

```python
if __name__ == "__main__":
    main()
```

### Requirement 4: Error Handling (S6)

- Invalid user input must not crash the application with a traceback.
- Missing files must be handled safely.
- Broken or corrupted files must be handled safely.

### Requirement 5: File Persistence (S7)

- Store application data using CSV or JSON.
- Use pathlib for file operations.
- Load previously saved data when the application starts again.

This project will use JSON.

### Requirement 6: Advanced Python (S9)

Implement at least one self-written:

- Generator
- Decorator
- Context manager

This project will implement a custom generator using yield.

### Requirement 7: Testing (S10)

- Include at least eight pytest tests.
- Cover normal cases, boundary values, and invalid input.
- All tests must pass using:

```bash
python -m pytest
```

### Requirement 8: Code Quality and Git (S11)

- Follow PEP 8 naming conventions.
- Include meaningful docstrings.
- Include a .gitignore file.
- Ruff must pass using:

```bash
python -m ruff check .
```

Individual projects require at least five commits with clear commit messages.

For team projects, members must work on branches, merge at least one pull request, and have contributions from every member in the Git history.

### Requirement 9: Public API Bonus (S12)

The optional bonus requires:

- A public API that does not require an API key.
- A saved JSON copy of an API response.
- Offline application support.

This feature is currently excluded from the project scope.

Do not implement any API integration until explicitly requested.

### Requirement 10: Presentation (S15)

- Seven-minute presentation.
- Live application demonstration.
- Five-minute question-and-answer session.
- Explain one design decision.
- Explain one real bug that was fixed.
- Every member must present and answer questions for team projects.

## 5. Project Scope

### Required Features

- Student registration.
- Student ID lookup.
- Multiple subjects per student.
- Subject registration for individual students.
- Score management.
- Automatic grade calculation.
- Average score calculation.
- Student record deletion.
- Subject deletion.
- JSON data persistence.
- Admin Mode.
- Student Mode.
- Input validation.
- Automated testing.

### Features Outside the Current Scope

Do not implement:

- Websites.
- Graphical user interfaces.
- Flask or Django.
- SQL databases.
- Cloud databases.
- Public APIs.
- Complex authentication systems.
- Password management.
- Machine learning.
- Artificial intelligence features.
- GPA calculations.
- Unnecessary third-party libraries.

Admin Mode and Student Mode are demonstration roles, not secure authentication systems.

Use fictional student records only.

## 6. Expected Project Structure

```text
student-grader/
│
├── main.py
│
├── grader/
│   ├── __init__.py
│   ├── student.py
│   ├── subject.py
│   ├── manager.py
│   ├── storage.py
│   └── menu.py
│
├── data/
│   └── students.json
│
├── tests/
│   ├── test_student.py
│   ├── test_subject.py
│   ├── test_manager.py
│   └── test_storage.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

Inspect the existing repository before creating or moving files.

If equivalent files already exist, reuse and improve them rather than creating duplicate implementations.

Keep package names consistent and use lowercase naming.

## 7. System Architecture

The application must separate user interaction, business logic, and data storage.

```text
User
  |
  v
main.py
  |
  v
menu.py
  |
  v
StudentManager
  |
  v
Student
  |
  v
Subject
```

The storage module is responsible for saving and loading student records.

```text
StudentManager
      |
      v
storage.py
      |
      v
students.json
```

Do not place all application logic inside main.py.

## 8. Class Design

### 8.1 Student Class

File: grader/student.py

Responsibility:

Represent one student and manage that student's subjects.

Attributes:

- student_id
- name
- subjects

The subjects attribute must be a dictionary containing Subject objects.

Use subject codes as dictionary keys.

Required methods:

- __init__()
- add_subject()
- remove_subject()
- get_subject()
- iter_subjects()
- __str__()

Required property:

- average_score

Rules:

- Student IDs must be non-empty strings.
- Student names must not be empty.
- Each student must have an independent subjects dictionary.
- Duplicate subject codes are not allowed within the same student.
- Different students may register for the same subject.
- A student may have zero subjects.
- A student without subjects must not cause division by zero.
- The average_score property should return None when no subjects exist.
- The menu should display N/A when no average is available.

Do not store a single score or grade directly inside the Student class.

Each student can have multiple subjects with different scores.

### 8.2 Subject Class

File: grader/subject.py

Responsibility:

Represent one academic subject result belonging to a student.

Attributes:

- subject_code
- subject_name
- _score

Required methods and properties:

- __init__()
- score
- score setter
- grade
- __str__()

Rules:

- Subject codes must not be empty.
- Subject names must not be empty.
- Scores must be integers between 0 and 100.
- Reject boolean values as scores.
- Invalid scores must raise ValueError.
- The score property must use a setter for validation.
- The grade property must calculate the grade from the current score.
- Do not store grades as separate mutable attributes.

Example:

```python
subject = Subject("CS105", "Python", 85)

print(subject.grade)
# A

subject.score = 65

print(subject.grade)
# C
```

### 8.3 StudentManager Class

File: grader/manager.py

Responsibility:

Manage the collection of students.

Attributes:

- students

The students attribute must be a dictionary.

Use student IDs as dictionary keys and Student objects as values.

Required methods:

- __init__()
- add_student()
- remove_student()
- find_student()
- get_all_students()
- update_score()

Rules:

- Duplicate student IDs are not allowed.
- Student IDs must remain strings.
- Searching for an unknown student must be handled safely.
- Updating a score must use the Subject score setter.
- StudentManager must not contain terminal input or printing logic.
- StudentManager must not directly manage JSON file operations.

## 9. Object-Oriented Programming Requirements

### Composition

Use composition because a Student contains multiple Subject objects, and a StudentManager contains multiple Student objects.

```text
StudentManager
    |
    +-- Student: John
    |     |
    |     +-- Python: 85
    |     +-- Calculus: 75
    |     +-- English: 65
    |
    +-- Student: Alice
          |
          +-- Python: 90
          +-- Calculus: 80
```

Do not introduce inheritance unless it solves a genuine problem.

### Encapsulation

Use the score property and setter to control how scores are modified.

The setter must prevent invalid scores from entering the application.

### Properties

Use @property for:

- Subject.score
- Subject.grade
- Student.average_score

Calculated values must reflect the current data.

### Dunder Methods

Implement meaningful __str__ methods for Student and Subject objects.

These methods should return readable descriptions of the objects.

## 10. Grading Rules

Use the following grading scale:

| Score | Grade |
|---|---|
| 80–100 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| 0–49 | F |

Use simple if, elif, and else statements.

Example:

```python
@property
def grade(self):
    if self.score >= 80:
        return "A"
    elif self.score >= 70:
        return "B"
    elif self.score >= 60:
        return "C"
    elif self.score >= 50:
        return "D"
    else:
        return "F"
```

Grades must be calculated automatically.

When a score changes, its grade must change automatically.

Do not store calculated grades in JSON.

## 11. Application Workflow

### Step 1: Application Startup

1. Execute main.py.
2. Create or load the StudentManager.
3. Check whether students.json exists.
4. Load previously saved student records.
5. Reconstruct Student and Subject objects.
6. Display the main menu.

If the file does not exist, start with an empty collection.

If the file is corrupted, display a clear error and protect the existing file from accidental overwriting.

### Step 2: Main Menu

Expected terminal interface:

```text
========================================
          STUDENT GRADER SYSTEM
========================================

1. Admin Mode
2. Student Mode
3. Exit

Enter your choice:
```

Invalid choices must display a friendly message and allow the user to try again.

### Step 3: Admin Mode

Expected interface:

```text
============== ADMIN MENU ==============

1. Register Student
2. Add Subject and Score
3. Update Subject Score
4. View All Students
5. Delete Subject
6. Delete Student
7. Return to Main Menu

Enter your choice:
```

#### Register Student

1. Ask for student ID.
2. Ask for student name.
3. Validate both values.
4. Check for duplicate IDs.
5. Create a Student object.
6. Add the student to StudentManager.
7. Save the updated records.
8. Display a success message only after saving succeeds.

Example:

```text
Enter student ID: 680001
Enter student name: John Smith

Student registered successfully.
```

#### Add Subject and Score

1. Ask for student ID.
2. Find the student.
3. Ask for subject code.
4. Ask for subject name.
5. Ask for score.
6. Validate all values.
7. Check for duplicate subject codes.
8. Create a Subject object.
9. Add the subject to the student.
10. Save the updated records.

Example:

```text
Enter student ID: 680001
Enter subject code: CS105
Enter subject name: Python
Enter score: 85

Subject added successfully.
Grade: A
```

#### Update Subject Score

1. Ask for student ID.
2. Find the student.
3. Display registered subjects.
4. Ask for subject code.
5. Ask for the new score.
6. Validate the new score.
7. Update the score.
8. Save the updated records.
9. Display the new calculated grade.

#### View All Students

Display all registered students.

Example:

```text
Student ID     Name              Subjects
------------------------------------------
680001         John Smith        3
680002         Alice Brown       2

Total students: 2
```

#### Delete Subject

1. Ask for student ID.
2. Find the student.
3. Display registered subjects.
4. Ask for subject code.
5. Request confirmation.
6. Remove the subject if confirmed.
7. Save the updated records.

#### Delete Student

1. Ask for student ID.
2. Find the student.
3. Display the student's name.
4. Request confirmation.
5. Remove the student if confirmed.
6. Save the updated records.

### Step 4: Student Mode

1. Ask for student ID.
2. Search StudentManager.
3. Display an error if the student does not exist.
4. Display the student's name and ID.
5. Display all registered subjects.
6. Display scores and calculated grades.
7. Display the total number of subjects.
8. Display the average score.
9. Allow the user to search again or return to the main menu.

Expected output:

```text
Enter student ID: 680001

============================================
             ACADEMIC RESULTS
============================================

Student ID: 680001
Student Name: John Smith

Code       Subject          Score     Grade
--------------------------------------------
CS105      Python             85        A
MA101      Calculus           75        B
EN101      English            65        C
CY101      Cybersecurity      90        A
--------------------------------------------

Total Subjects: 4
Average Score: 78.75

============================================
```

Student Mode must not allow users to modify academic records.

### Step 5: Exit

- Exit safely.
- Do not lose successfully saved records.
- Display a goodbye message.

## 12. JSON Data Persistence

File: grader/storage.py

Data file: data/students.json

Use only the standard library for JSON storage.

Required modules:

```python
import json
from pathlib import Path
```

Expected JSON structure:

```json
{
    "680001": {
        "name": "John Smith",
        "subjects": {
            "CS105": {
                "name": "Python",
                "score": 85
            },
            "MA101": {
                "name": "Calculus",
                "score": 75
            },
            "EN101": {
                "name": "English",
                "score": 65
            }
        }
    },
    "680002": {
        "name": "Alice Brown",
        "subjects": {
            "CS105": {
                "name": "Python",
                "score": 90
            }
        }
    }
}
```

Required functions:

- load_students()
- save_students()

Storage rules:

- Use pathlib for file paths.
- Resolve the default data path relative to the project directory.
- Allow tests to supply temporary file paths.
- Use UTF-8 encoding.
- Preserve student IDs as strings.
- Convert objects into dictionaries before saving.
- Reconstruct objects when loading.
- Save after every successful modification.
- Create missing directories when necessary.
- Validate loaded data.
- Do not silently discard corrupted records.
- Do not overwrite a corrupted data file automatically.
- Use a temporary file and replace the original only after writing succeeds.
- Report file operation failures clearly.
- If saving fails, revert the attempted modification or stop further editing safely.

The application must distinguish between a missing file and a corrupted file.

A missing file can represent a new application.

A corrupted file must not be treated as an empty database and silently overwritten.

## 13. Advanced Python: Custom Generator

Implement a generator inside the Student class.

```python
def iter_subjects(self):
    """Yield each subject belonging to the student."""
    for subject in self.subjects.values():
        yield subject
```

Use this generator when displaying academic results.

```python
for subject in student.iter_subjects():
    print(subject.subject_name, subject.score, subject.grade)
```

The generator must be used by the actual application.

Do not implement an unused generator only to satisfy the teacher's requirement.

## 14. Error Handling Requirements

The application must handle ordinary invalid input without crashing.

Required cases:

- Invalid menu choice.
- Empty student ID.
- Empty student name.
- Duplicate student ID.
- Student not found.
- Empty subject code.
- Empty subject name.
- Duplicate subject code.
- Subject not found.
- Non-numeric score.
- Negative score.
- Score greater than 100.
- Boolean score.
- Student without subjects.
- Missing JSON file.
- Corrupted JSON file.
- Invalid JSON structure.
- File permission errors.
- Failed file writes.

Use specific exceptions where appropriate.

Examples:

- ValueError
- KeyError
- FileNotFoundError
- PermissionError
- OSError
- json.JSONDecodeError

Do not use empty except blocks.

Do not hide unexpected errors with unnecessary broad exception handling.

Business logic should raise appropriate exceptions.

The menu should catch expected exceptions and display friendly messages.

## 15. Testing Requirements

Use pytest.

The teacher requires at least eight tests.

Implement the following core test cases.

### Student Tests

- Create a valid student.
- Reject an empty student ID.
- Reject an empty student name.
- Add multiple subjects.
- Reject duplicate subject codes.
- Calculate average scores.
- Handle a student with no subjects.
- Verify that students have independent subject dictionaries.
- Verify that the generator yields the correct subjects.

### Subject Tests

Test grade boundaries:

| Score | Expected Grade |
|---|---|
| 100 | A |
| 80 | A |
| 79 | B |
| 70 | B |
| 69 | C |
| 60 | C |
| 59 | D |
| 50 | D |
| 49 | F |
| 0 | F |

Also test:

- Reject negative scores.
- Reject scores above 100.
- Reject non-integer scores.
- Reject boolean scores.
- Update a score and verify the new grade.

### StudentManager Tests

- Register a student.
- Register multiple students.
- Reject duplicate student IDs.
- Find an existing student.
- Handle an unknown student.
- Remove a student.
- Update a subject score.

### Storage Tests

- Save student records.
- Load saved student records.
- Preserve multiple subjects after saving and loading.
- Preserve student IDs containing leading zeros.
- Handle missing JSON files.
- Handle corrupted JSON files.
- Handle invalid JSON structures.
- Protect corrupted files from being overwritten.

Use pytest's tmp_path fixture for file tests.

Tests must never modify real application data.

Use pytest.mark.parametrize where appropriate for grade boundaries.

Run:

```bash
python -m pytest
```

All tests must pass.

Do not modify correct expected results simply to make failing tests pass.

## 16. Coding Standards

All code must follow these rules.

### Naming

- Classes: PascalCase
- Functions: snake_case
- Variables: snake_case
- Constants: UPPER_CASE

### Readability

- Use meaningful variable names.
- Use clear and simple English.
- Include meaningful docstrings.
- Prefer explicit and readable logic.
- Keep functions focused on one responsibility.
- Avoid unnecessary code duplication.
- Add comments only when they improve understanding.

### Complexity Restrictions

Prefer Python concepts taught in the course.

Allowed concepts:

- Variables
- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- Classes and objects
- Composition
- Properties
- Dunder methods
- Generators
- Exception handling
- Modules and packages
- JSON
- pathlib
- pytest
- Simple type hints

Avoid unnecessary:

- Abstract base classes
- Metaclasses
- Complex design patterns
- Asynchronous programming
- Multithreading
- Dependency injection frameworks
- Complicated decorators
- Excessive inheritance
- Unreadable one-line expressions

The goal is not to create the most advanced implementation.

The goal is to create a correct application that a first-year university student can understand and explain.

### Code Quality Verification

Run:

```bash
python -m ruff check .
```

Fix all reported linting errors.

Do not disable lint rules merely to hide problems.

## 17. Entry Point

File: main.py

The main.py file must remain simple.

Responsibilities:

- Initialize the application.
- Load saved student records.
- Start the command-line menu.
- Handle startup errors safely.

Use:

```python
if __name__ == "__main__":
    main()
```

Importing modules must not automatically start the application.

## 18. Installation and Running

Python 3.12 or newer is required.

### macOS

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install development dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

### Windows PowerShell

Create a virtual environment:

```powershell
py -3.12 -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install development dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the application:

```powershell
python main.py
```

### Requirements

The requirements.txt file should contain:

```text
pytest
ruff
```

The application itself should use only the Python standard library.

## 19. Git Requirements

The teacher requires at least five meaningful commits for individual projects.

Recommended development commits:

1. Create project structure and Subject class
2. Implement Student class and subject management
3. Implement StudentManager and student lookup
4. Add JSON storage and error handling
5. Implement command-line menus
6. Add automated tests
7. Complete documentation and final verification

Commit messages must describe actual completed work.

Do not create empty or artificial commits to satisfy the commit count.

Inspect existing Git history before suggesting new commits.

Do not rewrite existing Git history.

Do not force push.

Do not commit, merge, push, or delete branches without explicit user permission.

The final working version must be available on the repository's default branch before submission.

## 20. Development Workflow for Codex

Follow these phases in order.

### Phase 0: Inspect the Existing Repository

- Read the entire README.
- Inspect existing files.
- Inspect the current package structure.
- Inspect the existing Student class.
- Inspect Git status and existing commits.
- Identify incomplete or incorrect implementations.
- Preserve useful existing code.
- Report the implementation plan before making major structural changes.

Do not recreate the entire repository unnecessarily.

### Phase 1: Subject Class

- Implement the Subject class.
- Implement score validation.
- Implement the score property and setter.
- Implement the grade property.
- Implement __str__.
- Test all grade boundaries.

Expected result:

A Subject object correctly validates scores and calculates grades.

### Phase 2: Student Class

- Implement student ID and name validation.
- Implement the subjects dictionary.
- Implement adding and removing subjects.
- Implement subject lookup.
- Implement average score calculation.
- Implement the custom generator.
- Test multiple subjects and independent student objects.

Expected result:

One student can contain multiple independent Subject objects.

### Phase 3: StudentManager Class

- Implement student registration.
- Implement student lookup.
- Implement duplicate ID validation.
- Implement student removal.
- Implement score updates.
- Test student management operations.

Expected result:

The application can manage multiple students using student IDs.

### Phase 4: JSON Storage

- Implement JSON serialization.
- Implement JSON deserialization.
- Use pathlib.
- Implement safe file saving.
- Implement missing-file handling.
- Implement corrupted-file handling.
- Test saving and loading.

Expected result:

Student records remain available after closing and restarting the application.

### Phase 5: Command-Line Interface

- Implement the main menu.
- Implement Admin Mode.
- Implement Student Mode.
- Connect the menus to StudentManager.
- Connect data modifications to JSON storage.
- Implement friendly error messages.
- Implement confirmation before deleting records.

Expected result:

Users can complete the entire application workflow through the terminal.

### Phase 6: Automated Testing

- Complete all required pytest tests.
- Run the full test suite.
- Investigate failing tests.
- Fix actual implementation problems.
- Run the tests again.

Expected result:

All tests pass.

### Phase 7: Code Quality

- Run Ruff.
- Fix linting errors.
- Review naming conventions.
- Add missing docstrings.
- Remove unused imports.
- Remove unused code.
- Check that every module has one clear purpose.

Expected result:

Ruff passes without errors.

### Phase 8: Integration Verification

Manually verify the following scenario:

1. Start the application.
2. Register student 680001 named John Smith.
3. Add Python with a score of 85.
4. Add Calculus with a score of 75.
5. Add English with a score of 65.
6. Open Student Mode.
7. Search for student 680001.
8. Verify grades A, B, and C.
9. Verify that the average score is 75.00.
10. Update Calculus to 95.
11. Verify that Calculus changes to grade A.
12. Verify that the new average score is approximately 81.67.
13. Exit the application.
14. Restart the application.
15. Verify that all updated records still exist.
16. Enter invalid input and verify that the application does not crash.

Use temporary or fictional data for verification.

### Phase 9: Final Documentation

- Verify Windows installation instructions.
- Verify macOS installation instructions.
- Update the project structure if necessary.
- Document the implemented features.
- Document important design decisions.
- Document actual bugs discovered and fixed.
- Report remaining limitations.
- Prepare the application for the live demonstration.

## 21. Strict Instructions for Codex

These instructions apply throughout the entire implementation.

### Implementation Rules

1. Read and follow this README before writing code.
2. Treat the official teacher requirements as mandatory.
3. Do not implement the optional API bonus.
4. Do not change the grading scale.
5. Do not remove multiple-subject support.
6. Do not remove JSON persistence.
7. Do not introduce unnecessary features.
8. Do not introduce unnecessary dependencies.
9. Do not create duplicate files or duplicate classes.
10. Do not replace existing working code without a clear reason.
11. Keep the implementation at a beginner-to-intermediate Python level.
12. Use simple and readable solutions.
13. Keep user interaction separate from business logic.
14. Keep storage logic separate from student management.
15. Do not hardcode student records into the application.
16. Do not hardcode calculated grades or averages.
17. Do not use real personal or academic information.
18. Do not leave unfinished TODO implementations in required features.
19. Do not fabricate test results.
20. Do not fabricate Git commits or bug-fix history.
21. Do not modify teacher requirements to match an incomplete implementation.
22. Do not perform destructive Git operations.
23. Ask for clarification when a major requirement is ambiguous.
24. Do not claim completion until mandatory checks have been executed.

### Communication Rules

Before implementation:

- Summarize the existing repository structure.
- Explain what needs to be created or modified.
- Present the implementation plan.

After each phase:

- Explain what was completed.
- Identify the files created or modified.
- Explain important design decisions.
- Report any errors encountered.
- Report the actual verification results.

After implementation:

- Provide a complete summary of the project.
- Explain the responsibility of every file.
- Explain the responsibility of every class.
- Explain how data moves through the application.
- Explain where composition is used.
- Explain where encapsulation is used.
- Explain where the generator is used.
- Explain how JSON persistence works.
- Report the number of passing and failing tests.
- Report the Ruff result.
- Report any remaining limitations.
- Suggest meaningful Git commit commands without executing them automatically.

The student must be able to understand and explain the implementation.

## 22. Definition of Done

The project is complete only when all mandatory requirements have been verified.

### Application

- [ ] Application runs with Python 3.12 or newer.
- [ ] Application starts using python main.py.
- [ ] Main menu works.
- [ ] Admin Mode works.
- [ ] Student Mode works.
- [ ] Multiple students are supported.
- [ ] Multiple subjects per student are supported.
- [ ] Student lookup works.
- [ ] Score updates work.
- [ ] Grades are calculated correctly.
- [ ] Average scores are calculated correctly.
- [ ] Student deletion works.
- [ ] Subject deletion works.

### Python Concepts

- [ ] At least three classes.
- [ ] Clear class responsibilities.
- [ ] Composition.
- [ ] Encapsulation.
- [ ] Properties.
- [ ] Dunder methods.
- [ ] Custom generator.
- [ ] Python package.
- [ ] Main guard.
- [ ] Exception handling.

### Data Persistence

- [ ] JSON storage.
- [ ] pathlib.
- [ ] Save and load functionality.
- [ ] Data survives application restart.
- [ ] Missing files are handled.
- [ ] Corrupted files are handled.
- [ ] Existing records are protected from accidental data loss.

### Testing and Quality

- [ ] At least eight pytest tests.
- [ ] All tests pass.
- [ ] Ruff passes.
- [ ] PEP 8 naming conventions.
- [ ] Meaningful docstrings.
- [ ] .gitignore exists.
- [ ] No unnecessary dependencies.

### Git and Submission

- [ ] At least five meaningful commits for an individual project.
- [ ] Public GitHub repository.
- [ ] Final implementation on the default branch.
- [ ] README contains Windows instructions.
- [ ] README contains macOS instructions.
- [ ] Fresh clone works correctly.
- [ ] Repository ZIP prepared.
- [ ] GitHub link submitted to Google Classroom.
- [ ] ZIP submitted to Google Classroom.

### Presentation

- [ ] Seven-minute presentation prepared.
- [ ] Live demonstration prepared.
- [ ] Five-minute Q&A prepared.
- [ ] One design decision explained.
- [ ] One actual bug fix explained.

## 23. Submission Rules

According to the official CS105BKK final project document:

- Project proposal deadline: Wednesday, 25 November 2026, 23:59.
- Consultation and rehearsal: Thursday, 26 November 2026.
- Code freeze: Friday, 27 November 2026, at the start of class.
- Final presentation: Friday, 27 November 2026.

Before the code freeze, submit:

- Public GitHub repository link.
- ZIP copy of the repository.

Submit both through Google Classroom.

For team projects, every member must submit.

The teacher will grade a fresh clone of the repository as it exists at the code freeze.

Later commits do not count.

Missing the presentation without a valid reason results in a project score of zero.

## 24. Final Priority

The implementation must prioritize the following, in order:

1. Compliance with official teacher requirements.
2. Correctness.
3. Data integrity.
4. Simplicity.
5. Readability.
6. Maintainability.
7. Ease of explanation during the presentation.

Do not sacrifice correctness for additional features.

Do not sacrifice readability for unnecessarily advanced Python techniques.

## 25. Implemented Application

The required command-line features are implemented in `main.py` and the
`grader` package. Admin Mode registers and deletes students, adds and deletes
subjects, updates scores, and lists students. Student Mode displays a student's
subjects, grades, and average without editing records. Changes are saved to
`data/students.json` after each successful edit. The file starts as `{}`.

The three business classes use composition: `StudentManager` contains students,
and each `Student` contains subjects. `Subject.score` validates assignments;
`Subject.grade` and `Student.average_score` calculate current values rather
than storing duplicate data. `Student.iter_subjects()` is the custom generator
used by the results display. Storage validates loaded JSON and writes through
a temporary file before replacing the original. A corrupt data file stops
startup and is left in place for inspection.

Run the checks after installing `requirements.txt`:

```bash
python -m pytest
python -m ruff check .
```

The application uses only the Python standard library. Admin Mode and Student
Mode are demonstration roles without authentication. Grades are individual
letter grades; GPA is outside the project scope. Use fictional records during
demonstrations.

Complete the required project before considering optional improvements.
