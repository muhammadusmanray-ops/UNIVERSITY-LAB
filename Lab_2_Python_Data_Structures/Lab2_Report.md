# Lab 2: Python Data Structures & File Processing

## Objective
To work with Python data structures, functions, file I/O (CSV, JSON, Text), and list comprehensions for efficient data processing.

## Tasks Performed
1. **Data Structures**: Implemented Lists, Dictionaries, Tuples, and Sets for student management.
2. **File Processing**: Created functions to parse `students.csv` and `students.json`.
3. **Transformation**: Used List Comprehensions to calculate average grades and filter high-performing students.
4. **Error Handling**: Implemented `try-except` blocks for safe file reading and writing.
5. **Reporting**: Generated a final `grades_report.txt` summarizing student performance.

## Key Code Snippets
### List Comprehension for Averages
```python
student_averages = [
    {"name": s['name'], "avg": (s['math'] + s['science'] + s['english']) / 3} 
    for s in csv_data
]
```

## Results
- Successfully processed **5 students**.
- Identified **3 High Achievers** (Average > 80).
- Generated automated performance report.

## Screenshots
### Jupyter Notebook Execution
![Notebook Screenshot](notebook_screenshot.png)

### Terminal Output & Report Generation
![Terminal Output](terminal_output.png)
