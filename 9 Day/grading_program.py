student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}

for name, score in student_scores.items():
    if score <= 70:
        student_grades[name] = "Fail"
    elif score >= 71 and score <= 80:
        student_grades[name] = "Acceptable"
    elif score >= 81 and score <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 91 and score <= 100:
        student_grades[name] = "Outstanding"
    

print(student_grades)
