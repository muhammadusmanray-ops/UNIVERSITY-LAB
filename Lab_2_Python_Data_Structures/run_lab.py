import csv
import json
import os

# 1. Setup paths
cwd = r'C:\Users\muham\.gemini\antigravity\scratch\university-ai-lab-2'
csv_path = os.path.join(cwd, 'students.csv')
report_path = os.path.join(cwd, 'grades_report.txt')

print("--- Running Lab 2 Data Processing ---")

# 2. Process CSV
data = []
try:
    with open(csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['math'] = int(row['math'])
            row['science'] = int(row['science'])
            row['english'] = int(row['english'])
            data.append(row)
    print(f"Successfully loaded {len(data)} students.")
except Exception as e:
    print(f"Error: {e}")

# 3. Calculate Averages (List Comprehension)
student_averages = [
    {"name": s['name'], "avg": (s['math'] + s['science'] + s['english']) / 3} 
    for s in data
]

# 4. Save Report
try:
    with open(report_path, 'w') as f:
        f.write("STUDENT PERFORMANCE REPORT\n")
        f.write("=" * 30 + "\n")
        for item in student_averages:
            f.write(f"{item['name']}: {item['avg']:.2f}\n")
    print(f"Report generated at: {report_path}")
except Exception as e:
    print(f"Error writing report: {e}")

# 5. Display high achievers for user
high_achievers = [s for s in student_averages if s['avg'] > 80]
print("\n--- High Achievers ---")
for s in high_achievers:
    print(f"{s['name']}: {s['avg']:.2f}")
