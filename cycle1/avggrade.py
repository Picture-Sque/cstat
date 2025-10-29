student_grades = {
"Maths" : 100,
"Science" : 98,
"History" : 100,
"Geography" : 100,
"English" : 98

}

def average_grade(grades):
 if not grades:
  return 0
 total = sum(grades.values())
 count = len(grades)
 average = total / count
 return average

saverage = average_grade(student_grades)
print(f"The average grade of student : {saverage} ")
