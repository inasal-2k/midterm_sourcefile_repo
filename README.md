# Midterm Source Files

This repository contains Python programs developed for midterm lessons and
activities. The examples focus on processing student scores and producing
grade summaries.

## Repository contents

| Folder | Source file | Description |
| --- | --- | --- |
| `Lesson1/` | `Valerio.py` | Prints student scores and calculates pass/fail counts and basic score statistics. |
| `Lesson2/` | `student_grade_analyzer.py` | Loads student records from a text file, classifies grades, calculates statistics, supports searching, and can save a report. |
| `Lesson3/` | `Valerio_Raymund_StudentGradeAnalyzer.py` | Validates sample student records, ranks students, and prints grade and class summaries. |

## Requirements

- Python 3
- No third-party packages are required.

## Running the programs

From the repository root, run the standalone examples with:

```bash
python Lesson1/Valerio.py
python Lesson3/Valerio_Raymund_StudentGradeAnalyzer.py
```

The Lesson 2 program expects a `grades.txt` file in its current working
directory. Each data line must contain three comma-separated values in this
order: student ID, student name, and grade. Blank lines and lines beginning
with `#` are ignored. Run it from the `Lesson2` directory after adding the
input file there:

```bash
cd Lesson2
python student_grade_analyzer.py
```

The program can save its generated report as `grade_report.txt` in the current
working directory.